% 3D Penning Trap Simulation
% Simulates charged particle motion in combined magnetic and electric fields
%
% Constants
q = 1.6e-19;        % Charge of particle (Coulombs)
m = 1.67e-27;       % Mass of particle (kg), e.g., a proton
B = 1;              % Magnetic field strength (Tesla)
V0 = 10;            % Voltage for electric field (Volts)
d = 0.01;           % Characteristic trap dimension (meters)
T = 2e-6;           % Total simulation time (seconds)
dt = 1e-9;          % Time step (seconds)

% Initial conditions
r = [0.01; 0; 0.01]; % Initial position (x, y, z)
v = [100; 0; 50];    % Initial velocity (vx, vy, vz)

% Preallocate arrays for position tracking
num_steps = round(T / dt);
positions = zeros(3, num_steps);

% Magnetic and electric field setup
B_vec = [0; 0; B];           % Magnetic field in z-direction
E = @(r) -V0 * [r(1); r(2); -2*r(3)] / d^2; % Quadrupole electric field

% Simulation loop
for i = 1:num_steps
    % Calculate forces
    F_electric = q * E(r);             % Electric force (z confinement)
    F_magnetic = q * cross(v, B_vec);  % Magnetic force (xy-plane rotation)
    F_total = F_electric + F_magnetic; % Total force

    % Update velocity and position using Newton's second law
    a = F_total / m;                   % Acceleration
    v = v + a * dt;                    % Update velocity
    r = r + v * dt;                    % Update position

    % Store the position for plotting
    positions(:, i) = r;
end

% Plot the particle's trajectory in 3D
plot3(positions(1, :), positions(2, :), positions(3, :));
xlabel('x (m)');
ylabel('y (m)');
zlabel('z (m)');
title('3D Trajectory of Particle in Penning Trap');
grid on;
