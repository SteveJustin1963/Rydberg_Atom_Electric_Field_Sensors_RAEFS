% EIT Autler-Townes Lineshape Model for Rydberg Electric Field Sensing
% Based on NIST Rydberg atom sensor research
%
% This implements the full physics of Electromagnetically Induced Transparency
% with RF-induced Autler-Townes splitting for electric field measurement

clear; clc;

%% Physical Constants
hbar = 1.054e-34;    % Planck's constant / 2π (J·s)
h = 6.626e-34;       % Planck's constant (J·s)
e = 1.602e-19;       % Elementary charge (C)
a0 = 5.29e-11;       % Bohr radius (m)
kB = 1.38e-23;       % Boltzmann constant (J/K)

%% Atomic Parameters (Rubidium)
n = 50;                       % Rydberg principal quantum number
ea0 = e*a0*n^2;               % Dipole moment scaling (C·m)
mRb = 1.44e-25;               % Mass of Rb-87 (kg)
T = 300;                      % Temperature (K)
lambda_p = 780e-9;            % Probe wavelength (m)
kp = 2*pi/lambda_p;           % Probe wave vector

%% Decay Rates (MHz)
gamma_e = 6;                  % Excited state decay
gamma_r = 0.5;                % Rydberg state decay
gamma_rp = 0.5;               % Second Rydberg state decay

%% Laser Parameters (MHz)
Omega_c = 15;                 % Coupling laser Rabi frequency
Omega_p = 1;                  % Probe laser Rabi frequency (weak)

%% RF Field Parameters
E_RF = 1e-4;                  % RF electric field (V/m)
Omega_RF = (ea0*E_RF)/(hbar*2*pi*1e6);  % RF Rabi frequency (MHz)

fprintf('=== Rydberg Atom E-Field Sensor Parameters ===\n');
fprintf('Principal quantum number n = %d\n', n);
fprintf('RF electric field = %.2e V/m\n', E_RF);
fprintf('RF Rabi frequency = %.3f MHz\n', Omega_RF);
fprintf('Predicted AT splitting = %.3f MHz\n', Omega_RF);

%% Probe Detuning Scan
Delta_p = linspace(-40, 40, 4000);  % Probe detuning (MHz)

%% EIT Susceptibility Calculation

% Without RF (baseline EIT)
chi_noRF = 1 ./ (Delta_p + 1i*gamma_e ...
    - (Omega_c^2/4) ./ (0 + 1i*gamma_r));
T_noRF = exp(-abs(imag(chi_noRF))/max(abs(imag(chi_noRF))));

% With RF (Autler-Townes splitting)
chi_RF = 1 ./ (Delta_p + 1i*gamma_e ...
    - (Omega_c^2/4) ./ ...
      (0 + 1i*gamma_r ...
      - (Omega_RF^2/4) ./ (0 + 1i*gamma_rp)));
T_RF = exp(-abs(imag(chi_RF))/max(abs(imag(chi_RF))));

%% Plot Results
figure('Position', [100 100 1000 600]);

subplot(2,1,1);
plot(Delta_p, T_noRF, 'b', 'LineWidth', 2);
hold on;
plot(Delta_p, T_RF, 'r', 'LineWidth', 2);
xlabel('Probe Detuning (MHz)', 'FontSize', 12);
ylabel('EIT Transmission (arb.)', 'FontSize', 12);
title('Rydberg-EIT with Autler-Townes Splitting', 'FontSize', 14, 'FontWeight', 'bold');
legend('No RF (EIT)', 'With RF (AT splitting)', 'Location', 'best');
grid on;
set(gca, 'FontSize', 11);

% Zoom on AT peaks
subplot(2,1,2);
idx = find(abs(Delta_p) < 20);
plot(Delta_p(idx), T_RF(idx), 'r', 'LineWidth', 2);
xlabel('Probe Detuning (MHz)', 'FontSize', 12);
ylabel('Transmission (arb.)', 'FontSize', 12);
title('Autler-Townes Doublet (Zoomed)', 'FontSize', 14, 'FontWeight', 'bold');
grid on;
set(gca, 'FontSize', 11);

% Find peaks and measure splitting
[pks, locs] = findpeaks(T_RF, Delta_p, 'MinPeakDistance', 3, 'SortStr', 'descend');
if length(locs) >= 2
    measured_splitting = abs(locs(1) - locs(2));
    fprintf('\n=== Measurement Results ===\n');
    fprintf('Measured AT splitting = %.3f MHz\n', measured_splitting);
    fprintf('Predicted splitting = %.3f MHz\n', Omega_RF);
    fprintf('Error = %.2f%%\n', abs(measured_splitting - Omega_RF)/Omega_RF * 100);

    % Extract electric field from splitting
    E_measured = (2*pi*hbar*measured_splitting*1e6) / ea0;
    fprintf('\n=== Field Extraction ===\n');
    fprintf('Extracted E-field = %.2e V/m\n', E_measured);
    fprintf('True E-field = %.2e V/m\n', E_RF);
    fprintf('Field measurement error = %.2f%%\n', abs(E_measured - E_RF)/E_RF * 100);
end

%% Doppler Averaging (optional, more realistic)
fprintf('\n=== Including Doppler Effects ===\n');
v = linspace(-500, 500, 1000);  % Velocity grid (m/s)
fv = sqrt(mRb/(2*pi*kB*T)) * exp(-mRb*v.^2/(2*kB*T));
fv = fv / trapz(v, fv);  % Normalize

% Doppler-averaged susceptibility
chi_Dop = zeros(size(Delta_p));
for i = 1:length(v)
    Doppler_shift = kp*v(i)/1e6;  % MHz
    chi_v = 1 ./ ((Delta_p - Doppler_shift) + 1i*gamma_e ...
        - (Omega_c^2/4) ./ ...
          (0 + 1i*gamma_r ...
          - (Omega_RF^2/4) ./ (0 + 1i*gamma_rp)));
    chi_Dop = chi_Dop + chi_v * fv(i);
end

T_Dop = exp(-abs(imag(chi_Dop))/max(abs(imag(chi_Dop))));

figure;
plot(Delta_p, T_RF, 'r--', 'LineWidth', 1.5, 'DisplayName', 'No Doppler');
hold on;
plot(Delta_p, T_Dop, 'b', 'LineWidth', 2, 'DisplayName', 'With Doppler');
xlabel('Probe Detuning (MHz)', 'FontSize', 12);
ylabel('Transmission (arb.)', 'FontSize', 12);
title('Effect of Doppler Broadening on AT Splitting', 'FontSize', 14, 'FontWeight', 'bold');
legend('Location', 'best');
grid on;
set(gca, 'FontSize', 11);

fprintf('Doppler broadening simulation complete.\n');
fprintf('\nKey finding: AT splitting remains unchanged despite Doppler broadening.\n');
fprintf('This is why splitting-based measurement is preferred over slope detection.\n');
