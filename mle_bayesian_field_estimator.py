"""
Maximum Likelihood and Bayesian Electric Field Estimation
for Rydberg Atom Sensors

This implements optimal statistical estimation of electric fields from
Autler-Townes splitting measurements, including uncertainty quantification.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit, minimize
from scipy.stats import norm
import emcee  # MCMC sampler for Bayesian inference

# Physical constants
HBAR = 1.054e-34  # J·s
E_CHARGE = 1.602e-19  # C
BOHR_RADIUS = 5.29e-11  # m

def eit_autler_townes_model(x, C, A, Gamma, df):
    """
    Two-peak Lorentzian model for Autler-Townes split EIT spectrum.

    Parameters:
    -----------
    x : array
        Probe detuning (MHz)
    C : float
        Baseline offset
    A : float
        Peak amplitude
    Gamma : float
        Linewidth (MHz)
    df : float
        Autler-Townes splitting (MHz)

    Returns:
    --------
    y : array
        Transmission signal
    """
    return (C
            + A / ((x - df/2)**2 + Gamma**2)
            + A / ((x + df/2)**2 + Gamma**2))


class RydbergFieldEstimator:
    """
    Complete field estimation pipeline for Rydberg atom sensors.
    """

    def __init__(self, n=50, species='Rb'):
        """
        Initialize estimator with atomic parameters.

        Parameters:
        -----------
        n : int
            Principal quantum number
        species : str
            Atomic species ('Rb', 'Cs', 'K')
        """
        self.n = n
        self.species = species

        # Calculate dipole moment scaling (simplified)
        self.dipole_moment = E_CHARGE * BOHR_RADIUS * n**2

        # Atomic species data
        self.wavelengths = {'Rb': 780e-9, 'Cs': 852e-9, 'K': 770e-9}
        self.lambda_probe = self.wavelengths.get(species, 780e-9)

    def mle_single_scan(self, x, y, p0=None):
        """
        Maximum Likelihood Estimation from single EIT scan.

        Parameters:
        -----------
        x : array
            Probe detuning (MHz)
        y : array
            Measured transmission
        p0 : array, optional
            Initial parameter guess [C, A, Gamma, df]

        Returns:
        --------
        popt : array
            Optimal parameters
        pcov : array
            Covariance matrix
        """
        if p0 is None:
            # Intelligent initial guess
            C_guess = np.min(y)
            A_guess = np.max(y) - np.min(y)
            Gamma_guess = 5.0
            df_guess = 10.0
            p0 = [C_guess, A_guess, Gamma_guess, df_guess]

        # Fit using nonlinear least squares (= MLE for Gaussian noise)
        popt, pcov = curve_fit(eit_autler_townes_model, x, y, p0=p0)

        return popt, pcov

    def extract_field(self, df_MHz, sigma_df_MHz=None):
        """
        Convert frequency splitting to electric field.

        Parameters:
        -----------
        df_MHz : float
            Autler-Townes splitting (MHz)
        sigma_df_MHz : float, optional
            Uncertainty in splitting (MHz)

        Returns:
        --------
        E : float
            Electric field (V/m)
        sigma_E : float (if sigma_df provided)
            Field uncertainty (V/m)
        """
        df_Hz = df_MHz * 1e6
        E = (2 * np.pi * HBAR * df_Hz) / self.dipole_moment

        if sigma_df_MHz is not None:
            sigma_df_Hz = sigma_df_MHz * 1e6
            sigma_E = (2 * np.pi * HBAR * sigma_df_Hz) / self.dipole_moment
            return E, sigma_E

        return E

    def cramér_rao_bound(self, x, y, popt):
        """
        Calculate Cramér-Rao lower bound for splitting estimation.

        Parameters:
        -----------
        x, y : arrays
            Data points
        popt : array
            Fitted parameters

        Returns:
        --------
        sigma_df_min : float
            Minimum achievable uncertainty in splitting (MHz)
        """
        # Compute Fisher Information via numerical Jacobian
        eps = 1e-6
        J = np.zeros((len(x), len(popt)))

        for i in range(len(popt)):
            dp = np.zeros_like(popt)
            dp[i] = eps
            J[:, i] = (eit_autler_townes_model(x, *(popt + dp)) -
                      eit_autler_townes_model(x, *(popt - dp))) / (2*eps)

        # Residual variance
        residuals = y - eit_autler_townes_model(x, *popt)
        sigma2 = np.var(residuals)

        # Fisher Information Matrix
        FIM = (J.T @ J) / sigma2

        # CRLB for df (parameter index 3)
        cov = np.linalg.inv(FIM)
        sigma_df_min = np.sqrt(cov[3, 3])

        return sigma_df_min

    def multi_scan_fusion(self, df_list, sigma_list):
        """
        Optimal weighted averaging of multiple scans.

        Parameters:
        -----------
        df_list : array
            Splitting estimates from multiple scans (MHz)
        sigma_list : array
            Uncertainties for each scan (MHz)

        Returns:
        --------
        df_fused : float
            Fused splitting estimate
        sigma_fused : float
            Fused uncertainty
        """
        df_array = np.array(df_list)
        sigma_array = np.array(sigma_list)

        # Inverse variance weighting
        weights = 1.0 / sigma_array**2
        df_fused = np.sum(weights * df_array) / np.sum(weights)
        sigma_fused = np.sqrt(1.0 / np.sum(weights))

        return df_fused, sigma_fused


def bayesian_posterior_mcmc(x, y, sigma_noise, nwalkers=32, nsteps=3000):
    """
    Full Bayesian posterior inference using MCMC.

    Parameters:
    -----------
    x, y : arrays
        EIT spectrum data
    sigma_noise : float
        Estimated noise level
    nwalkers : int
        Number of MCMC walkers
    nsteps : int
        Number of MCMC steps

    Returns:
    --------
    samples : array
        MCMC samples from posterior
    """

    def log_prior(theta):
        C, A, Gamma, df = theta
        if A > 0 and Gamma > 0 and df > 0:
            return 0.0
        return -np.inf

    def log_likelihood(theta, x, y, sigma):
        model = eit_autler_townes_model(x, *theta)
        return -0.5 * np.sum(((y - model) / sigma)**2)

    def log_posterior(theta, x, y, sigma):
        lp = log_prior(theta)
        if not np.isfinite(lp):
            return -np.inf
        return lp + log_likelihood(theta, x, y, sigma)

    # Initial guess from MLE
    estimator = RydbergFieldEstimator()
    popt, _ = estimator.mle_single_scan(x, y)

    # Initialize walkers
    ndim = 4
    pos = popt + 1e-3 * np.random.randn(nwalkers, ndim)

    # Run MCMC
    sampler = emcee.EnsembleSampler(nwalkers, ndim, log_posterior,
                                     args=(x, y, sigma_noise))
    sampler.run_mcmc(pos, nsteps, progress=True)

    # Extract samples
    samples = sampler.get_chain(discard=1000, flat=True)

    return samples


def demonstrate_estimation():
    """
    Complete demonstration of MLE and Bayesian estimation.
    """
    print("=" * 60)
    print("Rydberg Atom Electric Field Estimation Demo")
    print("=" * 60)

    # Generate synthetic data
    x = np.linspace(-30, 30, 500)
    true_params = [0.1, 1.0, 3.0, 12.0]  # [C, A, Gamma, df]
    noise_level = 0.05
    y_true = eit_autler_townes_model(x, *true_params)
    y = y_true + noise_level * np.random.randn(len(x))

    # Initialize estimator
    estimator = RydbergFieldEstimator(n=50, species='Rb')

    # MLE estimation
    print("\n--- Maximum Likelihood Estimation ---")
    popt, pcov = estimator.mle_single_scan(x, y)
    sigma_df = np.sqrt(pcov[3, 3])

    print(f"True splitting: {true_params[3]:.3f} MHz")
    print(f"MLE splitting: {popt[3]:.3f} ± {sigma_df:.3f} MHz")

    # CRLB
    crlb = estimator.cramér_rao_bound(x, y, popt)
    print(f"Cramér-Rao bound: {crlb:.3f} MHz")
    print(f"Efficiency: {(crlb/sigma_df)**2 * 100:.1f}%")

    # Extract field
    E, sigma_E = estimator.extract_field(popt[3], sigma_df)
    print(f"\nExtracted E-field: {E:.3e} ± {sigma_E:.3e} V/m")

    # Multi-scan simulation
    print("\n--- Multi-Scan Fusion ---")
    n_scans = 10
    df_scans = []
    sigma_scans = []

    for _ in range(n_scans):
        y_scan = y_true + noise_level * np.random.randn(len(x))
        p, cov = estimator.mle_single_scan(x, y_scan)
        df_scans.append(p[3])
        sigma_scans.append(np.sqrt(cov[3, 3]))

    df_fused, sigma_fused = estimator.multi_scan_fusion(df_scans, sigma_scans)
    print(f"Single scan uncertainty: {np.mean(sigma_scans):.3f} MHz")
    print(f"Fused uncertainty ({n_scans} scans): {sigma_fused:.3f} MHz")
    print(f"Improvement factor: {np.mean(sigma_scans)/sigma_fused:.2f}")
    print(f"Theoretical √N: {np.sqrt(n_scans):.2f}")

    # Visualization
    plt.figure(figsize=(14, 5))

    # Subplot 1: Data and fit
    plt.subplot(1, 2, 1)
    plt.plot(x, y, 'k.', alpha=0.5, label='Data')
    plt.plot(x, eit_autler_townes_model(x, *popt), 'r-', lw=2, label='MLE Fit')
    plt.xlabel('Probe Detuning (MHz)', fontsize=12)
    plt.ylabel('Transmission (arb.)', fontsize=12)
    plt.title('Autler-Townes Spectrum Fitting', fontsize=14, weight='bold')
    plt.legend()
    plt.grid(True, alpha=0.3)

    # Subplot 2: Multi-scan convergence
    plt.subplot(1, 2, 2)
    cumulative_uncertainty = []
    for i in range(1, n_scans + 1):
        _, sig = estimator.multi_scan_fusion(df_scans[:i], sigma_scans[:i])
        cumulative_uncertainty.append(sig)

    plt.plot(range(1, n_scans + 1), cumulative_uncertainty, 'bo-', lw=2,
             label='Measured')
    plt.plot(range(1, n_scans + 1),
             sigma_scans[0] / np.sqrt(range(1, n_scans + 1)),
             'r--', lw=2, label='Theoretical 1/√N')
    plt.xlabel('Number of Scans', fontsize=12)
    plt.ylabel('Uncertainty (MHz)', fontsize=12)
    plt.title('Multi-Scan Uncertainty Reduction', fontsize=14, weight='bold')
    plt.legend()
    plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('field_estimation_demo.png', dpi=150, bbox_inches='tight')
    print("\nPlot saved as 'field_estimation_demo.png'")
    plt.show()


if __name__ == "__main__":
    demonstrate_estimation()
    print("\n" + "=" * 60)
    print("Estimation complete. Ready for deployment.")
    print("=" * 60)
