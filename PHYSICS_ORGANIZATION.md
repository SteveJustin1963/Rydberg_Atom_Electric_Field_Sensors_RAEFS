# Physics-Based Organization

The simulation files have been organized by physics domain:

## Directories by Physics Domain

### `eit_spectroscopy/`
**Electromagnetically Induced Transparency & Autler-Townes Splitting**
- `eit_autler_townes_model.m` - Core EIT physics with RF-induced splitting for field sensing

### `polaron_physics/`
**Holstein Model & Electron-Phonon Interactions**
- `holstein_model.m` - MATLAB implementation of Holstein Hamiltonian
- `holstein_numerical.py` - Numerical diagonalization and verification

### `ion_trap_dynamics/`
**Charged Particle Motion in Electromagnetic Fields**
- `penning_trap_3d.m` - Full 3D particle trajectory simulation
- `penning_trap_epitrochoid.m` - Cyclotron/magnetron motion patterns

### `field_estimation/`
**Statistical Signal Processing & Field Measurement**
- `mle_bayesian_field_estimator.py` - Maximum likelihood estimation with Bayesian inference

## Physics Relationships

1. **EIT Spectroscopy** → Core Rydberg sensor mechanism
2. **Polaron Physics** → Many-body effects in Rydberg atoms
3. **Ion Trap Dynamics** → Complementary charged particle physics
4. **Field Estimation** → Signal processing for sensor output

Each domain represents a different aspect of the quantum sensing physics stack.