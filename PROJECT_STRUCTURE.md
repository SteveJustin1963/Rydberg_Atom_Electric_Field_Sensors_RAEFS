# Project Structure

This document describes the organization of the Rydberg Atom Electric Field Sensors (RAEFS) project.

## Directory Structure

```
Rydberg_Atom_Electric_Field_Sensors_RAEFS/
├── README.md                    # Main project overview
├── QUICK_START.md              # Quick start guide
├── PROJECT_STRUCTURE.md        # This file
├── docs/                       # Documentation
│   ├── README_Project_Organization.md
│   ├── Rydberg_Atom_Electric_Field_Sensors_Complete_Reference.md
│   └── transcript.md           # Technical discussion transcript
├── simulation/                 # Simulation code (organized by physics)
│   ├── eit_spectroscopy/      # EIT & Autler-Townes splitting
│   │   └── eit_autler_townes_model.m
│   ├── polaron_physics/       # Holstein model & electron-phonon interactions
│   │   ├── holstein_model.m
│   │   └── holstein_numerical.py
│   ├── ion_trap_dynamics/     # Charged particle motion
│   │   ├── penning_trap_3d.m
│   │   └── penning_trap_epitrochoid.m
│   └── field_estimation/      # Statistical field measurement
│       └── mle_bayesian_field_estimator.py
├── literature/                # Research papers and references
│   ├── 3208.pdf
│   ├── Electromagnetically_induced_transparency_with_Rydberg_atoms.pdf
│   ├── Rydberg_Atom_Electric_Field_Sensors_for_Communications_and_Sensing.pdf
│   └── photonics-10-01367.pdf
└── examples/                  # Example implementations and tutorials
```

## File Descriptions

### Root Level
- **README.md**: Main project documentation with theory and implementation details
- **QUICK_START.md**: Quick start guide for getting up and running
- **PROJECT_STRUCTURE.md**: This organization document

### Documentation (`docs/`)
- **README_Project_Organization.md**: Project organization guidelines
- **Rydberg_Atom_Electric_Field_Sensors_Complete_Reference.md**: Complete technical reference
- **transcript.md**: Detailed technical discussion about practical implementation

### Simulation Code (`simulation/`)
Organized by physics domain rather than programming language.

#### EIT Spectroscopy (`simulation/eit_spectroscopy/`)
- **eit_autler_townes_model.m**: EIT and Autler-Townes splitting simulation

#### Polaron Physics (`simulation/polaron_physics/`)
- **holstein_model.m**: Holstein model implementation (MATLAB)
- **holstein_numerical.py**: Numerical Holstein model implementation (Python)

#### Ion Trap Dynamics (`simulation/ion_trap_dynamics/`)
- **penning_trap_3d.m**: 3D Penning trap simulation
- **penning_trap_epitrochoid.m**: Epitrochoid trajectory simulation

#### Field Estimation (`simulation/field_estimation/`)
- **mle_bayesian_field_estimator.py**: Maximum likelihood estimation for field detection

### Literature (`literature/`)
- Research papers and academic references related to Rydberg atom physics
- EIT theory and applications
- Quantum sensing methodologies

### Examples (`examples/`)
- Future location for example implementations
- Tutorials and getting started code
- Experimental configurations