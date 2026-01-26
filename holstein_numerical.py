"""
Holstein Hamiltonian Numerical Diagonalization
Verifies analytical results from Lang-Firsov transformation
"""

import numpy as np
from scipy.linalg import eigh
from scipy.special import factorial

def build_holstein_matrix(epsilon, omega, lam, N_ph):
    """
    Build Holstein Hamiltonian matrix in phonon number basis

    Parameters:
    -----------
    epsilon : float
        Electronic energy
    omega : float
        Phonon frequency
    lam : float
        Electron-phonon coupling strength
    N_ph : int
        Maximum phonon number (truncation)

    Returns:
    --------
    H : ndarray
        Holstein Hamiltonian matrix
    """
    dim = N_ph + 1
    k = np.arange(dim)
    diag = epsilon + omega * k
    off = lam * np.sqrt(np.arange(1, dim))
    H = np.diag(diag) + np.diag(off, 1) + np.diag(off, -1)
    return H

# Parameters
epsilon = 1.0
omega = 1.0
N_ph = 20  # Increase for stronger coupling

# Energy shift verification
lambda_vals = np.linspace(0, 2, 100)
analytical_shift = epsilon - (lambda_vals ** 2) / omega

numerical_gs = []
for lam in lambda_vals:
    H = build_holstein_matrix(epsilon, omega, lam, N_ph)
    eigvals = eigh(H)[0]
    gs_energy = min(eigvals)
    numerical_gs.append(gs_energy)

print("Energy Shift Verification:")
print("Maximum difference (analytical vs numerical):",
      max(abs(np.array(analytical_shift) - np.array(numerical_gs))))

# Phonon probabilities for specific lambdas
lambda_test = [0.5, 1.0, 1.5]
print("\nPhonon Occupation Probabilities:")
for lam in lambda_test:
    g = lam / omega
    n = np.arange(N_ph + 1)
    analytical_probs = np.exp(-g**2) * (g**(2 * n)) / factorial(n)
    analytical_probs /= np.sum(analytical_probs)

    H = build_holstein_matrix(epsilon, omega, lam, N_ph)
    eigvals, eigvecs = eigh(H)
    idx_gs = np.argmin(eigvals)
    psi_gs = eigvecs[:, idx_gs]
    numerical_probs = np.abs(psi_gs)**2

    print(f"\nλ = {lam}:")
    print(f"  Ground state energy (analytical): {epsilon - lam**2/omega:.6f}")
    print(f"  Ground state energy (numerical):  {eigvals[idx_gs]:.6f}")
    print(f"  Max probability difference: {max(abs(analytical_probs - numerical_probs)):.2e}")

# Optional: Plotting (uncomment if matplotlib is available)
# import matplotlib.pyplot as plt
#
# plt.figure(figsize=(12, 5))
#
# # Energy shift plot
# plt.subplot(1, 2, 1)
# plt.plot(lambda_vals, analytical_shift, 'b-', linewidth=2, label='Analytical')
# plt.plot(lambda_vals, numerical_gs, 'r--', linewidth=2, label='Numerical')
# plt.xlabel('λ (Electron-Phonon Coupling)')
# plt.ylabel('Ground State Energy')
# plt.title('Polaron Energy Shift')
# plt.legend()
# plt.grid(True)
#
# # Phonon occupation plot
# plt.subplot(1, 2, 2)
# for i, lam in enumerate(lambda_test):
#     g = lam / omega
#     n = np.arange(11)
#     probs = np.exp(-g**2) * (g**(2 * n)) / factorial(n)
#     probs /= np.sum(probs)
#     plt.stem(n, probs, label=f'λ = {lam}', basefmt=' ')
#
# plt.xlabel('Phonon Number n')
# plt.ylabel('Probability P(n)')
# plt.title('Phonon Occupation Probabilities')
# plt.legend()
# plt.grid(True)
#
# plt.tight_layout()
# plt.savefig('holstein_verification.png', dpi=150)
# plt.show()

print("\nVerification complete!")
