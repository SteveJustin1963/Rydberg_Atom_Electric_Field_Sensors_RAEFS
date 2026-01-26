% Holstein Hamiltonian Analysis in Octave
% Demonstrates polaron energy shift and phonon occupation probabilities
%
clear; clc; close all;

% Parameters
epsilon = 1.0;  % Electronic energy
omega = 1.0;    % Phonon energy
lambda_vals = linspace(0, 2, 100); % Electron-phonon coupling strengths

% Compute energy shift due to polaron formation
energy_shift = epsilon - (lambda_vals .^ 2) ./ omega;

% Plot the energy shift as a function of lambda
figure;
plot(lambda_vals, energy_shift, 'b-', 'LineWidth', 2);
xlabel('\lambda (Electron-Phonon Coupling)');
ylabel('Energy Shift \tilde{\epsilon}');
title('Polaron Energy Shift due to Electron-Phonon Interaction');
grid on;

% Compute phonon occupation probabilities for different lambda
N_phonons = 10; % Truncate phonon basis
lambda_test = [0.5, 1.0, 1.5]; % Specific lambda values to test
colors = {'r', 'g', 'b'};

figure;
hold on;
for i = 1:length(lambda_test)
    lambda = lambda_test(i);
    g = lambda / omega;
    phonon_probs = exp(-g^2) .* (g.^(2 * (0:N_phonons))) ./ factorial(0:N_phonons);
    phonon_probs = phonon_probs / sum(phonon_probs); % Normalize

    % Plot phonon probability distribution
    stem(0:N_phonons, phonon_probs, colors{i}, 'LineWidth', 2, 'MarkerSize', 8);
end
xlabel('Phonon Number n');
ylabel('Probability P(n)');
title('Phonon Occupation Probabilities for Different \lambda');
legend(arrayfun(@(x) sprintf('\\lambda = %.1f', x), lambda_test, 'UniformOutput', false));
grid on;
hold off;

disp('Simulation complete: Energy shift plotted and phonon occupation distributions analyzed.');
