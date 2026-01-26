% Epitrochoidal Motion in Penning Trap
% Models cyclotron and magnetron motion creating epitrochoid patterns
%
% Constants
q = 1.6e-19;         % Charge of particle (Coulombs)
m = 1.67e-27;        % Mass of particle (kg), e.g., a proton
B = 0.01;            % Magnetic field strength (Tesla)
V0 = 0.1;            % Voltage for electric field (Volts)
d = 0.01;            % Characteristic trap dimension (meters)
T = 1e-4;            % Total simulation time (seconds), reduced
dt = 5e-8;           % Larger time step to speed up simulation

% Cyclotron and magnetron frequencies
omega_c = q * B / m;  % Unmodified cyclotron frequency
omega_plus = omega_c / 2 + sqrt((omega_c / 2)^2 - q * V0 / (m * d^2));  % Modified cyclotron
omega_minus = omega_c / 2 - sqrt((omega_c / 2)^2 - q * V0 / (m * d^2)); % Magnetron

% Check the frequency ratio
freq_ratio = omega_plus / abs(omega_minus);
disp(['Frequency Ratio ω+/ω- = ', num2str(freq_ratio)]);

% Initial conditions
r = [0.01; 0; 0];      % Initial position in 3D space (x, y, z)
v = [0; 100; 0];       % Initial velocity in 3D space

% Preallocate arrays for storing positions over time
num_steps = round(T / dt);
positions = zeros(2, num_steps);

% Simulation loop
for i = 1:num_steps
    % Calculate forces
    F_electric = q * [-r(1); -r(2); 2 * r(3)] * V0 / d^2;   % Quadrupole electric field
    F_magnetic = q * cross(v, [0; 0; B]);                   % Magnetic force in 3D
    F_total = F_electric + F_magnetic;                      % Total force

    % Update velocity and position
    a = F_total / m;                 % Acceleration
    v = v + a * dt;                  % Update velocity in 3D
    r = r + v * dt;                  % Update position in 3D

    % Store the position for 2D plotting in the radial plane
    positions(:, i) = r(1:2);
end

% Plot the 2D trajectory in the radial plane
plot(positions(1, :), positions(2, :), 'b');
xlabel('x (m)');
ylabel('y (m)');
title(['Radial Motion in Penning Trap (ω+/ω- = ', num2str(freq_ratio), ')']);
axis equal;
grid on;
