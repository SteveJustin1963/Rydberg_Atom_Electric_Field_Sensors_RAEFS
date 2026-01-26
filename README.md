# RAEFS - Rydberg Atom Electric Field Sensors

**Exploring Rydberg Atom Electric Field Sensors for Communications and Sensing**

---

## Table of Contents

- [Project Status](#project-status)
- [Getting Started](#getting-started)
  - [Software Requirements](#software-requirements)
  - [Installation](#installation)
  - [Running the Simulations](#running-the-simulations)
- [Overview](#overview)
- [Alternative Systems for Bound State Simulation](#alternative-systems-for-bound-state-simulation)
- [Penning Trap Simulations](#penning-trap-simulations)
  - [3D Penning Trap](#3d-penning-trap)
  - [Epitrochoidal Motion](#epitrochoidal-motion)
- [Physical Laboratory Experiments](#physical-laboratory-experiments)
  - [Building a Functional Rydberg Atom Electric Field Sensor](#building-a-functional-rydberg-atom-electric-field-sensor)
- [Low-Cost Alternatives for RF Detection](#low-cost-alternatives-for-rf-detection)
- [RF Difference Detection and Antenna Array Experiments](#rf-difference-detection-and-antenna-array-experiments)
- [Using Three Loop Antennas for RF Difference Detection Experiments](#using-three-loop-antennas-for-rf-difference-detection-experiments)
- [Hybrid Rydberg-Loop Antenna Array Systems](#hybrid-rydberg-loop-antenna-array-systems)
- [Phonon Science Applications](#phonon-science-applications)
- [Holstein Hamiltonian Model](#holstein-hamiltonian-model)
  - [Appendix 1: Mathematical Treatment](#appendix-1-mathematical-treatment)
  - [Numerical Diagonalization](#numerical-diagonalization)
- [Communications and Sensing Applications](#communications-and-sensing-applications)
- [Validation and Results](#validation-and-results)
- [Roadmap and Next Steps](#roadmap-and-next-steps)
- [References](#references)
- [Additional Resources](#additional-resources)
- [Contributing](#contributing)
- [License](#license)

---

## Project Status

**Current Phase:** Theoretical exploration and computational simulation (Early Research)

This repository is actively exploring ways to use Rydberg Atom Electric Field Sensors (RAEFS) for communications and sensing applications. Currently, we are in the **theoretical and simulation phase** - there is no physical Rydberg atom implementation yet. The focus is on:

1. Understanding the fundamental physics through computational models
2. Exploring alternative bound-state systems that can mimic Rydberg-like behavior
3. Developing simulation frameworks for future experimental work
4. Investigating connections to phonon science and quantum communication

**What this repo contains:**
- Computational simulations of Penning traps (alternative confinement systems)
- Holstein Hamiltonian models for electron-phonon coupling
- Theoretical frameworks for future RAEFS applications
- Cost estimates and requirements for building actual hardware

**What this repo does NOT contain (yet):**
- Working Rydberg atom vapor cell experiments
- Physical laser setups or optics
- Demonstrated communication protocols
- Hardware designs or circuit schematics

We welcome contributions and collaborations to advance from simulation to experimental implementation!

---

## Getting Started

### Software Requirements

To run the simulations in this repository, you need:

**For Octave/MATLAB Simulations:**
- **GNU Octave** (free, open-source) version 6.0 or higher, OR
- **MATLAB** R2018a or higher
- No additional toolboxes required for basic simulations

**For Python Simulations:**
- **Python** 3.7 or higher
- **NumPy** (`pip install numpy`)
- **SciPy** (`pip install scipy`)
- **Matplotlib** (optional, for visualization: `pip install matplotlib`)

### Installation

#### Installing GNU Octave (Recommended for beginners)

**Linux (Debian/Ubuntu):**
```bash
sudo apt-get update
sudo apt-get install octave
```

**macOS (with Homebrew):**
```bash
brew install octave
```

**Windows:**
Download the installer from [https://www.gnu.org/software/octave/](https://www.gnu.org/software/octave/)

#### Installing Python Dependencies

```bash
# Create a virtual environment (recommended)
python -m venv raefs-env
source raefs-env/bin/activate  # On Windows: raefs-env\Scripts\activate

# Install required packages
pip install numpy scipy matplotlib
```

### Running the Simulations

#### Octave/MATLAB Simulations

**1. 3D Penning Trap Simulation:**
```bash
octave penning_trap_3d.m
```
Expected runtime: ~5-30 seconds (depending on system)
Output: 3D trajectory plot showing helical particle motion

**2. Epitrochoidal Motion Simulation:**
```bash
octave penning_trap_epitrochoid.m
```
Expected runtime: ~10-60 seconds
Output: 2D radial plane plot showing flower-like epitrochoid patterns + frequency ratio

**3. Holstein Hamiltonian Analysis:**
```bash
octave holstein_model.m
```
Expected runtime: ~2-10 seconds
Output: Two figures - (1) Polaron energy shift vs. coupling, (2) Phonon occupation probabilities

#### Python Simulation

**Holstein Numerical Diagonalization:**
```bash
python holstein_numerical.py
```
Expected runtime: ~1-5 seconds
Output: Console output showing energy verification and probability differences

To enable plotting (uncomment the matplotlib section in `holstein_numerical.py`), the script will save `holstein_verification.png`.

---

## Overview

This project explores the use of **Rydberg atoms** - highly excited atoms with exaggerated properties - as electric field sensors for communications and sensing applications. Rydberg atoms are extraordinarily sensitive to electromagnetic fields, making them ideal candidates for:

- **Ultra-sensitive E-field detection** (sensitivity down to μV/cm)
- **Quantum communication** (via electromagnetically induced transparency)
- **RF spectrum sensing** (MHz to THz frequencies)
- **Fundamental physics research** (quantum optics, many-body physics)

Since building actual Rydberg atom systems requires expensive laboratory equipment ($200k-$500k+), this repository focuses on **computational models** and **alternative systems** that can simulate bound-state behavior without requiring atomic physics infrastructure.

**Research Strategy:**
The approach bridges multiple domains - Penning traps (electromagnetic confinement), phonon science (lattice vibrations), and quantum simulation - to develop a comprehensive theoretical framework before attempting physical implementation.

For comprehensive background on Rydberg atom E-field sensors, see the included document:
**[Rydberg_Atom_Electric_Field_Sensors_for_Communications_and_Sensing.pdf](Rydberg_Atom_Electric_Field_Sensors_for_Communications_and_Sensing.pdf)**

This document provides detailed information on:
- Fundamental principles of Rydberg atom physics
- Current state-of-the-art experimental techniques
- Applications in communications and sensing
- Technical specifications and performance metrics

---

## Alternative Systems for Bound State Simulation

It's possible to simulate alternative systems using "bound" states by confining particles or waves within specific potentials. Although they differ from true atomic bound states, they capture the essence of confined energy levels and spatial limitations. Each approach offers flexibility, enabling bound state simulations without the need for an atomic nucleus. Let's try and make computational models. While in atoms, the bound state is a result of the Coulomb force between an electron and the nucleus, in non-atomic systems, other forces and interactions can mimic this binding effect.

Here are a few ways to simulate or approximate bound states without an actual atom:

### 1. **Electromagnetic Trapping (Penning and Paul Traps)**
   - **Penning Traps**: These devices use a combination of magnetic and electric fields to trap charged particles, effectively binding them to a fixed position or orbit. Although not a true Rydberg bound state, the particles remain constrained in a defined region and can exhibit orbit-like motion.
   - **Paul Traps**: This technique uses oscillating electric fields to trap ions in a pseudo-potential, allowing them to remain in specific locations. Bound states here can simulate atomic orbits but use electromagnetic fields instead of a nuclear force.

### 2. **Quantum Dots as Artificial Atoms**
   - Quantum dots, sometimes called "artificial atoms," can confine electrons within a small space, creating a quantized energy spectrum that resembles the electron states in atoms.
   - By adjusting the size, shape, and materials of the quantum dot, one can design energy levels that resemble Rydberg-like high-energy states. Electrons within a quantum dot are bound by the confining potential of the dot rather than by a nucleus, creating a form of bound state that's tunable and customizable.

### 3. **Cold Atom Traps and Optical Lattices**
   - **Optical Lattices**: By interfering multiple laser beams, researchers can create a standing wave pattern that traps atoms or particles in periodic potential wells, binding them to specific locations.
   - **Cold Atom Simulations**: In ultracold conditions, neutral atoms can be manipulated to mimic bound states within an external potential, sometimes using artificial magnetic fields. These conditions can simulate interactions and "binding" without an atomic core, and even reproduce behaviors analogous to electron orbits.

### 4. **Simulating Bound States in Computation (Quantum and Classical Simulations)**
   - Using **quantum mechanics simulations** (e.g., Schrödinger or Dirac equations in a potential well), one can computationally simulate a bound state by creating an attractive potential, like a harmonic oscillator or Coulomb-like potential, and calculating the resulting wavefunctions.
   - This approach doesn't rely on actual particles but rather on solving the equations for hypothetical particles in a potential, which produces energy levels and states similar to atomic orbitals.

### 5. **Metamaterials and Bound State Simulation**
   - Certain **metamaterials** (engineered materials with properties not found in nature) can simulate bound states by designing regions where electromagnetic waves are confined in a pattern.
   - For example, by creating photonic crystals or plasmonic resonators, it's possible to trap electromagnetic fields in a manner that mimics bound states. These setups can emulate the spatial confinement seen in atomic orbitals without needing an actual atom.

### 6. **Artificial Atoms in Superconducting Circuits**
   - In superconducting qubits, energy levels are created by the design of Josephson junctions, allowing for discrete energy states similar to atomic bound states.
   - In such circuits, a particle-like behavior is mimicked by confining the wavefunction within the circuit. While there is no central nucleus, the energy levels are quantized, resembling those found in real atoms.

---

## Penning Trap Simulations

### 3D Penning Trap

Wiki: `Penning traps use a strong homogeneous axial magnetic field to confine particles radially and a quadrupole electric field to confine the particles axially. The static electric potential can be generated using a set of three electrodes: a ring and two endcaps.`

![image](https://github.com/user-attachments/assets/681b8cbd-bcda-404c-a92c-7491f2665ba6)

So using a **3D Penning trap** without ignoring the \( z \)-axis, you need both the **magnetic field** (to induce circular motion) and a **quadrupole electric field** (to confine the particle along the \( z \)-axis). This combination creates a stable 3D confinement that prevents the particle from spiraling outward.

In a Penning trap, the quadrupole electric field restricts motion along the \( z \)-axis, while the magnetic field in the \( z \)-direction forces circular motion in the \( xy \)-plane. Together, these fields create a 3D trapping potential.

Simulate a 3D Penning trap with Octave - see **[penning_trap_3d.m](penning_trap_3d.m)**

![image](https://github.com/user-attachments/assets/679e28a9-f69c-4476-a6b5-0a8083e3205f)

#### Explanation

1. **Quadrupole Electric Field**:
   - The function `E(r)` defines the electric field for 3D confinement, where the field confines the particle along the \( z \)-axis and slightly repels in the \( x \) and \( y \) directions. This field creates a restoring force towards the trap center along \( z \), balancing out the magnetic field's tendency to make the particle spiral.

2. **Magnetic Field in \( z \)-Direction**:
   - The `B_vec` vector defines a constant magnetic field along the \( z \)-axis, inducing circular motion in the \( xy \)-plane. The magnetic force is calculated using the cross product of the velocity `v` and `B_vec`.

3. **3D Confinement**:
   - Both fields work together to keep the particle in a stable, bounded region within the trap, resulting in a helical motion confined within a defined 3D space.

4. **3D Plot**:
   - The plot displays the particle's trajectory, showing helical or oscillatory motion that remains contained within the 3D space due to the combined fields.

This simulation should demonstrate a stable 3D confinement, with the particle oscillating in the \( z \)-direction while moving in a circular or helical pattern in the \( xy \)-plane, characteristic of a Penning trap.

### Epitrochoidal Motion

![image](https://github.com/user-attachments/assets/1b94f45c-2839-4198-b2f3-37dc77939db1)

The electric field causes ions to oscillate (harmonically in the case of an ideal Penning trap) along the trap axis. The magnetic field in combination with the electric field causes charged particles to move in the radial plane with a motion which traces out an epitrochoid.

Making a simulation models a Penning trap's confinement of a charged particle by combining magnetic and electric fields. The result is a distinctive pattern of motion that is useful for precision measurements in physics, where the trapped particle's properties can be studied without it escaping. The simulation illustrates how carefully controlled fields can stabilize and control particle motion in three dimensions.

#### Key Concepts of the Penning Trap

This code simulates the motion of a charged particle (like a proton)

1. **Magnetic Field Confinement**:
   - A strong magnetic field is applied along the \( z \)-axis (the vertical axis), which forces the particle to move in circular or spiral paths in the horizontal (radial) \( xy \)-plane. This is due to the Lorentz force, which acts perpendicular to the particle's velocity and the magnetic field, causing it to circle around the field lines.

2. **Electric Field Confinement**:
   - A quadrupole electric field is created by applying voltage to electrodes arranged in a specific shape (usually hyperbolic). This field confines the particle along the \( z \)-axis by creating a "saddle point" in the potential, where the particle is pushed back toward the center if it tries to drift along the \( z \)-axis.
   - The electric field stabilizes the motion along the axial direction, balancing the effect of the magnetic field and preventing the particle from spiraling out of control.

3. **Combined Effect: Cyclotron and Magnetron Motion**:
   - The particle's motion in a Penning trap is a combination of two main components:
     - **Modified Cyclotron Motion** (\( \omega_+ \)): This is a high-frequency circular motion in the radial plane induced by the magnetic field.
     - **Magnetron Motion** (\( \omega_- \)): This is a slower, large-radius motion in the opposite direction that results from the combined electric and magnetic fields.
   - Together, these two types of motion cause the particle to trace out a complex path called an **epitrochoid** in the radial plane (a flower-like or looping pattern).

4. **Frequency Ratio**:
   - The relationship between the modified cyclotron frequency and the magnetron frequency is crucial. The code aims for a specific frequency ratio (like 8:1) to create the characteristic looping pattern seen in epitrochoidal motion. This ratio is adjusted by tweaking the magnetic field strength and the electric field voltage.

5. **Simulation Process**:
   - The code simulates the particle's movement step-by-step over time. In each step, it calculates the forces acting on the particle due to the electric and magnetic fields, updates the particle's velocity and position, and then records the new position.
   - The result is a trajectory showing the particle's movement in 3D space, with a 2D plot focusing on its looping pattern in the radial plane.

6. **Expected Motion**:
   - With the right balance of electric and magnetic forces, the particle remains trapped in a stable, confined orbit. The radial pattern forms loops or flower-like shapes, characteristic of particles in a Penning trap under epitrochoidal motion.

See **[penning_trap_epitrochoid.m](penning_trap_epitrochoid.m)** for the complete simulation code.

![image](https://github.com/user-attachments/assets/1b4b41b5-079a-4cf4-96bc-730716aeefd3)

---

## Physical Laboratory Experiments

### To Run the "Experiments" in the Repo

- **Required "gear"**: Just software — Octave (free) or MATLAB to run the provided simulation code.
- **No physical lab equipment** is needed or mentioned (no optics, lasers, vapor cells, photodetectors, RF sources, electrodes, etc.).
- **Voltages/frequencies mentioned**: These are purely simulation parameters, not real-world applied voltages:
  - Quadrupole electric potential: V₀ = 10 V
  - Magnetic field: B = 1 Tesla (along z-axis)
  - Other params: Particle charge q = 1.6e-19 C, mass m = 1.67e-27 kg (proton-like), trap size d = 0.01 m, cyclotron frequency ω_c = qB/m, etc.
- No power supplies, DC/AC/RF voltages, or hardware are specified because it's computational.

### Repository Files

The repo contains:
- **README.md** - This documentation
- **penning_trap_3d.m** - 3D Penning trap simulation
- **penning_trap_epitrochoid.m** - Epitrochoidal motion simulation
- **holstein_model.m** - Holstein Hamiltonian analysis
- **holstein_numerical.py** - Numerical diagonalization of Holstein model
- **Rydberg_Atom_Electric_Field_Sensors_for_Communications_and_Sensing.pdf** - Comprehensive background document

For detailed background information, physical setups, figures, schematics, and theoretical foundations, please refer to the PDF document included in this repository.

### Typical Real Rydberg Atom E-Field Sensor Experiments

If you're asking about building/running actual Rydberg atom-based electric field sensors (common in research labs, e.g., with rubidium/cesium atoms), those are advanced atomic physics setups and **not** what's in this repo currently. Typical requirements include:

- **Lasers** → Two tunable diode lasers (e.g., ~780 nm probe + ~480 nm coupling for Rb Rydberg states), mW-level power, frequency-stabilized.
- **Vapor cell** → Glass cell with Rb/Cs atoms (often heated to ~40-100°C).
- **Optics** → Lenses, beamsplitters, mirrors, optical table, anti-vibration.
- **Detection** → Fast photodiode + transimpedance amplifier, possibly lock-in amplifier.
- **Field application/calibration** → Electrodes or antennas; calibration fields often use DC/AC voltages from 0-100 V (or higher) across plates to generate known E-fields (mV/cm to V/cm range).
- **RF/electronics** → Signal generator for test fields (MHz-GHz), low-noise power supplies, data acquisition (oscilloscope, spectrum analyzer).
- **Safety/environment** → Laser safety gear, vacuum (sometimes), magnetic shielding.

These setups are expensive/complex (university or national lab level) and sensitive to noise/vibrations. If that's what you meant, clarify or point to a specific reference/paper — this repo doesn't provide build details for that (yet).

### Building a functional **Rydberg atom electric field sensor**

(using electromagnetically induced transparency/Autler-Townes splitting in a room-temperature vapor cell) in a university lab is a major advanced atomic physics project. It typically costs **$200,000–$500,000+** for a basic setup (dominated by lasers), requires expertise in laser stabilization, optics alignment, and vacuum/electronics, and takes months to years to commission. No simple "open-source" full hardware blueprint exists, but many labs follow similar designs inspired by NIST, Princeton, or commercial precursors.

#### Core Principle

Two counter-propagating lasers excite alkali atoms (usually ⁸⁷Rb) in a vapor cell to a Rydberg state via a ladder scheme:
- Probe: ~780 nm (5S → 5P)
- Coupling: ~480 nm (5P → Rydberg nS/nD)

An applied RF/DC E-field shifts/splits the EIT signal, read out optically on a photodiode.

#### Essential Hardware List with Examples and Likely Costs

Costs are approximate (2025 USD, new from vendors like Toptica, Thorlabs, Vescent; university discounts ~20-30% off). Used/refurbished equipment can cut 30-50%.

##### 1. Lasers (biggest expense)
- **780 nm probe laser** (tunable ECDL, narrow linewidth <1 MHz, ~50-100 mW):
  - Example: Toptica DL pro or TA pro (~75-105 mW versions).
  - Cost: $30,000–$60,000 (including frequency stabilization electronics).
- **480 nm coupling laser** (higher power needed, often frequency-doubled from ~960 nm):
  - Example: Toptica TA-SHG pro or DLC Rydberg Rb II (~500-1000 mW).
  - Cost: $50,000–$100,000+ (doubling cavity + IR laser + amplifier).
- **Frequency stabilization** (locks to atomic transitions; often saturated absorption or transfer cavity):
  - Example: Toptica DLC pro locks or wavemeter.
  - Cost: $20,000–$40,000.

##### 2. Vapor Cell and Housing
- **Rubidium vapor cell** (glass, ~75 mm long, often with stem for Rb reservoir):
  - Example: Thorlabs GC19075-RB (natural Rb) or GC19075-RB87 (pure ⁸⁷Rb), quartz for better UV/IR transmission.
  - Cost: $1,000–$3,000.
- **Cell heater/mount** (temperature control ~40-100°C for vapor density):
  - Example: Thorlabs GCH25-75 heater + TC300 controller.
  - Cost: $1,500–$3,000.

##### 3. Optics and Beam Delivery
- Optical table (vibration-isolated) + breadboards/posts/mirrors/lenses/beamsplitters/PBS/AOMs (for frequency shifting/locking).
  - Cost: $20,000–$50,000 (full setup; Thorlabs/Newport).
- Optical isolators, fibers (optional for portable probe), waveplates.
  - Cost: $10,000–$20,000.

##### 4. Detection and Electronics
- Fast photodiode (balanced for noise reduction) + transimpedance amplifier.
  - Example: Thorlabs or Newport high-speed PDs.
  - Cost: $2,000–$5,000.
- Oscilloscope/spectrum analyzer/lock-in amplifier (for signal readout).
  - Cost: $5,000–$20,000.
- RF source for calibration (signal generator + horn antenna).
  - Cost: $5,000–$15,000.

##### 5. Optional/Advanced
- Magnetic shielding (mu-metal) and coils (for zeroing B-fields).
  - Cost: $5,000–$10,000.
- Data acquisition (DAQ card + computer control).
  - Cost: $2,000–$5,000.

**Total likely cost for a minimal working university setup**: $200,000–$400,000 (lasers ~70%). Full professional-grade (e.g., with fiber-coupling, auto-locking): $500,000+.

#### Voltages and Power Supplies
- No high voltages for the atoms themselves (room-temperature vapor, no trap).
- DC calibration fields: Low-voltage power supplies (0-100 V) across electrodes near/inside cell for ~V/cm fields.
- RF test fields: Standard signal generator (mW-level into antenna).
- Lasers need stable current/temperature controllers (included with systems).

#### Recommendations for a University Lab
- Start with a 780 nm system for basic EIT/spectroscopy (~$100k), then add 480 nm.
- Collaborate or use shared facilities (many AMO groups have parts).
- Commercial options emerging (e.g., Rydberg Technologies probes, but not cheap/open).
- Papers from NIST (Holloway group) or reviews provide schematics—replicate those.

This is not plug-and-play; alignment and stabilization are tricky. If your lab has cold atom experience, it's feasible; otherwise, consider simulations or partnering. Clarify if you want references to specific build papers!

---

## Low-Cost Alternatives for RF Detection

While full Rydberg atom systems require $200k-$500k investments, several low-cost approaches can achieve useful RF/E-field sensing using atomic systems. These alternatives sacrifice some sensitivity but provide practical entry points for research, education, and specific applications.

### 1. Ground-State Hyperfine Transitions (Recommended: $5k-$10k)

**Concept:**
Instead of expensive Rydberg states requiring two lasers, use **microwave transitions between ground-state hyperfine levels** in alkali atoms. For Rb-87, the ground state splits into F=1 and F=2 levels separated by 6.834682610904 GHz. While this is far from 7 MHz CW, we can detect low-frequency RF (like 7 MHz amateur radio signals) by mixing them with a local oscillator to create difference frequencies that modulate the atomic absorption, or by detecting the AC Stark shift and light shift effects on the optical transition.

#### Detailed Parts List

| Item | Part Number/Description | Supplier | Approx. Cost |
|------|------------------------|----------|--------------|
| **Rb-87 Vapor Cell** | GC19075-RB87 (75mm, enriched) | Thorlabs | $2,000 |
| **780 nm ECDL Laser** | DL100 or TA100 (used) | eBay/Toptica | $3,000-5,000 |
| **Photodiode** | DET36A/M (Si, 350-1100nm) | Thorlabs | $495 |
| **Cell Heater** | GCH25-75 (25-75mm adjustable) | Thorlabs | $1,020 |
| **Temperature Controller** | TC300 (0.001°C stability) | Thorlabs | $1,495 |
| **Optical Isolator** | IO-3D-780-VLP (prevents feedback) | Thorlabs | $850 |
| **Beam Splitter** | BS013 (50:50, 700-1100nm) | Thorlabs | $120 |
| **Mirrors (2×)** | BB1-E02 (1" broadband) | Thorlabs | $70 each |
| **Lens (collimating)** | AC254-030-B (f=30mm) | Thorlabs | $55 |
| **Lens (focusing)** | AC254-050-B (f=50mm) | Thorlabs | $55 |
| **Post holders/mounts** | Various (buy used lot) | eBay/Thorlabs | $300-500 |
| **Oscilloscope** | TDS2024B (200 MHz, 4-ch) or similar | eBay (used) | $400-800 |
| **Lock-in Amplifier** | SR830 (used) or DIY Arduino | eBay/DIY | $1,500 / $50 |
| **Function Generator** | 33220A or similar (20 MHz) | eBay (used) | $300-600 |
| **HF Radio Receiver** | RTL-SDR + upconverter OR old ham radio | Amazon/eBay | $50-200 |
| **7 MHz Antenna** | 40m dipole or loop (DIY wire) | DIY | $20 |
| **Breadboard/Table** | 12"×18" aluminum breadboard | Thorlabs/eBay | $150-300 |

**Total: $8,000-$12,000** (can reduce to ~$6k with DIY heater, used optics, skip lock-in initially)

#### Step-by-Step Build Instructions

**Phase 1: Optical Setup (Week 1-2)**

1. **Mount vapor cell in heater**
   - Install Rb cell into GCH25-75 heater assembly
   - Connect TC300 temperature controller
   - Set temperature to 55°C (provides ~10¹⁰ atoms/cm³ density)
   - Wait 30-60 minutes for thermal equilibrium
   - Monitor temperature stability: should hold ±0.01°C

2. **Laser alignment (coarse)**
   - Mount ECDL on breadboard with ~12" clearance to cell
   - Set laser current to mid-range (typically 60-80 mA for DL100)
   - Set temperature controller to manufacturer spec (usually 20-25°C)
   - Verify output power: should see 10-50 mW (measure with power meter or photodiode)
   - Collimate beam: adjust output collimation lens for minimal divergence at 1-2 meters

3. **Build optical path**
   ```
   LASER → ISOLATOR → BEAM SPLITTER → CELL → LENS → PHOTODIODE
                            ↓
                      SATURATION SPECTROSCOPY REFERENCE
   ```
   - Install optical isolator immediately after laser (critical: prevents feedback)
   - Use 50:50 beam splitter to send ~50% through cell, 50% to reference
   - Focus beam through cell with f=30mm lens (~1-2mm beam diameter)
   - Collimate after cell and focus onto photodiode with f=50mm lens
   - Keep beam height consistent (typically 2-4" above table)

4. **Tune laser to Rb D2 line (780.24 nm)**
   - Connect photodiode output to oscilloscope (DC coupling, 1 MΩ)
   - Slowly scan laser wavelength by adjusting piezo voltage (0-100V ramp, ~1 Hz)
   - Look for **absorption dips** on oscilloscope (transmission decreases)
   - You should see multiple dips corresponding to different Rb transitions:
     - F=2→F'=1,2,3 and F=1→F'=1,2 (5 transitions total, some overlap)
   - Identify the F=2→F'=3 transition (rightmost dip, strongest)
   - Fine-tune grating angle if needed (rotation changes wavelength coarsely)

**Phase 2: Saturated Absorption Spectroscopy Lock (Week 2-3)**

5. **Build reference beam path**
   - Split beam before cell: send weak probe beam through cell, retro-reflect strong "pump" beam
   - Pump beam (split from other BS output): expand to ~5mm, send backwards through cell
   - Probe and pump overlap in cell, creating saturated absorption signals
   - Detect probe beam on second photodiode after cell

6. **Observe saturated absorption peaks**
   - Scan laser frequency (piezo ramp)
   - Oscilloscope shows inverted peaks (Doppler-free resonances) on top of absorption dips
   - Crossover resonances appear between main transitions
   - Lock to F=2→F'=3 resonance (no crossover, clean signal)

7. **Implement frequency lock**
   - Use lock-in amplifier or DIY PID circuit
   - Modulate laser frequency at ~10-100 kHz (small sine wave on piezo)
   - Demodulate photodiode signal → error signal
   - Feed error signal back to piezo (slow) and laser current (fast)
   - Verify lock: laser stays on resonance for hours without drift

**Phase 3: RF Field Detection Setup (Week 3-4)**

8. **Build RF field applicator for 7 MHz CW detection**

   **Option A: Parallel Plate Electrodes (for strong E-field coupling)**
   ```
   Copper plates (10 cm × 10 cm) positioned 5 cm apart, straddling vapor cell

   7 MHz CW source → 50Ω coax → Plates

   E-field between plates = V/d = (Amplitude in Volts) / 0.05 m
   ```
   - Cut two copper/aluminum plates (PCB stock works)
   - Mount on insulating supports (acrylic, PTFE) at 5 cm spacing
   - Position vapor cell at center between plates
   - Connect 7 MHz signal source to plates via BNC cable
   - Use RF amplifier if needed (10-100W for strong field)

   **Option B: Loop Antenna (for B-field coupling → AC Stark shift)**
   ```
   40-meter band loop: circumference = λ/4 ≈ 10 meters (for resonance)
   Or small pickup loop: 10-20 turns, 20 cm diameter near cell
   ```
   - Wind 10-20 turns of magnet wire (22-26 AWG) in 20 cm coil
   - Place coil around vapor cell (axis along beam direction or perpendicular)
   - Connect to 7 MHz source via 50Ω coax
   - Tune for resonance with variable capacitor if using resonant loop

   **Option C: Direct Antenna Pickup (passive detection of ambient 7 MHz signals)**
   - String 40m dipole antenna outdoors: 2×10m wires, fed at center
   - Connect to capacitive plates near vapor cell
   - Amplify if needed with wideband RF preamp (e.g., Minicircuits ZX60-33LN-S+)

9. **7 MHz Signal Source Setup**
   - **Option 1 (Active test):** Function generator set to 7.000 MHz, 1-10 Vpp into plates
   - **Option 2 (Passive detection):** Tune HF receiver/RTL-SDR to 40m amateur band (7.000-7.300 MHz)
   - Listen for CW signals: Morse code transmissions sound like beeps
   - Use antenna to couple 7 MHz energy near vapor cell

10. **Detection Method: Amplitude Modulation of Optical Absorption**
    - The 7 MHz RF field won't directly drive hyperfine transitions (need 6.8 GHz for that)
    - Instead, detect via **AC Stark shift** of optical transition:
      - RF E-field oscillates electron wavefunction
      - This shifts energy levels slightly (quadratic in E-field)
      - Optical absorption at 780 nm changes at 7 MHz rate

    - **Measurement approach:**
      - Lock laser to Rb transition
      - Monitor photodiode signal on oscilloscope (AC coupling, 10 MHz bandwidth)
      - Apply 7 MHz CW to plates
      - Observe 7 MHz modulation on photodiode signal (amplitude modulation)
      - Use lock-in amplifier referenced to 7 MHz for better sensitivity

**Phase 4: Calibration and Testing (Week 4)**

11. **Calibrate E-field strength**
    - Known E-field between plates: E = V/d
    - Example: 10 Vpp into 5 cm gap → E = 10V / 0.05m = 200 V/m = 2 V/cm (peak)
    - Measure photodiode signal change: ΔI (in µA or mV)
    - Sensitivity: (ΔI/I) / E_field = responsivity in (%/V/cm)

12. **Test with real 7 MHz CW signals**
    - Connect 40m dipole antenna to parallel plates
    - Tune HF receiver to 7 MHz amateur band
    - Wait for CW transmission (Morse code beeps)
    - Observe corresponding pulses on oscilloscope synchronized with audio
    - Typical amateur signal: 100W transmitter, 50 km away → ~1-10 mV/cm at receiving antenna
    - Should see clear modulation on photodiode during CW transmissions

13. **Optimize sensitivity**
    - Increase laser power (more photons → better SNR)
    - Improve temperature stability (reduces drift)
    - Shield from ambient RF (Faraday cage around cell, filtered power)
    - Use balanced detection (two photodiodes, differential amplifier) to reject common-mode noise
    - Add lock-in amplifier tuned to 7 MHz (extracts signal from noise)

#### Expected Results

**Signal Characteristics:**
- **Baseline (no RF):** Steady DC voltage on photodiode (~1-5 V depending on laser power)
- **With 7 MHz CW (1 V/cm):**
  - AC modulation at 7 MHz, amplitude ~1-10 mV (0.1-1% of DC)
  - On oscilloscope: sine wave riding on DC level
  - Morse code visible as on/off keying of 7 MHz carrier

**Sensitivity Estimate:**
- Optical power: 10 mW through cell
- Shot noise limit: √(2eP/hν) ≈ 10 pA/√Hz for 10 mW
- AC Stark shift coefficient for Rb: ~10 kHz/(V/cm)² at 7 MHz
- With 1 Hz bandwidth (lock-in): detectable E-field ~1-10 mV/cm

**Troubleshooting:**
- **No absorption signal:** Laser wavelength wrong (check 780 nm), cell too cold, misalignment
- **Absorption too strong (saturated):** Laser power too high (add ND filter) or cell too hot
- **Can't lock laser:** Modulation depth wrong, feedback polarity inverted, too much noise
- **No 7 MHz signal:** RF amplifier needed, poor antenna coupling, faraday cage blocking signal
- **Noise/drift:** Improve shielding, stabilize temperature, check ground loops

#### Advanced: Heterodyne Detection for HF Band

To directly measure 7 MHz (instead of relying on AC Stark shift), mix with local oscillator:

```
7 MHz signal × 6.827 GHz LO = 6.827 GHz ± 7 MHz sidebands
```

The lower sideband (6.820 GHz) is close to Rb hyperfine splitting (6.835 GHz) - detectable with microwave horn antenna and mixer.

**Cost:** +$2k for microwave synthesizer and mixer
**Sensitivity:** Improved to ~100 µV/cm

#### Performance Summary

- **Sensitivity:** 1-10 mV/cm (direct AC Stark), 100 µV/cm (heterodyne)
- **7 MHz CW detection:** Yes, via amplitude modulation of optical absorption
- **Bandwidth:** DC - 10 MHz (limited by photodiode)
- **Dynamic range:** 60 dB (with lock-in amplifier)
- **Total Cost:** $7k-$10k

### 2. Coherent Population Trapping (CPT) - Very Low Cost

**Concept:**
Use a **single laser modulated at 6.8 GHz** (Rb hyperfine splitting) to create two sidebands that simultaneously drive F=1→F' and F=2→F' transitions. When both sidebands are resonant, atoms trap in a dark state (coherent superposition of F=1 and F=2). This creates a narrow transparency window. The 7 MHz CW signal modulates the CPT resonance via light shifts, causing intensity changes detectable on a photodiode.

#### Detailed Parts List

| Item | Part Number/Description | Supplier | Approx. Cost |
|------|------------------------|----------|--------------|
| **Rb-87 Vapor Cell (small)** | 25mm diameter, natural abundance OK | eBay/Surplus | $200-500 |
| **795 nm Laser Diode** | HL7851G or similar (50-100 mW) | Thorlabs/eBay | $150-300 |
| **Laser Mount/Driver** | LDM21 mount + LDC205C driver | Thorlabs | $500 total |
| **Electro-Optic Modulator** | EO-PM-NR-C1 (resonant, 6.8 GHz) | Thorlabs | $1,800 |
| **OR: Direct Current Modulation** | HMC566 6.8 GHz VCO chip + bias tee | Mini-Circuits | $50 (DIY) |
| **Photodiode** | FDS100 (fast Si detector) | Thorlabs | $145 |
| **Lens** | F220SMA-780 (collimating) | Thorlabs | $25 |
| **RF Amplifier** | ZHL-3A (0.4-3 GHz, 25 dBm) | Mini-Circuits | $75 (used) |
| **7 MHz Generator** | Arduino DDS (AD9850 module) | Amazon | $10 |
| **Oscilloscope** | 100 MHz, 2-channel (used) | eBay | $200-400 |
| **Small heater (DIY)** | Kapton tape heater + thermocouple | Omega/eBay | $50 |
| **Optics mount** | Basic cage system or DIY | Thorlabs/DIY | $100-200 |

**Total Cost:** $2,000-$3,500 (EOM version) OR $600-$1,200 (current modulation version)

#### Step-by-Step Build: Current Modulation Approach (Cheapest)

**Week 1: Basic Optical Setup**

1. **Assemble laser diode system**
   - Mount HL7851G laser diode in LDM21 mount (or DIY copper block with thermoelectric cooler)
   - Connect to LDC205C current/TEC driver
   - Set current to ~80 mA, temperature to 25°C
   - Output should be ~50 mW at 795 nm (Rb D1 line - easier to work with than D2)

2. **Collimate laser beam**
   - Install F220SMA-780 aspheric lens in SM1 tube mount
   - Adjust distance to laser diode until beam is collimated (~1-2mm diameter)
   - Check collimation: beam should not expand/contract over 1-2 meter distance

3. **Add 6.8 GHz modulation to laser current**
   - **DIY Circuit:**
     ```
     HMC566 VCO (6.8 GHz) → SMA bias tee → Laser current input
                                ↑
                         DC current (LDC205C)
     ```
   - Build on small PCB or breadboard
   - VCO output: ~0 dBm (1 mW) is sufficient
   - Bias tee separates DC (laser current) from AC (6.8 GHz modulation)
   - Tune VCO frequency precisely to 6.834682 GHz (use frequency counter or spectrum analyzer)

   **Expected result:** Laser output has three frequency components:
   - Carrier at ν₀ (center frequency)
   - Upper sideband at ν₀ + 6.8 GHz
   - Lower sideband at ν₀ - 6.8 GHz

**Week 2: Vapor Cell and CPT Observation**

4. **Prepare Rb vapor cell**
   - If using bare cell: wrap with Kapton tape heater (25W, small strips)
   - Add thermocouple to monitor temperature
   - Heat to 40-50°C (adjust for optimal signal)
   - Shield from stray magnetic fields (mu-metal sheet or three orthogonal Helmholtz coils)

5. **Align beam through cell**
   - Position cell in beam path (use simple mounts or clay)
   - Focus beam to ~1-2 mm diameter through cell center
   - Collect transmitted light on FDS100 photodiode

6. **Observe CPT resonance**
   - Connect photodiode to oscilloscope (DC coupling)
   - Slowly scan laser frequency (adjust current or temperature)
   - Look for **narrow transmission peak** (CPT resonance) within broader absorption dip
   - Width: ~1-10 kHz (much narrower than Doppler width ~500 MHz)

   **What you'll see:**
   - Broad absorption dip (~500 MHz wide) from Doppler broadening
   - Sharp transmission spike at center (CPT dark state)
   - Peak occurs when laser frequency is centered such that both sidebands are resonant

**Week 3: 7 MHz CW Detection Setup**

7. **Build RF field applicator**
   - Use **Option A from Method 1** (parallel copper plates, 5 cm spacing)
   - Or wrap coil around vapor cell (10 turns, 10 cm diameter)

8. **Generate 7 MHz CW signal**
   - Arduino + AD9850 DDS module programmed for 7.000 MHz output
   - Or use function generator set to 7 MHz, 1 Vpp
   - Connect to RF amplifier (optional, for stronger signal)
   - Feed into parallel plates or coil

9. **Detect 7 MHz modulation of CPT signal**
   - Lock laser frequency to CPT resonance (manually or with slow feedback)
   - Monitor photodiode on oscilloscope, AC coupling, 10 MHz bandwidth
   - Apply 7 MHz CW signal to cell

   **Detection mechanism:**
   - 7 MHz E-field causes AC Stark shift of ground states F=1 and F=2
   - This shifts CPT resonance frequency at 7 MHz rate
   - Since laser is locked to CPT peak, transmission oscillates at 7 MHz
   - Observe 7 MHz sine wave on oscilloscope

10. **Optimize and calibrate**
    - Increase 7 MHz amplitude: observe larger oscilloscope signal
    - Plot photodiode AC amplitude vs. applied E-field (known from V/d)
    - Typical sensitivity: 5-50 mV/cm with simple setup

#### Testing with Amateur Radio 7 MHz CW

11. **Connect outdoor antenna**
    - String 40m dipole (2×10m wires, center-fed)
    - Run coax to parallel plates near vapor cell
    - Add RF preamplifier if signals are weak (e.g., ZX60-33LN-S+, $30)

12. **Monitor amateur radio band**
    - Use RTL-SDR tuned to 7.000-7.300 MHz
    - Listen for CW (Morse code) transmissions - common in evening hours
    - Typical signals: dit-dah-dit patterns (dots and dashes)

13. **Observe CW on atomic sensor**
    - When CW transmission occurs, oscilloscope shows 7 MHz burst
    - Duration matches Morse code elements (50-200 ms dots/dashes)
    - **Proof of detection:** Oscilloscope and audio from SDR are synchronized

#### Expected Performance

- **Sensitivity:** 5-50 mV/cm (worse than full EIT, but adequate)
- **7 MHz detection:** Yes, clear on/off keying visible
- **Advantages:** Ultra-compact, low power (~2W total), room temperature
- **Build time:** 2-3 weeks for first-time builder

#### Troubleshooting

- **No CPT signal:** Check 6.8 GHz modulation (use spectrum analyzer), magnetic field shielding, laser frequency
- **CPT too weak:** Increase modulation depth, optimize cell temperature, reduce beam diameter
- **7 MHz signal buried in noise:** Add lock-in amplifier, improve RF shielding, increase antenna gain
- **Drift:** Stabilize laser temperature (±0.01°C), shield from air currents

#### Why This Works for 7 MHz

The CPT dark state is extremely sensitive to perturbations. Even though 7 MHz is far from the GHz hyperfine splitting, the AC E-field modulates:
1. **Differential light shift** between F=1 and F=2 states
2. **Zeeman shifts** (if 7 MHz has magnetic component)
3. **Laser intensity** via electroabsorption in vapor cell

Combined, these give measurable 7 MHz modulation of transmitted intensity.

### 3. Faraday Rotation Sensors ($5k-$15k)

**Concept:**
A linearly polarized laser beam passing through Rb vapor rotates its polarization angle when exposed to a magnetic field (Faraday effect). The 7 MHz CW signal's **magnetic component** (B-field from loop antenna or inductor) causes time-varying Faraday rotation at 7 MHz. This rotation is converted to intensity modulation using a polarizing beam splitter and balanced detector.

#### Detailed Parts List

| Item | Part Number/Description | Supplier | Approx. Cost |
|------|------------------------|----------|--------------|
| **Rb Vapor Cell** | 25-50mm, natural abundance | Thorlabs/eBay | $300-1,000 |
| **780 nm Laser Diode** | L780P010 (10 mW DFB laser) | Thorlabs | $300 |
| **Laser Controller** | ITC4001 (current + TEC) | Thorlabs | $1,200 |
| **Linear Polarizer (input)** | LPVIS050 (high extinction) | Thorlabs | $85 |
| **Polarizing Beam Splitter** | PBS252 (cube, 620-1000nm) | Thorlabs | $165 |
| **Balanced Photodetector** | PDB450A (DC-150 MHz) | Thorlabs | $695 |
| **Quarter-wave plate** | WPQ10M-780 (for circular pol, optional) | Thorlabs | $140 |
| **Lenses (2×)** | AC254-045-B (f=45mm) | Thorlabs | $55 each |
| **Helmholtz Coils** | DIY: 200 turns, 20 cm diameter, pair | DIY wire | $40 |
| **Mu-Metal Shield** | Cylinder, 10 cm dia × 15 cm long | Magnetic Shield Corp | $200-500 |
| **Lock-in Amplifier** | SR830 (used) or HF2LI | eBay/Zurich | $1,500 / $15k |
| **7 MHz Loop Antenna** | 10-turn coil, 30 cm dia, tuned | DIY | $30 |
| **Cell Heater** | Kapton tape + PID controller | Omega | $100 |
| **Oscilloscope** | 100 MHz, 2-ch | eBay | $300 |

**Total: $5,000-$15,000** (depending on lock-in choice)

#### Step-by-Step Build

**Week 1: Optical Path and Polarization Setup**

1. **Assemble laser system**
   - Mount L780P010 DFB laser in SM1-threaded mount
   - Connect to ITC4001 controller (current + TEC)
   - Set current to 20 mA, temperature to 25°C
   - Output: ~10 mW, very stable frequency (DFB laser has narrow linewidth)

2. **Create polarized beam**
   - Place LPVIS050 linear polarizer after laser
   - Adjust polarizer angle to maximize transmission (find extinction axis)
   - Verify polarization: rotate second polarizer 90° should block all light

3. **Vapor cell preparation**
   - Wrap cell with Kapton heater, set to 45-55°C
   - Place inside mu-metal cylinder (shields from Earth's B-field ~50 µT)
   - Leave small holes for laser beam entrance/exit
   - Install Helmholtz coils around shield (for zeroing residual fields)

**Week 2: Faraday Rotation Detection**

4. **Build balanced detection path**
   ```
   LASER → LINEAR POLARIZER → VAPOR CELL → PBS CUBE → Balanced Detector
                                                    ↓
                                              (S and P polarizations separated)
   ```
   - PBS cube splits beam into S-pol (reflected) and P-pol (transmitted)
   - Each output goes to one channel of PDB450A balanced detector
   - Balanced output = (I_S - I_P) / (I_S + I_P) ∝ rotation angle

5. **Null the detector**
   - With no B-field, rotate PBS cube angle to balance S and P signals
   - Balanced output should be near zero (µV level)
   - Small residual signal OK - this is the null point

6. **Test with DC magnetic field**
   - Apply small DC current to Helmholtz coils (start with 10 mA)
   - Observe balanced detector output change (should see mV-level shift)
   - Reverse current → signal reverses (confirms Faraday rotation)
   - Typical sensitivity: ~1 mV output per nT B-field

**Week 3: 7 MHz CW Detection Setup**

7. **Build 7 MHz magnetic field applicator**
   - Wind 10 turns of 18 AWG wire in 30 cm diameter coil
   - Position coil with axis aligned to laser beam (parallel to vapor cell)
   - Add tuning capacitor for resonance:
     ```
     L ≈ 10 µH (10 turns, 30 cm)
     Resonance at 7 MHz: C = 1/(4π²f²L) ≈ 50 pF
     ```
   - Connect 7 MHz signal generator via 50Ω coax
   - At resonance, Q ~100 → 100× voltage gain

8. **Generate 7 MHz magnetic field**
   - Function generator: 7.000 MHz, 1 Vpp into resonant coil
   - Current in coil: I = V×Q/ωL ≈ 10-100 mA (depending on Q)
   - B-field at cell center: B ≈ μ₀NI/d = (4π×10⁻⁷)(10)(0.1A)/0.3m ≈ 4 µT peak

9. **Detect 7 MHz Faraday rotation**
   - Connect balanced detector output to oscilloscope (AC coupling, 10 MHz BW)
   - Apply 7 MHz to coil
   - Observe 7 MHz sine wave on oscilloscope
   - Amplitude proportional to B-field strength

   **Physics:**
   - Faraday rotation angle: θ = V × B × L
     - V = Verdet constant (~10⁶ rad/T/m for Rb vapor at 780 nm)
     - B = 4 µT
     - L = 0.05 m (cell length)
   - θ ≈ (10⁶)(4×10⁻⁶)(0.05) = 0.2 radians = 11°
   - Intensity modulation: ΔI/I ≈ sin(2θ) ≈ 35% (easily detectable!)

**Week 4: Testing with Amateur Radio 7 MHz**

10. **Build receive loop antenna**
    - Large loop: 2-3 meter diameter, 1-2 turns
    - Or ferrite rod antenna: 100 turns on 30 cm ferrite rod
    - Tune with variable capacitor to 7 MHz
    - Connect to magnetic field coil via matching network

11. **Passive detection of 7 MHz CW**
    - Place receive loop outdoors, oriented for best signal
    - Use RTL-SDR to monitor 40m band audio
    - When CW transmission occurs:
      - Audio from SDR: beep-beep-beep (Morse code)
      - Oscilloscope from balanced detector: 7 MHz bursts synchronized with audio
    - Typical signal: 100W at 50 km → ~10 nT at receive antenna
      - This produces ~1 mV signal on balanced detector

12. **Convert to E-field detection**
    - Since E-field and B-field are related in EM wave: E = c×B
    - B = 10 nT → E = (3×10⁸ m/s)(10×10⁻⁹ T) = 3 V/m = 30 mV/cm
    - So 1 mV detector signal corresponds to 30 mV/cm E-field
    - **Sensitivity: ~30 mV/cm** (comparable to other methods)

#### Expected Performance

- **B-field sensitivity:** 100 pT - 1 nT (with lock-in)
- **E-field sensitivity (converted):** 3-30 mV/cm
- **7 MHz detection:** Excellent - Faraday rotation responds to AC fields
- **Bandwidth:** DC - 100 MHz (limited by balanced detector)
- **Advantages:** Very linear, wide dynamic range, works off-resonance

#### Troubleshooting

- **No Faraday signal:** Check mu-metal shielding (residual DC field saturates signal), verify laser wavelength
- **Signal too small:** Increase cell temperature (more atoms), use longer cell, increase B-field
- **Noise:** Improve balance (adjust PBS angle finely), add lock-in amplifier, shield from vibration
- **Drift:** Stabilize laser wavelength, temperature, magnetic shield position

#### Why Faraday Rotation Excels at 7 MHz

Unlike hyperfine transitions (GHz), Faraday rotation works at **any frequency** from DC to GHz:
- The AC magnetic field directly rotates polarization (no need to match atomic transition)
- Response is nearly instantaneous (limited only by atomic collision time ~ns)
- Linear in B-field (no saturation effects at modest power)

This makes it ideal for HF/VHF detection (1-100 MHz range).

### 4. Thermal Beam / Effusive Cell Methods (Educational: $500-$2k)

**Concept:**
Heat sodium metal in a glass tube to create vapor (~200-300°C). A 589 nm laser excites sodium atoms to the first excited state (D-line). The 7 MHz RF field modulates fluorescence intensity via Autler-Townes splitting or AC Stark shifts. Detect modulation with photodiode. This is the **simplest and cheapest** atomic sensor, ideal for education.

#### Detailed Parts List

| Item | Description | Supplier | Cost |
|------|-------------|----------|------|
| **Sodium metal** | 5-10 grams, 99.9%, in mineral oil | Sigma-Aldrich/eBay | $50-100 |
| **Glass tube** | Pyrex, 15mm OD, 30 cm length, sealed one end | Scientific glass supplier | $30 |
| **Vacuum pump** | Roughing pump (10⁻³ Torr) | Harbor Freight / eBay | $100-200 |
| **Argon gas** | Small cylinder (buffer gas, ~10 Torr) | Welding supply | $50 |
| **589 nm laser** | Yellow laser pointer (5-50 mW) stabilized | LaserGlow / Z-Bolt | $200-500 |
| **OR: 589 nm LED** | High-power yellow LED + narrow filter | Lumileds / Edmund Optics | $100 |
| **Photodiode** | BPW34 (Si, cheap, sensitive) | Digikey | $2 |
| **Heater** | Nichrome wire (24 AWG, 5 ft) + fiberglass tape | eBay | $15 |
| **Variac** | 0-140V variable transformer | Amazon | $50 |
| **Thermocouple** | K-type, 0-400°C | Omega/Amazon | $10 |
| **7 MHz source** | Function generator or Arduino DDS | eBay / DIY | $50-300 |
| **RF coil** | 20 turns, 10 cm diameter, around cell | DIY wire | $5 |
| **Oscilloscope** | 20 MHz+, 1-2 channel | eBay (old Tek) | $100-300 |
| **Optics** | Lens (f=50mm), mounts, posts | Surplus Shed / eBay | $50 |

**Total: $500-$1,500** (depends on new vs. surplus parts)

#### Step-by-Step Build

**SAFETY WARNING:**
- Sodium reacts violently with water/moisture → fire/explosion risk
- Work in dry environment, have Class D fire extinguisher (dry sand backup)
- Wear safety glasses, gloves, lab coat
- Cut sodium under mineral oil, transfer quickly to dry tube
- Seal tube under vacuum or inert gas

**Week 1: Cell Construction (Most Critical Step)**

1. **Prepare glass tube**
   - Use Pyrex tube 15mm OD × 30 cm long, sealed at one end
   - Clean thoroughly: acetone, methanol, distilled water, bake at 150°C for 1 hour
   - Dry completely (overnight in oven at 100°C)

2. **Add sodium metal (work under argon or in glovebox)**
   - Remove ~1 gram sodium from mineral oil
   - Quickly cut into small chunks (~5mm cubes) under oil
   - Blot dry with paper towel (wear gloves!)
   - Drop sodium into dry tube immediately
   - Sodium should be shiny silver (tarnish = oxidized = bad)

3. **Evacuate and seal**
   - Connect tube to vacuum pump via flexible hose + valve
   - Pump down to 10⁻³ Torr (use roughing pump, 15-30 min)
   - Backfill with argon to 10 Torr (buffer gas prevents radiation trapping)
   - Seal tube with torch (propane or glass-working torch)
     - Heat neck region to ~1000°C, pull to close
     - Allow sodium to remain cold (ice bath on bottom of tube during sealing)

   **Alternative (simpler but less optimal):**
   - Skip vacuum, just flush with argon, seal quickly
   - Some air contamination OK for educational purposes (reduces lifetime to weeks vs. years)

**Week 2: Optical and Heating Setup**

4. **Build heater assembly**
   - Wrap nichrome wire around tube (20-30 turns, spaced evenly over 10 cm section)
   - Cover with fiberglass tape for insulation and electrical safety
   - Attach thermocouple to tube wall with Kapton tape
   - Connect nichrome to variac (start at 0V!)

5. **Heat cell gradually**
   - Increase variac slowly over 30 minutes to avoid thermal shock
   - Target temperature: 250-300°C (sodium vapor pressure ~0.1-1 Torr)
   - Monitor thermocouple: Pyrex melts at 820°C, safe up to 500°C
   - Observe: sodium melts at 98°C (silvery liquid), vaporizes above 200°C (faint yellow glow)

6. **Optical setup**
   - Point 589 nm laser through cell (along tube axis)
   - Use lens to focus beam to 2-3 mm diameter in cell center
   - Place photodiode 10-20 cm after cell to collect fluorescence (orthogonal to beam for best signal)
   - Shield photodiode from direct laser light (black tube/baffles)

**Week 3: 7 MHz CW Detection**

7. **Observe sodium D-line absorption**
   - With laser on and cell hot, photodiode should show reduced signal when laser passes through vapor (absorption)
   - Tune laser wavelength (if tunable) to maximize absorption (589.0 nm or 589.6 nm, D2 or D1 lines)
   - If using fixed laser pointer: adjust cell temperature to shift Doppler profile into resonance

8. **Build RF coil for 7 MHz**
   - Wind 20 turns of magnet wire in 10 cm diameter coil
   - Slide cell through coil center (coil axis = tube axis)
   - Connect to 7 MHz function generator (1-10 Vpp)

9. **Detect 7 MHz modulation**
   - Connect photodiode to oscilloscope (AC coupling, 10 MHz BW)
   - Apply 7 MHz signal to coil
   - Look for 7 MHz modulation on photodiode signal

   **Expected mechanism:**
   - AC Stark shift: 7 MHz E-field/B-field shifts atomic levels at 7 MHz rate
   - This modulates absorption → fluorescence changes at 7 MHz
   - Signal amplitude: ~0.1-1% of DC fluorescence (weak but detectable)

10. **Optimize sensitivity**
    - Increase 7 MHz amplitude (use RF power amplifier if available, e.g., 10-50W)
    - Adjust cell temperature for maximum absorption (more atoms = stronger signal)
    - Use lock-in amplifier referenced to 7 MHz (dramatically improves SNR)

**Week 4: Testing with Real 7 MHz CW**

11. **Connect outdoor antenna**
    - 40m dipole (2×10m wires) connected to RF coil via 50Ω coax
    - Add RF preamp if needed (e.g., 20 dB gain at 7 MHz)

12. **Monitor amateur radio**
    - Use RTL-SDR or communications receiver tuned to 7.000-7.200 MHz
    - Listen for CW transmissions (common in evenings, especially 7.025-7.040 MHz)

13. **Observe on sodium sensor**
    - When CW transmission occurs, oscilloscope shows 7 MHz burst
    - On/off pattern matches Morse code elements
    - Typical signal strength: 100W transmitter at 50 km → 0.1-1 V/cm at antenna
    - Sodium sensor detects this as ~0.1-1 mV modulation on photodiode

#### Expected Performance

- **Sensitivity:** 0.1-1 V/cm (1000× worse than Rydberg, but works!)
- **7 MHz detection:** Yes, visible on oscilloscope during strong CW transmissions
- **Advantages:** Ultra-cheap, educational, no expensive lasers, demonstrates atomic sensing
- **Limitations:** Poor sensitivity, short cell lifetime if air-contaminated, safety concerns

#### Troubleshooting

- **No fluorescence:** Cell too cold (increase temp), laser off-resonance, photodiode not aligned
- **Weak absorption:** Sodium oxidized (cell has leak), temperature wrong
- **No 7 MHz signal:** RF power too low (need 10W+), coil not coupled to cell, photodiode saturated
- **Cell degraded:** Sodium turned black (oxide) - cell is dead, build new one

#### Educational Value

This setup is perfect for undergraduate physics labs:
- Demonstrates atomic spectroscopy (D-line absorption/fluorescence)
- Shows quantum sensing principles at low cost
- Introduces vacuum techniques, glass-working (optional), RF electronics
- Can detect real-world RF signals (ham radio CW)
- Total cost ~$500 with careful scrounging

#### Advanced Variation: Sodium Lamp Excitation

Instead of laser, use sodium street lamp (low-pressure Na discharge):
- **Cost:** $20-50 (eBay, old street lamp)
- **Wavelength:** Perfect match to D-line (589 nm, both lines present)
- **Detect:** Increased fluorescence when RF is applied (opposite of absorption measurement)
- **Advantage:** No laser stabilization needed
- **Disadvantage:** Broad, incoherent source (lower signal)

### 5. Repurposed Atomic Clock Modules ($1k-$3k)

**Concept:**
Commercial rubidium atomic frequency standards (used in telecom, GPS, military) contain a complete atomic physics package: Rb-87 cell, RF synthesizer at 6.8 GHz, lamp, photodetector, and servo electronics. These devices lock their output frequency to the Rb hyperfine transition. By tapping the **error signal** (which monitors deviation from atomic resonance), we can detect external RF fields that shift the atomic transition. For 7 MHz detection, we apply the HF signal to shift the resonance and observe the error signal modulation.

#### Recommended Surplus Units

| Model | Manufacturer | Typical Price | Notes |
|-------|--------------|---------------|-------|
| **LPRO-101** | Symmetricom (Microsemi) | $500-$1,000 | Most common, good docs available |
| **FE-5680A** | Frequency Electronics | $300-$800 | Compact, lower power |
| **PRS10** | Stanford Research Systems | $1,500-$2,500 | Best performance, lab-grade |
| **CSAC** | Symmetricom (chip-scale) | $1,000-$1,500 | Ultra-compact, lower performance |

**Best choice for hacking: LPRO-101** (abundant on eBay, active enthusiast community on Time-Nuts mailing list)

#### Detailed Parts List

| Item | Description | Supplier | Cost |
|------|-------------|----------|------|
| **Rb Frequency Standard** | Symmetricom LPRO-101 (used, working) | eBay | $500-1,000 |
| **Power Supply** | +5V, 1.5A regulated | Amazon/bench supply | $20-50 |
| **Oscilloscope** | 100 MHz, 2-channel | eBay | $200-400 |
| **Multimeter** | Basic DMM for DC voltages | Amazon | $20 |
| **7 MHz Source** | Function generator or SDR transmit | eBay | $50-300 |
| **Copper plates** | For E-field application near Rb cell | Hardware store | $10 |
| **Coax/connectors** | SMA, BNC cables | Amazon | $20 |
| **Lock-in Amplifier** | SR830 (optional, for low-level signals) | eBay | $1,500 (used) |

**Total: $800-$2,500** (depends on luck finding cheap LPRO)

#### Step-by-Step Modification

**Week 1: Understanding the Unit**

1. **Acquire LPRO-101 and documentation**
   - Buy from eBay (search "rubidium frequency standard LPRO")
   - Download service manual: available on Time-Nuts archives or K6JCA website
   - Key specs: Output 10 MHz sine wave, locks to Rb 6.834682610904 GHz

2. **Power up and verify operation**
   - Connect +5V power (pin 1 = +5V, pin 7 = GND, DB-9 or DB-15 connector)
   - Current draw: ~1.2A initially (heater), settles to 0.8A after warm-up (~5 min)
   - Monitor 10 MHz output on oscilloscope (should be clean sine wave, ~1 Vpp)
   - Wait ~10 minutes for frequency lock (LED indicator or check control voltage)

3. **Locate test points**
   - **TP1: Error signal / C-field DAC** (monitors deviation from lock point)
   - **TP2: Lamp photodiode output** (RF absorption signal)
   - **TP3: 6.8 GHz synthesizer monitor** (low-level 6.8 GHz output)
   - Refer to service manual for exact locations (usually small vias or resistor pads)

**Week 2: Tapping the Error Signal**

4. **Access internal circuitry (WARNING: Voids warranty, risk of damage)**
   - Remove top cover (usually 4-6 screws)
   - ESD precautions: ground wrist strap, work on anti-static mat
   - Identify physics package (metal cylinder, ~3 cm diameter) and control PCB

5. **Connect oscilloscope to error signal (TP1)**
   - Use high-impedance probe (10 MΩ, 10× attenuation)
   - Should see ~0-5V DC when locked (varies by unit)
   - This voltage adjusts C-field (magnetic field) to keep atoms on resonance
   - Changes in this voltage indicate shift in atomic transition frequency

**Week 3: 7 MHz Field Application**

6. **Build E-field applicator**
   - Cut two copper plates (5 cm × 5 cm)
   - Position plates 3-5 cm apart, straddling the physics package inside LPRO
   - Route wires carefully (don't short to PCB!)
   - Connect to BNC feedthrough or bring wires out through ventilation holes

7. **Apply 7 MHz signal**
   - Function generator: 7.000 MHz, start with 1 Vpp
   - Feed into copper plates
   - **Detection mechanism:**
     - 7 MHz E-field causes AC Stark shift of Rb hyperfine transition
     - This shifts transition frequency by small amount (~kHz level)
     - Servo loop tries to compensate → error signal (TP1) shows 7 MHz modulation

8. **Observe 7 MHz on error signal**
   - Oscilloscope connected to TP1, AC coupling, 10 MHz bandwidth
   - Apply 7 MHz to plates
   - Look for 7 MHz sine wave superimposed on DC error voltage
   - Amplitude: ~1-10 mV for 1 V/cm E-field (depends on servo bandwidth)

**Week 4: Calibration and Testing**

9. **Calibrate sensitivity**
   - Known E-field: E = V/d (voltage between plates / spacing)
   - Example: 5 Vpp across 5 cm → E = 5V / 0.05m = 100 V/m = 1 V/cm
   - Measure TP1 modulation amplitude
   - Responsivity: (mV modulation at TP1) / (V/cm applied field)
   - Typical: 10-100 µV per mV/cm → sensitivity ~10-100 mV/cm

10. **Test with amateur radio 7 MHz CW**
    - Connect 40m dipole to copper plates (via matching network if needed)
    - Monitor 7 MHz band with RTL-SDR
    - During CW transmission: TP1 shows bursts synchronized with Morse code
    - Typical received signal (100W at 50 km): ~10-100 mV/cm
    - Should produce ~1-10 mV modulation on TP1

11. **Improve sensitivity with lock-in detection**
    - Connect TP1 to lock-in amplifier input
    - Reference: 7 MHz from function generator or recovered from antenna signal
    - Lock-in extracts 7 MHz component from noise
    - Can improve sensitivity by 10-100× (down to ~1-10 mV/cm)

#### Expected Performance

- **Sensitivity:** 10-100 mV/cm (direct), 1-10 mV/cm (with lock-in)
- **7 MHz detection:** Yes, via error signal modulation
- **Advantages:** Turnkey hardware, reliable, includes all RF/servo electronics
- **Bandwidth:** ~1 kHz (limited by servo loop response time)
- **Limitations:** Slow servo (can't track fast variations), bulky

#### Troubleshooting

- **Unit won't lock:** Check power voltage (must be 5.0V ±0.1V), warm-up time, aged Rb lamp (replace lamp if >10 years old)
- **No error signal:** Wrong test point, unit not locked, probe loading circuit
- **No 7 MHz response:** E-field too weak (increase amplitude), physics package shielded (better coupling needed)
- **Drift:** Temperature changes (LPRO has oven, but still sensitive), aging (normal, ~1×10⁻¹¹/day)

#### Advanced: Heterodyne Detection for Direct HF Measurement

For true HF sensitivity, mix 7 MHz signal with internal 6.8 GHz synthesizer:

1. Extract 6.8 GHz from TP3 (low-level signal, ~-20 dBm)
2. Mix with 7 MHz using microwave mixer (e.g., Minicircuits ZX05-153MH-S+)
3. Products: 6.800 GHz ± 7 MHz = 6.793 GHz and 6.807 GHz sidebands
4. One sideband is closer to Rb transition → enhances response
5. **Improved sensitivity:** ~100 µV/cm (10× better)

#### Why This Works

The Rb frequency standard is essentially a complete atomic sensor in a box. The servo electronics continuously monitor the atomic resonance and correct for drifts. By observing the error signal, we're directly measuring how much the applied 7 MHz field perturbs the atoms. This is analog to how seismometers work: the feedback signal tells you about external disturbances.

#### Community Resources

- **Time-Nuts mailing list** (groups.io/g/time-nuts): Active community of atomic clock enthusiasts
- **LPRO mods and hacks:** many members have done similar experiments
- **Schematics:** available for LPRO-101, PRS10, FE-5680A
- **Rb lamp replacement:** ~$200 from vendors, extends life by 10+ years

### 6. Nitrogen-Vacancy (NV) Diamond Sensors ($10k-$50k)

**Concept:**
Nitrogen-vacancy centers in diamond are atom-like defects with quantum spin states that can be optically initialized, manipulated, and read out. The NV center's ground state has a spin triplet (m_s = 0, ±1) split by 2.87 GHz. A 7 MHz RF field modulates the spin state populations via AC Stark shifts and spin mixing, changing the fluorescence intensity. NV sensors work at room temperature and offer nanoscale spatial resolution - ideal for near-field RF mapping.

#### How NV Centers Detect 7 MHz

Unlike alkali atoms (GHz hyperfine transitions), NV centers respond to 7 MHz via:
1. **AC electric field coupling:** Shifts ground state levels via Stark effect (quadratic in E-field)
2. **AC magnetic field coupling:** Zeeman effect modulates m_s = ±1 splitting (linear in B-field)
3. **Strain modulation:** Piezoelectric effect in diamond converts E-field to strain, shifts NV levels

The key advantage: **broadband response** from DC to GHz, making 7 MHz detection straightforward.

#### Detailed Parts List

| Item | Description | Supplier | Cost |
|------|-------------|----------|------|
| **NV Diamond Sample** | Type Ib, [NV⁻] ~1 ppm, polished, 3×3×0.5 mm | Element Six / Adamas Nano | $500-2,000 |
| **532 nm Laser** | DPSS, 50-200 mW, single-mode | Thorlabs (DJ532-40) | $2,500 |
| **Photodetector** | APD or PMT for fluorescence (650-800 nm) | Thorlabs (APD430A2) | $3,500 |
| **Dichroic Mirror** | 532 nm reflect / 650+ nm transmit | Semrock (Di03-R532) | $350 |
| **Long-pass Filter** | Block 532 nm, pass 650-800 nm | Semrock (BLP01-532R) | $300 |
| **Objective Lens** | NA 0.7-0.9, infinity-corrected, 40-100× | Olympus / Nikon | $1,000-3,000 |
| **Microwave Source** | 2.87 GHz synthesizer + amplifier | Mini-Circuits / HP | $1,000-3,000 |
| **Microwave Antenna** | Copper wire loop or stripline on PCB | DIY | $10 |
| **7 MHz Source** | Function generator | eBay | $100-500 |
| **Lock-in Amplifier** | SR830 or equivalent | eBay | $1,500 (used) |
| **Optical Table/Breadboard** | Vibration isolation | Thorlabs | $500-2,000 |
| **Misc. optics** | Mirrors, lenses, mounts | Thorlabs | $1,000 |
| **Magnet** | Permanent (10-100 Gauss, optional) | K&J Magnetics | $20 |

**Total: $12,000-$20,000** (entry-level), up to $50k for complete microscope setup

#### Step-by-Step Build

**Week 1-2: Optical Setup (Confocal Fluorescence Microscope)**

1. **Mount NV diamond sample**
   - Attach diamond to glass slide with index-matching oil
   - Position on XYZ translation stage (micrometer precision)
   - Orient diamond with [100] or [111] face up (NV axis known)

2. **Build optical excitation path**
   ```
   532 nm LASER → DICHROIC MIRROR → OBJECTIVE → DIAMOND
                                          ↑
                                    FLUORESCENCE (650-800 nm)
                                          ↓
                                   LONG-PASS FILTER → APD
   ```
   - Expand and collimate 532 nm beam to fill objective back aperture
   - Dichroic reflects 532 nm down into objective, transmits red fluorescence up
   - Objective focuses 532 nm to ~500 nm spot on diamond (~1 µm² area)
   - Collect fluorescence through same objective (confocal geometry)
   - Long-pass filter blocks scattered 532 nm laser light
   - APD detects red fluorescence (zero-phonon line at 637 nm + phonon sideband to 800 nm)

3. **Observe NV fluorescence**
   - With 50 mW laser power, expect 10⁴-10⁶ counts/sec on APD (depends on NV density)
   - Scan XYZ stage to find bright NV centers (use software like Python + DAQ)
   - Individual NV centers appear as diffraction-limited spots (~500 nm FWHM)

**Week 2-3: Microwave Setup and ODMR**

4. **Build microwave delivery**
   - **Option A (simple):** Copper wire loop (10 mm diameter) placed 1-2 mm above diamond
   - **Option B (better):** PCB stripline (50 Ω impedance) with diamond on top
   - Connect to 2.87 GHz synthesizer + amplifier (1-10W output)

5. **Perform Optically Detected Magnetic Resonance (ODMR)**
   - Apply continuous 532 nm laser + constant microwave power (~10 dBm at antenna)
   - Sweep microwave frequency from 2.80 to 2.95 GHz (slow scan, ~10 sec)
   - Monitor APD count rate vs. frequency
   - **Expected result:** Fluorescence **dip** at 2.87 GHz (m_s = 0 → m_s = ±1 transition)
   - Dip depth: 10-30% of baseline fluorescence
   - Linewidth: 1-10 MHz (depends on NV quality, power broadening)

6. **Apply static magnetic field (optional)**
   - Place small permanent magnet near diamond (~10-100 Gauss field)
   - ODMR now shows **two dips** (Zeeman splitting of m_s = -1 and +1)
   - Separation: ~2.8 MHz per Gauss (gyromagnetic ratio of NV electron spin)
   - This improves sensitivity for B-field detection

**Week 3-4: 7 MHz RF Field Detection**

7. **Build 7 MHz E-field or B-field applicator**

   **For E-field:**
   - Place two small electrodes (copper tape, 1 mm wide) on diamond surface, 100 µm apart
   - Connect to 7 MHz function generator (1-10 Vpp)
   - E-field between electrodes: E = V / 100 µm = 10⁵ V/m = 1000 V/cm (strong!)

   **For B-field:**
   - Wind small coil (5-10 turns, 5 mm diameter) around diamond
   - Drive with 7 MHz, 0.1-1 Vpp
   - B-field at diamond: ~1-10 µT AC

8. **Detection method: Amplitude modulation of ODMR**
   - Set microwave frequency to slope of ODMR dip (maximum dF/df sensitivity)
   - Apply 7 MHz signal to diamond
   - **Mechanism:**
     - 7 MHz E-field/B-field shifts NV spin levels at 7 MHz rate
     - This shifts ODMR resonance frequency → fluorescence modulates at 7 MHz
   - Monitor APD output on oscilloscope (AC coupling, 10 MHz BW)
   - Observe 7 MHz sine wave synchronized with applied signal

9. **Lock-in detection for improved SNR**
   - Connect APD to lock-in amplifier input
   - Reference: 7 MHz from function generator
   - Lock-in measures amplitude of 7 MHz modulation
   - Sensitivity: ~1 mV/cm for E-field, ~100 pT for B-field (with 1 Hz bandwidth)

**Week 4: Testing with Amateur Radio 7 MHz CW**

10. **Build receive antenna coupled to diamond**
    - Small loop antenna (10 cm diameter, resonant at 7 MHz) placed near diamond
    - Or capacitive coupling: 40m dipole → parallel plates with diamond between them

11. **Monitor 7 MHz amateur band**
    - RTL-SDR tuned to 7.000-7.300 MHz CW activity
    - When CW transmission occurs, lock-in output shows step increase
    - Morse code dots/dashes visible as amplitude changes

12. **Spatial mapping (advanced)**
    - Scan XYZ stage to map 7 MHz field distribution
    - Create 2D/3D maps of E-field or B-field amplitude
    - Resolution: ~500 nm (diffraction limit)
    - Applications: Near-field imaging of antennas, circuits, transmission lines

#### Expected Performance

- **E-field sensitivity:** 1-10 mV/cm (room temperature, single NV)
  - Can reach µV/cm with ensemble averaging or cryogenic cooling
- **B-field sensitivity:** 10-100 pT (single NV), sub-pT (ensemble)
- **Spatial resolution:** 500 nm (optical diffraction limit) to sub-nm (scanning probe)
- **7 MHz detection:** Excellent - direct coupling to spin levels
- **Bandwidth:** DC - several GHz (limited by NV spin relaxation, ~ms)
- **Advantages:** Solid-state, room temp, nanoscale imaging, no drift

#### Troubleshooting

- **No fluorescence:** Laser wavelength wrong (must be 532 nm ±5 nm), misaligned optics, no NV centers (wrong diamond)
- **No ODMR dip:** Microwave power too low/high, frequency wrong, NV centers photobleached
- **Weak 7 MHz signal:** Poor coupling (electrodes/coil too far), NV not aligned with field, lock-in settings wrong
- **Background noise:** Laser intensity noise (use balanced detection), vibration (isolate table), RF pickup

#### Why NV Centers Excel for 7 MHz

1. **Broad spectral response:** Unlike atomic hyperfine transitions (must match GHz), NV centers respond to any frequency that modulates their spin states
2. **Room temperature operation:** No vapor cell, heater, vacuum needed
3. **Spatial resolution:** Can map 7 MHz near-fields at sub-wavelength scale (λ @ 7 MHz = 43 m, but NV resolves to ~500 nm!)
4. **Vectorial sensing:** NV centers along different crystallographic axes ([111] directions in diamond) sense different field components → full 3D vector reconstruction

#### Applications Beyond 7 MHz CW Detection

- **Biomedical:** Image RF heating in tissue (MRI safety, ablation therapy)
- **Electronics:** Debug IC RF emissions, antenna design
- **Quantum information:** Read out spin qubits, magnetic imaging of quantum materials
- **Geophysics:** Sub-nT magnetometry for mineral prospecting

#### Alternative: Ensemble NV Sensing (Lower Cost)

For applications not requiring nanoscale resolution, use bulk diamond with high [NV⁻] density (~10-100 ppm):

- **Cost:** $2k-$5k total (simpler optics, no scanning needed)
- **Sensitivity:** 10× better (more NV centers → more signal)
- **Spatial resolution:** ~10-100 µm (bulk measurement)
- **Setup:** Simpler - just illuminate whole diamond, collect bulk fluorescence

---

## RF Difference Detection and Antenna Array Experiments

### Basic Concept: Using Antenna Offsets for RF Difference Detection

With two small antennas (possibly receiving ones) placed near each other but slightly offset in position, we can configure a setup where a third antenna detects the difference (e.g., phase or amplitude difference) in an incoming RF signal. This is a core idea in RF engineering, particularly in **direction finding (DF)**, **interferometry**, or **phased array systems**.

#### Why Two Offset Antennas Matter

If the antennas are separated by a small distance $d$ (e.g., a fraction of the wavelength $\lambda$ of the RF signal), an incoming plane wave at an angle $\theta$ from the baseline creates a path length difference of $d \sin \theta$. This translates to a phase shift:

$$\delta = \frac{2\pi d \sin \theta}{\lambda}$$

By comparing the signals from the two antennas, you can compute this difference.

#### Role of a Third Antenna

A third antenna isn't strictly necessary for basic difference detection (you can process the two signals directly), but it can enhance the setup in several ways:

1. **Ambiguity resolution:** With only two antennas, phase differences can be ambiguous (e.g., multiple possible $\theta$ values for the same $\delta$). A third antenna, placed non-collinearly (e.g., forming a triangle), provides an additional baseline to triangulate and resolve this.

2. **Reference or calibration:** The third could act as a phase reference, especially if the incoming RF is weak or noisy, or to subtract common-mode noise/interference affecting all antennas.

3. **Improved accuracy:** In array processing, three antennas allow for better beamforming or nulling, where you electronically steer the array to focus on the difference signal.

4. **Diversity:** If the third is positioned differently, it can help detect polarization differences or multipath effects.

### Practical Setup Examples

#### Traditional RF Setup

**Hardware:**
- Two small receiving antennas (e.g., monopoles) spaced ~0.1–0.5$\lambda$ apart (for VHF/UHF bands, that's cm to meters)
- Connect them to a receiver chain with mixers or ADCs to digitize the signals

**Processing:**
1. Downconvert both signals to baseband
2. Use a phase detector (like a multiplier or IQ demodulator) to extract $\delta$

**Third antenna integration:** Add it as a reference—mix its signal with the difference from the first two to isolate the offset-induced effect. This could detect DOA with ~1–5° accuracy, depending on frequency and spacing.

**Challenges:** Calibration for mutual coupling (antennas interfering with each other), noise, and ensuring the offset doesn't exceed $\lambda/2$ to avoid aliasing.

#### Using Rydberg Atom Sensors

These vapor-cell sensors are essentially tiny, optical-readout "antennas" (~1–10 cm size) that detect RF E-fields with extreme sensitivity (down to mV/m) and broadband coverage (kHz to THz).

**Two offset sensors:** Place two cells close but slightly offset (e.g., 1–10 cm apart). Each measures the local E-field amplitude and phase via laser probing and EIT. The offset creates a measurable phase difference for incoming RF waves, enabling DOA estimation or wavefront mapping.

**Third sensor for difference detection:** Position a third cell nearby (e.g., equidistant or in an L-shape). Use it to:
- Compute pairwise differences (e.g., sensor1 - sensor2, then compare to sensor3)
- Enable vector E-field sensing (full 3D field reconstruction)

**Advantages over traditional antennas:**
- No metal parts to perturb the field
- Higher precision (phase resolution <1° possible)
- Smaller size for dense arrays
- SI-traceable measurements without calibration artifacts

**How to implement:** Digitize the optical outputs from each cell, then use signal processing (e.g., Fourier transforms) to extract differences. Labs/companies (e.g., via DARPA programs) are prototyping arrayed versions for applications like radar or communications.

### Potential Applications

- **Direction finding:** Track incoming RF sources (e.g., drones, jammers)
- **Interference detection:** Spot subtle differences in multipath signals
- **Sensing gradients:** For near-field RF, detect field variations across space

---

## Using Three Loop Antennas for RF Difference Detection Experiments

Loop antennas are ideal for these kinds of experiments because they primarily sense the **magnetic component** of electromagnetic (EM) waves, making them suitable for low-to-medium frequency RF (e.g., HF to UHF bands, like 3–300 MHz), near-field measurements, and setups where you want to minimize electric field interference. They're compact, directional (with a figure-8 pattern), and can be made from simple wire coils.

### Basic Setup Components

1. **Three loop antennas:** Make or buy small loops (e.g., 10–50 cm diameter, multi-turn wire coils for better sensitivity). Position them close but offset (e.g., 10–50 cm apart, or ~0.1–0.5 wavelengths of your target RF frequency to capture phase differences without too much ambiguity).

2. **Receivers:** Connect each loop to a low-noise amplifier (LNA) and then to a receiver (e.g., SDR dongles synced via a common clock for phase coherence).

3. **Processing:** Use software like GNU Radio, MATLAB, or Python (with libraries like NumPy/SciPy) to digitize signals, compute differences, and visualize results.

4. **Test source:** Two dipoles transmitting the same signal but with a slight phase or position offset to create an interference pattern.

**Safety note:** If dealing with transmitting antennas, keep power low (<1W) to avoid interference or regulatory issues.

### Experiment 1: Direction Finding (DOA Estimation) via Phase Differences

This detects the angle of arrival of an incoming RF signal by measuring phase shifts across the array.

#### Setup

1. Arrange the three loops in a **triangular formation** (e.g., equilateral triangle with sides ~λ/4, where λ is the wavelength). This provides two baselines for phase comparison, reducing ambiguity compared to just two antennas.

2. Orient all loops in the same plane (e.g., vertical for horizontal magnetic fields).

3. Transmit a test RF signal (e.g., 433 MHz ISM band tone) from your two offset transmitters, positioned at a known angle/distance.

#### How It Works

1. The incoming wave hits each loop at slightly different times due to the offsets, creating phase differences ($\delta$) between pairs (e.g., loop1 vs. loop2, loop1 vs. loop3).

2. Digitize the signals and use correlation or IQ data to calculate:
   $$\delta = \arg(S_2 / S_1)$$
   where $S_1$ and $S_2$ are complex signals from two loops.

3. With three loops, solve for the direction $\theta$ using trigonometry:
   $$\theta = \arcsin\left(\frac{\delta \lambda}{2\pi d}\right)$$
   where $d$ is the baseline distance. The third loop confirms and refines the estimate.

#### What You Detect

The "difference" is the phase offset, revealing the signal's direction (accuracy ~5–10° with simple setups). If your transmitters are slightly off, this simulates a wavefront tilt, and the array detects it as a non-zero $\theta$.

**Tips:** Calibrate for mutual coupling (loops can interfere). Start with simulations in Python: Model wave propagation with $e^{jkr}$ phases.

### Experiment 2: Magnetic Field Gradient Mapping (Near-Field Differences)

For detecting subtle variations in RF magnetic fields, like from closely spaced transmitters.

#### Setup

1. Place the three loops in a line or cluster near your two transmitting antennas (e.g., within 1–2 wavelengths, in the near-field zone).

2. Use one loop as a reference (central), and the other two offset slightly (e.g., +x and -x directions) to measure gradients.

#### How It Works

1. Each loop outputs a voltage proportional to the local magnetic field $H$:
   $$V \approx \mu N A \omega H$$
   where $N$ = turns, $A$ = area, $\omega$ = frequency.

2. Amplify and measure amplitude/phase from each. Compute differences:
   $$\Delta H_x = \frac{H_{\text{left}} - H_{\text{right}}}{\text{distance}}$$
   using the third for y- or z-axis if oriented differently.

3. For an incoming RF from your offset transmitters, the gradients show interference patterns (e.g., nulls or peaks due to phase cancellation).

#### What You Detect

Amplitude differences highlight field inhomogeneities—e.g., if transmitters are slightly off-frequency, you'll see beat patterns; if off-position, spatial asymmetries.

**Tips:** Good for low frequencies (<30 MHz) where loops excel. Add Faraday shielding to reduce E-field pickup.

### Experiment 3: Basic Phased Array Beamforming for Signal Enhancement/Nulling

This uses the array to electronically "steer" sensitivity, detecting differences by suppressing or amplifying parts of the incoming RF.

#### Setup

1. Configure the three loops as a small array (e.g., linear with equal spacing).

2. Feed signals into a digital beamformer (e.g., via SDRs and software).

#### How It Works

1. Apply phase shifts digitally to the signals (e.g., multiply by $e^{j\phi}$ for each channel).

2. Sum them:
   $$S_{\text{total}} = S_1 + S_2 e^{j\phi_2} + S_3 e^{j\phi_3}$$

3. Steer the beam toward your transmitters' direction to maximize the difference signal (e.g., null out interference from one transmitter while enhancing the other).

#### What You Detect

Phase/amplitude differences allow you to isolate the "offset" effect—e.g., if transmitters are slightly detuned, beamforming separates their signals.

**Tips:** Requires phase-locked receivers. For advanced twists, tie in Rydberg sensors (from earlier sections) by replacing one loop with a vapor cell for hybrid quantum-classical comparison.

### Implementation Notes

These experiments scale from DIY (cost ~$50–200 for parts) to lab-grade. Key considerations:

- **Frequency range:** Choose based on your application (HF for long-range, VHF/UHF for local experiments)
- **Synchronization:** For phase-coherent measurements, ensure all receivers share a common clock reference
- **Calibration:** Account for systematic phase offsets in cables, amplifiers, and receivers
- **Regulatory compliance:** Always check local regulations for transmitting experiments

For heterodyne detection (frequency offset approach): If the "slightly off" refers to frequency offset (not position), this could be about heterodyne detection: two antennas receiving slightly detuned signals, mixing to produce a beat frequency at the difference, and the third detecting that low-frequency output.

**For hands-on demonstrations:** You could simulate these concepts in Python with libraries like NumPy/SciPy (modeling wave propagation and phase shifts) before building physical hardware.

---

## Hybrid Rydberg-Loop Antenna Array Systems

An exciting frontier is combining **Rydberg atom electric field sensors** with **loop antenna magnetic field detectors** into hybrid arrays. This approach leverages the complementary strengths of both technologies to achieve unprecedented RF sensing capabilities.

### Why Combine Rydberg Sensors with Loop Antennas?

#### Complementary Field Sensing

The key insight is that electromagnetic waves have both **electric (E)** and **magnetic (B)** field components that are orthogonal and coupled:

$$\vec{E} = c\vec{B} \times \hat{k}$$

where $c$ is the speed of light and $\hat{k}$ is the propagation direction.

- **Rydberg sensors**: Exquisitely sensitive to E-fields (down to µV/cm), measured via EIT/Autler-Townes splitting
- **Loop antennas**: Primarily sensitive to B-fields (magnetic flux through the loop)

By measuring both simultaneously at the same spatial location, you get:
1. **Redundancy and validation**: Cross-check measurements using Maxwell's equations
2. **Polarization analysis**: Determine wave polarization (linear, circular, elliptical)
3. **Near-field vs far-field discrimination**: In near-field, E and B are not simply related by impedance of free space (377 Ω)
4. **Vector field reconstruction**: Combine multiple measurements to map full 3D electromagnetic field structure

#### Practical Advantages

1. **Phase reference**: Loop antennas provide robust, phase-coherent timing references for synchronizing multiple Rydberg sensors
2. **Dynamic range extension**: Use loops for strong fields (>1 V/cm) where Rydberg atoms might saturate
3. **Frequency coverage**: Loops excel at lower frequencies (kHz-MHz), Rydberg at higher (MHz-THz), covering full spectrum
4. **Calibration**: Loop antennas have well-known, calculable responses - use them to calibrate absolute field strengths for Rydberg sensors
5. **Cost reduction**: Start with loop arrays, then upgrade strategic positions with Rydberg sensors

### Hybrid Array Architectures

#### Architecture 1: Interleaved E/B Array

**Configuration:**
```
Layout (top view):
    L1 ---- R1 ---- L2 ---- R2 ---- L3
    |               |               |
   [Loop]      [Rydberg]        [Loop]
   (B-field)    (E-field)       (B-field)
```

- Alternate loop antennas (L) and Rydberg vapor cells (R) in a linear or 2D grid
- Spacing: ~λ/4 to λ/2 for phase coherence at target frequency
- Each position measures either E or B field

**Benefits:**
- Full vector EM field mapping with spatial resolution ~10 cm
- Phase differences reveal wavefront structure and direction of arrival
- Detect interference patterns, multipath, and near-field sources

**Use cases:**
- Direction finding with <1° accuracy
- Near-field antenna testing
- RF threat detection (drones, jammers)

#### Architecture 2: Co-located E/B Sensors

**Configuration:**
```
Single sensing node:
    ┌─────────────────┐
    │  Vapor Cell (R) │ ← Measures E-field
    │  ┌─────────┐    │
    │  │ Loop (L)│    │ ← Loop wrapped around cell
    │  └─────────┘    │    Measures B-field
    └─────────────────┘
```

- Place small loop antenna (10-20 cm diameter) concentrically around Rydberg vapor cell
- Both measure the same spatial point simultaneously
- Orient loop axis perpendicular to laser beams to avoid optical interference

**Benefits:**
- True vector field measurement at single point
- Directly verify $E = cB$ relationship (far-field) or detect near-field deviations
- Compact, portable sensor head
- Immune to position calibration errors

**Implementation:**
1. Use non-magnetic loop materials (copper, aluminum) to avoid perturbing Rydberg atoms
2. Keep loop current return path symmetric to minimize stray fields at vapor cell
3. Synchronize measurements: sample both E and B at same time (shared clock/trigger)

**Use cases:**
- Portable RF power density mapping
- EMC/EMI testing
- Bioelectromagnetics (SAR measurements)

#### Architecture 3: Loop-Referenced Rydberg Array

**Configuration:**
```
    Master Loop (phase reference)
           |
           | RF signal fed to all Rydberg sensors
           |
    ┌──────┴──────┬──────────┬──────────┐
    R1            R2         R3         R4
  [Rydberg]    [Rydberg]  [Rydberg]  [Rydberg]
  (E-field)    (E-field)  (E-field)  (E-field)
```

- Single loop antenna acts as **master phase reference**
- Distribute its signal (via low-loss coax) to all Rydberg sensor locations
- Each Rydberg sensor measures local E-field and compares phase to master loop

**Benefits:**
- Solves the "phase synchronization problem" for distributed Rydberg arrays
- All sensors locked to same RF phase reference (no clock drift between nodes)
- Enables coherent beamforming across large apertures (>10 m)

**Implementation:**
1. Use high-Q resonant loop at target frequency (e.g., 7 MHz, 433 MHz)
2. Amplify loop output and distribute via matched-length cables or fiber-optic links
3. At each Rydberg sensor, mix loop signal with optical EIT readout for phase extraction
4. Digital signal processing combines all channels for DOA, beamforming, or MIMO

**Use cases:**
- Large-aperture RF imaging (like radio astronomy, but with quantum sensors)
- Distributed spectrum sensing for cognitive radio
- Quantum radar prototypes

### Practical Implementation: Three-Sensor Hybrid Demonstrator

Here's a concrete design combining ideas from the loop antenna experiments with Rydberg sensing:

#### Hardware Configuration

**Sensor Node Design (build 3 identical units):**

| Component | Specification | Purpose |
|-----------|--------------|---------|
| **Rydberg vapor cell** | Rb-87, 75 mm length, heated to 55°C | E-field sensing via EIT |
| **Probe laser** | 780 nm ECDL, ~50 mW, locked to D2 line | Lower transition (5S→5P) |
| **Coupling laser** | 480 nm, ~500 mW (or use ground-state method to avoid this) | Upper transition (5P→Rydberg) for full Rydberg, OR skip for low-cost ground-state approach |
| **Loop antenna** | 20 cm diameter, 10 turns, wrapped around cell | B-field sensing at same point as E-field |
| **Low-noise amplifier** | 50Ω input, 40 dB gain, wideband (1-1000 MHz) | Amplify loop signal |
| **Photodiode** | Fast Si detector, >10 MHz bandwidth | Detect EIT signal from vapor cell |
| **Data acquisition** | Synchronized ADC, 16-bit, 100 MS/s, shared clock | Digitize both E and B signals simultaneously |

**Array Geometry (triangular):**
```
         Sensor 1 (S1)
            /\
           /  \
          /    \
    λ/4  /      \  λ/4
        /        \
       /          \
      /____________\
     S2            S3
           λ/4
```

- Equilateral triangle with sides = λ/4 at target frequency
- For 433 MHz: λ = 69 cm → sides ≈ 17 cm
- For 7 MHz: λ = 43 m → sides ≈ 10 m (or scale down, accept ambiguity)

#### Experimental Procedure

**Phase 1: Calibration**

1. **Generate known test signal:**
   - Place transmitting dipole at known location (e.g., 5 meters away, 30° from array boresight)
   - Transmit CW tone at 433 MHz, 1 W power
   - Calculate expected E and B fields at each sensor location using Friis equation

2. **Measure E-field with Rydberg sensors:**
   - Observe EIT signal on each photodiode
   - Record amplitude (proportional to E-field strength) and phase (from RF frequency modulation)
   - Verify linear response: vary transmitter power, check E-field scales correctly

3. **Measure B-field with loop antennas:**
   - Digitize voltage from each loop antenna's LNA output
   - Extract amplitude and phase using FFT or lock-in detection
   - Calibrate loop response: $V_{\text{loop}} = -j\omega \mu_0 N A B$ where $N$ = turns, $A$ = loop area

4. **Cross-validate E and B:**
   - In far-field, verify $E = cB$ (impedance of free space = 377 Ω)
   - If mismatch, check for near-field effects or calibration errors

**Phase 2: Direction Finding Experiments**

1. **Move transmitter to unknown location**
2. **Measure phase differences:**
   - Between Rydberg sensors: $\Delta\phi_E$ (from E-field array)
   - Between loop antennas: $\Delta\phi_B$ (from B-field array)
3. **Solve for direction of arrival (DOA):**
   - Use phase interferometry: $\theta = \arcsin(\Delta\phi \lambda / 2\pi d)$
   - Compare DOA from E-array vs B-array (should agree in far-field)
   - Averaging both gives improved accuracy
4. **Expected performance:**
   - Angular resolution: ~2-5° (limited by baseline length and SNR)
   - Ambiguity: ±180° (need additional sensors or constraints to resolve)

**Phase 3: Near-Field Vector Mapping**

1. **Place transmitter in near-field** (distance < λ)
2. **Measure E and B at all three positions simultaneously**
3. **Reconstruct vector fields:**
   - E-field: $\vec{E}(x,y,z)$ from Rydberg measurements
   - B-field: $\vec{B}(x,y,z)$ from loop measurements
4. **Analyze relationship:**
   - In near-field, $E/B \neq 377$ Ω (reactive vs radiative components)
   - Detect standing waves, multipath interference
   - Map field gradients: $\nabla \times \vec{E} = -\partial \vec{B}/\partial t$

**Phase 4: Beamforming and Nulling**

1. **Digital beamforming using E-field array:**
   - Apply complex weights $w_n e^{j\phi_n}$ to each Rydberg sensor output
   - Sum: $S_E = \sum_{n=1}^{3} w_n S_n e^{j\phi_n}$
   - Steer beam to maximize signal from desired direction, null others

2. **Cross-check with B-field array:**
   - Repeat beamforming using loop antenna signals
   - Compare beam patterns from E vs B arrays
   - Hybrid beamforming: combine both for improved SNR and robustness

### Quantum Advantages of Hybrid Arrays

#### SI-Traceable Absolute Calibration

Rydberg sensors provide **absolute E-field measurements** traceable to fundamental constants:
- Atomic transition frequencies known to 15+ digits (from atomic clocks)
- Autler-Townes splitting directly related to E-field via Stark effect
- No need for calibration against standard antennas

Use this to **calibrate loop antennas** in-situ:
1. Measure same field with both Rydberg sensor (absolute) and loop antenna (relative)
2. Determine loop's true effective area and gain without anechoic chamber
3. Now loop antenna becomes a calibrated standard for other measurements

#### Phase Coherence and Quantum Entanglement (Future)

Advanced concept: Use Rydberg atoms in **superposition states** across multiple sensors for quantum-enhanced sensing:
- Atoms in entangled states can beat classical signal-to-noise limits (Heisenberg limit vs shot noise limit)
- Distributed entanglement across array enables "quantum beamforming"
- Sensitivity improvement: factor of $\sqrt{N}$ for $N$ sensors (classical) → $N$ (quantum)

**Current status:** Lab demonstrations exist for single-point quantum sensing, but distributed quantum sensor arrays remain experimental (DARPA programs exploring this).

### Cost-Performance Trade-offs

| Array Type | Total Cost | E-Field Sensitivity | B-Field Sensitivity | Best For |
|------------|-----------|-------------------|-------------------|----------|
| **3× Loop Antennas Only** | $200-500 | N/A | 1-10 pT (magnetic) | DIY, education, B-field focus |
| **3× Ground-State Rb + 3× Loops** | $25k-35k | 1-10 mV/cm | 1-10 pT | Research labs, vector sensing |
| **3× Full Rydberg + 3× Loops** | $600k-1.5M | 1-10 µV/cm | 1-10 pT | Ultimate sensitivity, national labs |
| **1× Rydberg + 2× Loops (hybrid)** | $200k-250k | 1-10 µV/cm | 1-10 pT | Cost-optimized, proof-of-concept |

**Recommended starting point:** Build the 3× loop array first ($200-500), then upgrade one position to ground-state Rb sensor ($8k-10k) to explore hybrid concepts before committing to full Rydberg systems.

### Software and Signal Processing

For hybrid arrays, you'll need to:

1. **Synchronize data acquisition** from multiple heterogeneous sensors (optical photodiodes + RF amplifiers)
2. **Phase alignment** between different measurement modalities
3. **Vector field reconstruction** algorithms

**Example Python workflow:**

```python
import numpy as np
from scipy.fft import fft, fftfreq

# Synchronized sampling at 100 MS/s
t = np.linspace(0, 1e-3, 100000)  # 1 ms capture

# Rydberg sensor outputs (E-field, from photodiode signals)
E1 = photodiode_1_data  # Sensor 1
E2 = photodiode_2_data  # Sensor 2
E3 = photodiode_3_data  # Sensor 3

# Loop antenna outputs (B-field, from LNA signals)
B1 = loop_1_data  # Sensor 1
B2 = loop_2_data  # Sensor 2
B3 = loop_3_data  # Sensor 3

# Extract phase and amplitude at target frequency (e.g., 433 MHz)
def extract_signal(data, t, f_target=433e6):
    fft_data = fft(data)
    freqs = fftfreq(len(t), t[1]-t[0])
    idx = np.argmin(np.abs(freqs - f_target))
    amplitude = np.abs(fft_data[idx]) * 2 / len(data)
    phase = np.angle(fft_data[idx])
    return amplitude, phase

# Process all sensors
E1_amp, E1_phase = extract_signal(E1, t)
E2_amp, E2_phase = extract_signal(E2, t)
E3_amp, E3_phase = extract_signal(E3, t)

B1_amp, B1_phase = extract_signal(B1, t)
B2_amp, B2_phase = extract_signal(B2, t)
B3_amp, B3_phase = extract_signal(B3, t)

# Phase differences for DOA
delta_phi_E_12 = E1_phase - E2_phase
delta_phi_E_13 = E1_phase - E3_phase

delta_phi_B_12 = B1_phase - B2_phase
delta_phi_B_13 = B1_phase - B3_phase

# Solve for angle of arrival (simplified, assumes 1D)
wavelength = 3e8 / 433e6  # ~69 cm
baseline = 0.17  # 17 cm spacing

theta_E = np.arcsin(delta_phi_E_12 * wavelength / (2 * np.pi * baseline))
theta_B = np.arcsin(delta_phi_B_12 * wavelength / (2 * np.pi * baseline))

print(f"DOA from E-field array: {np.degrees(theta_E):.1f}°")
print(f"DOA from B-field array: {np.degrees(theta_B):.1f}°")
print(f"Average (hybrid): {np.degrees((theta_E + theta_B)/2):.1f}°")

# Verify far-field relationship E = cB (impedance check)
Z0 = 377  # Ohms, impedance of free space
for i in range(3):
    E_measured = [E1_amp, E2_amp, E3_amp][i]
    B_measured = [B1_amp, B2_amp, B3_amp][i]
    Z_measured = E_measured / (B_measured * 3e8)
    print(f"Sensor {i+1}: E/cB = {Z_measured:.0f} Ω (expect 377 Ω in far-field)")
```

### Research Directions

1. **Quantum-classical hybrid sensing:** Combine quantum (Rydberg) precision with classical (loop) robustness
2. **Self-calibrating arrays:** Use Rydberg's absolute calibration to continuously tune loop antenna responses
3. **AI-enhanced field reconstruction:** Machine learning to map sparse measurements (3 sensors) to full 3D field distribution
4. **Portable hybrid sensors:** Package co-located Rydberg cell + loop into handheld probe
5. **Time-domain applications:** Pulsed radar, transient detection, spread-spectrum signals

This hybrid approach represents a practical path from accessible DIY electronics (loops) to cutting-edge quantum sensing (Rydberg), allowing incremental development and learning at each stage.

---

## Summary of All Six Methods

All six approaches can successfully detect 7 MHz CW signals (amateur radio 40-meter band), with varying sensitivity, cost, and complexity:

| Method | Sensitivity | Cost | Complexity | Best For |
|--------|-------------|------|------------|----------|
| **1. Ground-State Hyperfine** | 1-10 mV/cm | $7k-$10k | Moderate | General RF sensing, research |
| **2. CPT** | 5-50 mV/cm | $600-$3k | Low | Portable sensors, education |
| **3. Faraday Rotation** | 3-30 mV/cm | $5k-$15k | Moderate | B-field sensing, HF/VHF ideal |
| **4. Sodium Thermal** | 0.1-1 V/cm | $500-$1.5k | Low | Education, proof-of-concept |
| **5. Atomic Clock Hack** | 10-100 mV/cm | $800-$2.5k | Low-Moderate | DIY, repurposing surplus |
| **6. NV Diamond** | 1-10 mV/cm | $12k-$50k | High | Near-field imaging, solid-state |

**Key Insight:** Even though 7 MHz is far below atomic transition frequencies (GHz range), all methods detect the signal via **second-order effects**: AC Stark shifts, light shifts, Zeeman modulation, or servo loop perturbations. With proper design, sensitivities in the mV/cm range are achievable - adequate for amateur radio reception within 50-100 km of transmitter.

---

## Performance Comparison Table

| Sensor Type | Cost | E-Field Sensitivity | Frequency Range | Complexity | Best For |
|-------------|------|-------------------|-----------------|------------|----------|
| **Full Rydberg (2-laser EIT)** | $200k-$500k | 1-10 µV/cm | DC - THz | Very High | Ultimate sensitivity, research |
| **Ground-State Hyperfine** | $7k-$10k | 1-10 mV/cm | DC - 10 GHz | Moderate | Practical RF sensing, education |
| **Coherent Population Trapping** | $2k-$5k | 5-50 mV/cm | DC - 10 GHz | Low | Portable sensors, field deployment |
| **Faraday Rotation** | $5k-$15k | 1-100 mV/cm (E), pT (B) | DC - GHz | Moderate | Magnetic sensing, imaging |
| **Sodium Thermal Beam** | $500-$2k | 0.1-1 V/cm | MHz - GHz | Low | Teaching labs, demos |
| **Surplus Rb Clock** | $1k-$3k | 10-100 mV/cm | MHz - 10 GHz | Low-Moderate | DIY projects, repurposing |
| **NV Diamond** | $10k-$50k | ~1 mV/cm (E), pT (B) | DC - GHz | High | Nanoscale sensing, solid-state |

---

## Recommended Starting Path

### For Researchers/Universities:
1. **Start with simulations** (continue work in this repository - free!)
2. **Build ground-state hyperfine sensor** ($10k budget)
   - Proves atomic sensing principles
   - Teaches laser stabilization, optics alignment, lock-in detection
   - Useful for many practical applications
3. **Partner with established labs** for Rydberg state experiments
   - Share equipment access
   - Collaborate on specific research questions

### For Hobbyists/Makers:
1. **Sodium vapor cell experiment** ($500-$2k)
   - Demonstrates atomic physics fundamentals
   - Safer than Rb/Cs (cheaper, less reactive)
   - Can detect strong RF fields (cell phones, WiFi routers)
2. **Surplus atomic clock modification** ($1k-$3k)
   - Pre-built, reliable hardware
   - Active online community (time-nuts mailing list)

### For Industry Applications:
1. **Evaluate sensitivity requirements**
   - If >10 mV/cm sufficient → ground-state or CPT sensors
   - If <1 mV/cm needed → partner with Rydberg specialists or NIST
2. **Prototype with commercial modules**
   - Several companies now offer Rydberg sensor products
   - Examples: Rydberg Technologies, quantum sensing startups
3. **Consider NV diamond** for solid-state applications
   - Better for harsh environments, miniaturization

---

## DIY Build Guide: Ground-State Rb Sensor

**Shopping List (Total: ~$8k):**

| Item | Supplier | Part Number | Cost |
|------|----------|-------------|------|
| Rb-87 vapor cell (75 mm) | Thorlabs | GC19075-RB87 | $2,000 |
| Used 780 nm ECDL laser | eBay/Surplus | Toptica DL100 (old model) | $3,000-$5,000 |
| Photodiode module | Thorlabs | DET36A/M | $500 |
| Cell heater | Thorlabs | GCH25-75 | $1,000 |
| Temperature controller | Thorlabs | TC300 | $1,500 |
| Optical mounts/posts | Thorlabs/Newport | Various (used) | $500 |
| RF signal generator | eBay | HP 8647A (used) | $500-$1,000 |

**Assembly Steps:**
1. Mount vapor cell in heater, stabilize at 50-60°C
2. Align laser beam through cell to photodiode
3. Tune laser to Rb D2 line (780 nm), lock to atomic transition
4. Apply RF field via nearby antenna or parallel-plate electrodes
5. Monitor photodiode signal with lock-in amplifier or oscilloscope
6. Calibrate: Plot signal vs. known RF field strength

**Estimated Build Time:** 2-4 weeks (with prior optics experience)

**Key Challenges:**
- Laser frequency stabilization (use saturated absorption spectroscopy)
- Temperature stability (±0.1°C needed)
- RF shielding (prevent pickup in detection electronics)
- Magnetic field cancellation (use Helmholtz coils or mu-metal shield)

---

## Connection to RAEFS Project Goals

These low-cost alternatives enable:

1. **Experimental validation** of simulations without massive capital investment
2. **Educational outreach** - students can build working quantum sensors
3. **Prototyping communication protocols** before scaling to Rydberg systems
4. **Niche applications** where moderate sensitivity suffices (EMC testing, spectrum monitoring)
5. **Technology development** - many innovations transfer to full Rydberg systems

The sensitivity gap (1000×) may seem large, but many applications don't require µV/cm performance. For 5G/6G band monitoring, WiFi characterization, or near-field RF imaging, mV/cm sensitivity is adequate and offers much faster development cycles.

---

## Phonon Science Applications

Applying the concepts of Rydberg atom sensors, Penning traps, and alternative bound-state systems to **phonon science** opens exciting possibilities for sensing, communication, and quantum simulation. Below is a structured approach to leverage these tools for phonon-related applications:

### **1. Rydberg Atom Sensors for Phonon Detection**

**Concept:**
Rydberg atoms are exquisitely sensitive to electric fields. Phonons in piezoelectric or polar materials (e.g., GaN, quartz) generate oscillating electric fields due to lattice vibrations. Rydberg sensors could detect these fields, enabling **non-invasive, high-resolution phonon spectroscopy**.

**Applications:**
- **Material Characterization:**
  Detect terahertz (THz) phonon modes in 2D materials (e.g., graphene, transition metal dichalcogenides) by measuring their electric field signatures.
- **Ultrafast Sensing:**
  Use Rydberg electrometers to monitor phonon dynamics in real time (e.g., coherent phonons in quantum materials).
- **Hybrid Systems:**
  Couple Rydberg sensors to phononic crystals or superconducting qubits to study phonon-mediated interactions.

**Challenges:**
- Phonon frequencies (THz range) may exceed Rydberg sensor bandwidths.
- Requires near-field coupling between the material and sensor.

**Computational Model:**
Simulate the interaction between a Rydberg atom and a phonon-induced electric field using time-dependent Schrödinger equations. Parameters:

```python
# Example pseudocode for phonon-Rydberg coupling
phonon_frequency = 1e12  # THz
rydberg_detuning = ...   # Adjust to match phonon frequency
electric_field = E0 * sin(2π * phonon_frequency * t)
```

### **2. Penning Traps for Phonon Simulation**

**Concept:**
Trapped ions in Penning traps exhibit collective motion analogous to phonons in crystals. By engineering their motion, you can simulate **phonon modes** or **quantum many-body physics**.

**Applications:**
- **Quantum Simulations:**
  Use trapped ions to mimic phonon-mediated superconductivity or spin-phonon coupling in lattices.
- **Phonon Engineering:**
  Design synthetic phonon spectra by tuning trap potentials (axial confinement for "acoustic" vs. "optical" modes).

**Example Setup:**
- Trap multiple ions in a Penning trap.
- Apply oscillating fields to excite collective vibrational modes (phonons).
- Measure mode frequencies and interactions.

**Simulation (Modified Penning Trap Code):**
Extend the Octave code to model **N-particle interactions** and analyze normal modes:

```matlab
% Add Coulomb interactions between trapped particles
for i = 1:N
    for j ≠ i
        F_coulomb = k_e * q^2 / |r_i - r_j|^3 * (r_i - r_j);
        F_total += F_coulomb;
    end
end
```

### **3. Quantum Dots as Phonon Probes**

**Concept:**
Electron-phonon coupling in quantum dots affects their electronic states. Use this to study phonon interactions or design **phonon lasers**.

**Applications:**
- **Phonon Spectroscopy:**
  Measure phonon density of states via quantum dot conductance fluctuations.
- **Thermal Management:**
  Engineer quantum dots to absorb/emit specific phonon modes for heat control in nanodevices.

**Modeling:**
Solve the **Holstein Hamiltonian** for electron-phonon coupling:

$\[
H = \epsilon d^\dagger d + \omega b^\dagger b + \lambda d^\dagger d (b + b^\dagger)
\]$

Where $\(d\)$ (electron) and $\(b\)$ (phonon) operators are coupled by strength $\(\lambda\)$.

See Appendix 1 below for detailed mathematical treatment.

### **4. Optical Lattices for Synthetic Phonons**

**Concept:**
Ultracold atoms in optical lattices can simulate phonon-like excitations by modulating lattice potentials.

**Applications:**
- **Bose-Hubbard Model:**
  Study phonon analogs (density waves) in superfluid-to-Mott insulator transitions.
- **Topological Phononics:**
  Engineer synthetic gauge fields to create chiral phonon edge states.

**Experiment Design:**
- Use a 2D optical lattice with tunable spacing.
- Introduce periodic modulation to excite phonon modes.
- Measure correlations via time-of-flight imaging.

### **5. Metamaterials for Phonon Control**

**Concept:**
Design **phononic metamaterials** (e.g., 3D-printed structures) to manipulate phonon propagation, inspired by electromagnetic metamaterials.

**Applications:**
- **Thermal Cloaking:**
  Redirect phonon flow to insulate hotspots in microelectronics.
- **Phonon Logic:**
  Create phononic circuits for mechanical computing.

**Simulation:**
Use finite-element analysis (FEA) to model phonon band structures in engineered materials.

### **6. Hybrid Systems for Phonon Communications**

**Concept:**
Combine Rydberg sensors, trapped ions, and phononic waveguides for **hybrid quantum communication**.

**Example Protocol:**
1. Encode information in phonons within a piezoelectric waveguide.
2. Transduce phonons to photons or electric fields.
3. Detect signals via Rydberg atoms or trapped ions.

**Challenges:**
- Efficient phonon-photon transduction at THz frequencies.
- Minimizing decoherence in hybrid interfaces.

### **Next Steps for Phonon Applications**

1. **Prioritize Simulations:**
   Start with computational models (e.g., phonon-Rydberg coupling in Julia/Python) to identify feasible experiments.
2. **Collaborate with Experimentalists:**
   Partner with labs working on cold atoms, quantum dots, or phononic crystals.
3. **Focus on THz Technologies:**
   Target applications in 6G communications (THz frequencies align with phonon modes in many materials).

By integrating these approaches, you can pioneer new methods to control, sense, and utilize phonons—bridging atomic-scale physics with macroscopic material properties.

---

## Holstein Hamiltonian Model

### Introduction to Phonon Science

Phonon science is the study of phonons, which are quantized modes of vibrational energy in a solid material's atomic lattice. Think of a crystal as a network of atoms connected by springs; when these atoms vibrate collectively (due to thermal energy or external stimuli), the vibrations propagate as waves. Phonons are the particle-like quanta of these waves, analogous to how photons are quanta of light.

**Key concepts:**
- **Types of Phonons**: Acoustic phonons (low-frequency, sound-like waves) and optical phonons (higher-frequency, where adjacent atoms move oppositely).
- **Importance**: Phonons play a critical role in thermal conductivity, electrical resistance (via electron-phonon scattering), superconductivity, and material properties like specific heat. In quantum technologies, they enable phonon-based computing, sensing, and communication.
- **Applications**: From everyday materials (e.g., heat management in electronics) to advanced fields like topological phononics (protecting vibrations against defects) and phonon lasers (coherent phonon sources).

The provided context explores advanced applications of quantum tools (e.g., Rydberg atoms, Penning traps) to phonon science, focusing on sensing, simulation, and control. It also delves into the Holstein model, a key Hamiltonian for understanding electron-phonon interactions, which is central to phenomena like polarons (electrons "dressed" by phonon clouds).

### Octave Program for Holstein Model

The program (see **[holstein_model.m](holstein_model.m)**):

1. **Computes the energy shift** due to electron-phonon interaction.
2. **Simulates phonon occupation probabilities** for different coupling strengths.
3. **Plots the energy shift** as a function of coupling strength.

#### **What This Code Does**

1. **Energy Shift Plot:**
   - Computes the renormalized electron energy $\( \tilde{\epsilon} = \epsilon - \lambda^2 / \omega \)$.
   - Plots the shift as a function of $\( \lambda \)$.

2. **Phonon Occupation Probability:**
   - Computes the phonon probability distribution for different values of $\( \lambda \)$.
   - Uses the **Poisson-like distribution** from polaron theory:
     $\[
     P(n) = e^{-g^2} \frac{g^{2n}}{n!}
     \]$
   - Plots the probability of different phonon occupation numbers for **three** coupling strengths.

#### **Expected Output**
- **Plot 1:** **Energy shift vs. $\( \lambda \)$** – shows how increasing electron-phonon coupling lowers the electron energy.
- **Plot 2:** **Phonon number probabilities** for different $\( \lambda \)$ values – shows how stronger coupling increases phonon excitation.

![image](https://github.com/user-attachments/assets/bc094d77-0bcd-45b9-9d4c-e5a84c1bcf4d)

### Appendix 1: Mathematical Treatment

The Holstein Hamiltonian describes the interaction between electrons and phonons and is given by:

$\[
H = \epsilon d^\dagger d + \omega b^\dagger b + \lambda d^\dagger d (b + b^\dagger)
\]$

where:
- $\( d^\dagger, d \)$ are electron creation and annihilation operators,
- $\( b^\dagger, b \)$ are phonon creation and annihilation operators,
- $\( \epsilon \)$ is the electronic energy,
- $\( \omega \)$ is the phonon frequency,
- $\( \lambda \)$ is the electron-phonon coupling strength.

#### **Step 1: Diagonalization via the Lang-Firsov Transformation**

To solve this problem, we use the **Lang-Firsov transformation**, which introduces a unitary transformation to decouple the electron-phonon interaction.

Define the unitary transformation:

$\[
U = e^{g d^\dagger d (b^\dagger - b)}
\]$

where $\( g = \frac{\lambda}{\omega} \)$ is a dimensionless electron-phonon coupling parameter.

Applying $\( U \)$ to the Hamiltonian:

$\[
H' = U H U^\dagger
\]$

Expanding each term under transformation:

1. The phonon term transforms as:

   $\[
   U b U^\dagger = b - g d^\dagger d
   \]$

   $\[
   U b^\dagger U^\dagger = b^\dagger - g d^\dagger d
   \]$

   This shifts the phonon operators.

2. The electron number operator remains unchanged:

   $\[
   U d^\dagger d U^\dagger = d^\dagger d
   \]$

Using these, the transformed Hamiltonian becomes:

$\[
H' = \epsilon d^\dagger d + \omega b^\dagger b - \frac{\lambda^2}{\omega} d^\dagger d
\]$

Thus, we obtain:

$\[
H' = (\epsilon - \frac{\lambda^2}{\omega}) d^\dagger d + \omega b^\dagger b
\]$

#### **Step 2: Interpretation**

1. The **electronic energy** shifts to an effective value:

   $\[
   \tilde{\epsilon} = \epsilon - \frac{\lambda^2}{\omega}
   \]$

   This is known as the **polaron shift**, which lowers the energy due to the electron-phonon coupling.

2. The **phonon energy** remains unchanged, meaning that the phonon bath is not directly modified but its interaction with electrons has been accounted for.

3. The resulting Hamiltonian is now **diagonal**, meaning the system can be interpreted as an electron that carries a phonon cloud, forming a **polaron**.

#### **Step 3: Eigenstates**

Since the transformed Hamiltonian is diagonal, the eigenstates are simple products of electron occupation states $\( |0\rangle, |1\rangle \)$ and phonon number states $\( |n\rangle \)$:

$\[
H' |n, 0\rangle = n\omega |n, 0\rangle
\]$

$\[
H' |n, 1\rangle = (\tilde{\epsilon} + n\omega) |n, 1\rangle
\]$

where $\( |n, 0\rangle \)$ represents $\( n \)$ phonons with no electron, and $\( |n, 1\rangle \)$ represents $\( n \)$ phonons with an electron.

#### **Conclusion**

The Holstein Hamiltonian describes an electron dressed by a phonon cloud, leading to a **polaron**. The main result is the renormalization of the electron energy:

$\[
\tilde{\epsilon} = \epsilon - \frac{\lambda^2}{\omega}
\]$

This captures the essence of electron-phonon interactions in the Holstein model.

### Numerical Diagonalization

While the Lang-Firsov transformation provides an exact analytical solution for the single-site Holstein model (decoupling electrons and phonons into a diagonal form), numerical diagonalization is useful for verification, especially in finite-dimensional approximations or extensions to multi-site models (e.g., for studying polaron transport). It also helps quantify truncation errors in the phonon basis.

#### Step-by-Step Reasoning and Method

1. **Hamiltonian Setup**: Recall the Holstein Hamiltonian:
   \[
   H = \epsilon \, d^\dagger d + \omega \, b^\dagger b + \lambda \, d^\dagger d (b + b^\dagger)
   \]
   We focus on the occupied electron sector ( \( d^\dagger d = 1 \) ), as the unoccupied sector ( \( d^\dagger d = 0 \) ) is simply the harmonic oscillator with energies \( \omega k \) ( \( k = 0, 1, \dots \) ). In this sector:
   \[
   H_\text{occ} = \epsilon + \omega \, b^\dagger b + \lambda (b + b^\dagger)
   \]
   This describes an electron coupled to a displaced harmonic oscillator.

2. **Basis Truncation**: To numerically solve, truncate the phonon Hilbert space to \( k = 0 \) to \( N \) (e.g., \( N = 20 \)). The basis states are \( |k\rangle \) (phonon number states). The matrix dimension is \( N+1 \).

3. **Matrix Construction**: Build the Hamiltonian matrix \( H \) in this basis:
   - Diagonal elements: \( H_{kk} = \epsilon + \omega k \)
   - Off-diagonal elements:
     - Superdiagonal \( H_{k, k+1} = \lambda \sqrt{k+1} \)
     - Subdiagonal \( H_{k+1, k} = \lambda \sqrt{k+1} \)
   This results in a symmetric tridiagonal matrix, efficient for diagonalization.

4. **Diagonalization**: Use eigenvalue decomposition (e.g., `scipy.linalg.eigh` for symmetric matrices) to find eigenvalues \( E_i \) and eigenvectors \( \psi_i \). The ground state energy is the minimum eigenvalue \( E_\text{gs} \), and the ground state wavefunction \( \psi_\text{gs} \) gives phonon occupation probabilities \( P(k) = |\psi_\text{gs, k}|^2 \).

5. **Comparison to Analytical Solution**:
   - Analytical ground state energy (from Lang-Firsov): \( \tilde{\epsilon} = \epsilon - \frac{\lambda^2}{\omega} \)
   - Analytical probabilities: Poisson distribution \( P(n) = e^{-g^2} \frac{g^{2n}}{n!} \), where \( g = \frac{\lambda}{\omega} \).
   - Compute differences to verify: Numerical \( E_\text{gs} \) should match \( \tilde{\epsilon} \), and numerical \( P(k) \) should match the Poisson form. Discrepancies arise from basis truncation (tail probabilities beyond \( N \)); larger \( N \) reduces error.

6. **Implementation and Results**: The Python code (see **[holstein_numerical.py](holstein_numerical.py)**) computes the energy shift over \( \lambda \in [0, 2] \), compares numerical vs. analytical ground states, and checks phonon probabilities for specific \( \lambda \) values (0.5, 1.0, 1.5). With \( N=20 \):
   - Maximum energy difference across all \( \lambda \): ~2.64 × 10⁻⁸ (numerical precision/truncation error).
   - For probabilities, maximum differences are on the order of 10⁻¹² to 10⁻¹⁶, confirming near-exact match.
   - Sample energy shifts (analytical vs. numerical):
     - \( \lambda = 0.00 \): 1.00 vs. 1.00
     - \( \lambda = 1.01 \): -0.02 vs. -0.02
     - \( \lambda = 2.00 \): -3.00 vs. -3.00
   - For \( \lambda = 1.5 \) (g=1.5, mean phonons ~2.25), first 5 probabilities (analytical/numerical identical within precision): [0.1054, 0.2371, 0.2668, 0.2001, 0.1126].

This verifies the transformation: the numerical approach reproduces the polaron shift and displaced oscillator statistics exactly for sufficient \( N \).

#### Connection Back to Phonon Science Applications

This Holstein model is foundational for understanding how phonons interact with electrons in materials, directly relevant to the earlier sections (e.g., quantum dots as phonon probes, or simulating phonon-mediated effects in Penning traps). In broader phonon science, polarons explain charge transport in organic semiconductors or high-temperature superconductors. Extending this numerical approach to multi-site Holstein models (e.g., using tensor networks) could simulate phonon effects in 1D chains, aligning with phononic metamaterials or hybrid quantum systems.

---

## Communications and Sensing Applications

This section outlines how the theoretical frameworks and simulations in this repository connect to practical communications and sensing applications.

### Potential Communication Protocols

**1. Amplitude Modulation via E-field Strength**
- Encode binary/analog data by varying the amplitude of applied electric fields
- Rydberg atoms detect field strength through EIT signal shifts
- Bandwidth: DC - GHz (depending on Rydberg state chosen)

**2. Frequency-Division Multiplexing**
- Use different RF frequencies to encode multiple channels
- Autler-Townes splitting separates channels in frequency domain
- Each Rydberg transition can serve as a distinct channel

**3. Quantum-Enhanced Detection**
- Leverage quantum coherence for sub-shot-noise sensitivity
- Potential for secure communication via quantum state encoding
- Phonon-photon-atom hybrid transduction

### Sensing Capabilities (Theoretical)

**Electric Field Sensing:**
- **Sensitivity**: μV/cm to mV/cm (depending on implementation)
- **Frequency range**: DC to THz
- **Spatial resolution**: λ/2 (wavelength limited) to sub-wavelength with near-field techniques

**Phonon Sensing (via E-field coupling):**
- Detect THz phonon modes in piezoelectric materials
- Monitor coherent phonon dynamics in quantum materials
- Non-invasive thermal characterization

**Potential Applications:**
- 5G/6G spectrum monitoring
- Non-invasive medical imaging (THz sensing)
- Quantum computing readout/control
- Materials characterization
- Electromagnetic compatibility (EMC) testing

### Current Limitations

- No experimental demonstration yet (simulation phase)
- Bandwidth limitations from Rydberg state lifetimes
- Decoherence from environmental noise
- Scalability challenges for practical deployment
- High cost of laboratory implementation

---

## Validation and Results

### Simulation Validation

All simulations in this repository have been validated against known analytical solutions and published literature:

**Penning Trap Simulations:**
- ✓ **3D confinement verified**: Particle remains bounded in all three dimensions
- ✓ **Energy conservation**: Total energy drift < 0.01% over simulation time
- ✓ **Frequency ratios**: Match theoretical predictions for epitrochoidal motion
- ✓ **Motion patterns**: Reproduce characteristic helical and flower-like trajectories
- **Reference**: Compared against equations from [Wikipedia: Penning Trap](https://en.wikipedia.org/wiki/Penning_trap)

**Holstein Hamiltonian:**
- ✓ **Analytical match**: Numerical diagonalization agrees with Lang-Firsov transformation (error < 10⁻⁷)
- ✓ **Polaron energy shift**: Verified formula $\tilde{\epsilon} = \epsilon - \lambda^2/\omega$
- ✓ **Phonon statistics**: Poisson distribution confirmed for all coupling strengths tested
- ✓ **Convergence**: Results stable for phonon basis truncation N ≥ 20
- **References**: Results consistent with textbook treatments (Mahan, "Many-Particle Physics")

### Expected vs. Actual Outputs

| Simulation | Expected Behavior | Observed Result | Status |
|------------|------------------|-----------------|--------|
| 3D Penning Trap | Helical trajectory, stable confinement | Matches expected | ✓ Pass |
| Epitrochoid | Flower pattern, frequency ratio ~8:1 | Ratio achieved by parameter tuning | ✓ Pass |
| Holstein Energy | Linear decrease with λ² | $\tilde{\epsilon}$ follows prediction | ✓ Pass |
| Phonon Occupation | Poisson distribution | Matches analytical form | ✓ Pass |

### Known Issues and Accuracy

**Numerical Precision:**
- Floating-point errors accumulate over long simulations (>10⁶ steps)
- Recommendation: Use adaptive time-stepping for critical applications

**Truncation Effects:**
- Holstein model: Phonon basis truncation negligible for λ/ω < 2
- For strong coupling (λ/ω > 2), increase N_phonons to 50+

**Physical Validity:**
- Simulations assume ideal conditions (no damping, perfect fields)
- Real experiments would include thermal noise, field inhomogeneities
- Quantitative predictions should be treated as upper bounds on performance

### Future Experimental Validation

To validate these models experimentally, the following tests are proposed:

1. **Penning Trap**: Build a tabletop electron trap (cost ~$10k) to verify trajectories
2. **Holstein Model**: Measure polaron effects in quantum dot systems (requires university facilities)
3. **RAEFS**: Full Rydberg atom setup (cost $200k+, requires specialized expertise)

---

## Roadmap and Next Steps

### Short-term Goals (0-6 months)

1. **Enhance Simulations**
   - [ ] Add damping/decoherence to Penning trap models
   - [ ] Implement multi-site Holstein model for phonon transport
   - [ ] Develop time-dependent Schrödinger equation solver for Rydberg-phonon coupling
   - [ ] Create visualization tools for 3D trajectory analysis

2. **Documentation and Community**
   - [ ] Write tutorial notebooks (Jupyter) for each simulation
   - [ ] Create video walkthroughs of key concepts
   - [ ] Establish discussion forum for collaborators
   - [ ] Develop troubleshooting guide for common issues

3. **Theoretical Extensions**
   - [ ] Analyze signal-to-noise ratios for communication protocols
   - [ ] Model realistic decoherence sources
   - [ ] Investigate error correction strategies
   - [ ] Benchmark against existing sensor technologies

### Medium-term Goals (6-18 months)

1. **Prototype Hardware Design**
   - [ ] Design low-cost Penning trap demonstrator ($5k-$10k budget)
   - [ ] Source used laser equipment for Rb spectroscopy
   - [ ] Partner with university labs for equipment sharing
   - [ ] Develop open-source control software

2. **Experimental Validation**
   - [ ] Build Penning trap and validate simulations
   - [ ] Perform basic Rb spectroscopy (if funding available)
   - [ ] Characterize noise sources experimentally
   - [ ] Publish validation results

3. **Application Development**
   - [ ] Prototype RF field sensing demonstration
   - [ ] Test phonon detection concept on piezoelectric materials
   - [ ] Develop modulation/demodulation schemes
   - [ ] Benchmark communication bandwidth

### Long-term Vision (18+ months)

1. **Full RAEFS Implementation**
   - [ ] Secure funding for complete Rydberg atom setup ($200k+)
   - [ ] Assemble research team (expertise in AMO physics, optics, electronics)
   - [ ] Commission full experimental apparatus
   - [ ] Demonstrate E-field sensing and communication

2. **Commercialization Pathways**
   - [ ] Identify niche applications (e.g., EMC testing, medical imaging)
   - [ ] Patent novel techniques
   - [ ] Develop portable sensor prototype
   - [ ] Engage with industry partners

3. **Scientific Contributions**
   - [ ] Publish results in peer-reviewed journals
   - [ ] Present at conferences (APS, OSA, IEEE)
   - [ ] Release open-source hardware/software designs
   - [ ] Train students and early-career researchers

### How You Can Contribute

We welcome contributions in the following areas:

- **Code**: Improve simulations, fix bugs, add features
- **Documentation**: Write tutorials, improve README, create examples
- **Theory**: Extend models, validate physics, propose new applications
- **Experiments**: Share lab experience, provide equipment recommendations
- **Funding**: Help identify grants, sponsors, or collaboration opportunities

See [Contributing](#contributing) section below for details.

---

## References

### Wikipedia References
- [Rydberg atom](https://en.wikipedia.org/wiki/Rydberg_atom)
- [Tunable laser](https://en.wikipedia.org/wiki/Tunable_laser)
- [Penning trap](https://en.wikipedia.org/wiki/Penning_trap)

### Key Scientific Papers (Recommended Reading)

**Rydberg Atom E-field Sensors:**
- Holloway et al., "Broadband Rydberg Atom-Based Electric-Field Probe for SI-Traceable, Self-Calibrated Measurements," IEEE Trans. Antennas Propag. (2014)
- Sedlacek et al., "Microwave electrometry with Rydberg atoms in a vapour cell using bright atomic resonances," Nature Physics (2012)

**Penning Traps:**
- Brown & Gabrielse, "Geonium theory: Physics of a single electron or ion in a Penning trap," Rev. Mod. Phys. (1986)

**Holstein Model and Polarons:**
- Mahan, "Many-Particle Physics," 3rd Edition (2000)
- Alexandrov & Devreese, "Advances in Polaron Physics" (2010)

**Phonon Science:**
- Maldovan, "Sound and heat revolutions in phononics," Nature (2013)
- Chen et al., "Non-Hermitian topological photonics," Nature Photonics (2021)

---

## Additional Resources

### Included Documents
- **[Rydberg_Atom_Electric_Field_Sensors_for_Communications_and_Sensing.pdf](Rydberg_Atom_Electric_Field_Sensors_for_Communications_and_Sensing.pdf)** - Comprehensive background document covering fundamental theory, experimental techniques, and state-of-the-art applications

### Simulation Files
- **[penning_trap_3d.m](penning_trap_3d.m)** - 3D Penning trap particle trajectory simulation
- **[penning_trap_epitrochoid.m](penning_trap_epitrochoid.m)** - Epitrochoidal motion analysis
- **[holstein_model.m](holstein_model.m)** - Holstein Hamiltonian polaron energy and phonon statistics
- **[holstein_numerical.py](holstein_numerical.py)** - Numerical diagonalization and verification

### Educational Videos

**"Rydberg Atom Based Sensors" - NIST Distinguished Lecture by Dr. Chris Holloway**
- **Video**: [CECS Distinguished Speaker Series](https://www.youtube.com/watch?v=VIDEO_ID&t=574s) (~1 hour, Nov 2021)
- **Speaker**: Dr. Chris Holloway, NIST Boulder (National Institute of Standards and Technology)

**Key topics covered:**
- **NIST's role in metrology** - Maintaining national/international measurement standards for fair commerce and scientific research
- **Evolution of SI units** - The 2018 shift from physical artifacts (meter sticks, kilogram prototypes) to definitions based on fundamental constants of nature (e.g., Planck's constant)
- **Rydberg atom-based E-field sensors** - Core technical content on using highly excited alkali atoms (rubidium) in vapor cells for electromagnetic field measurement
- **Electromagnetically Induced Transparency (EIT)** - Laser-based optical readout technique enabling SI-traceable, self-calibrated measurements
- **Advantages over traditional probes** - No field perturbation, broader bandwidth, smaller size, direct traceability to fundamental constants (~10% accuracy improvement)
- **Historical development** - NIST's foundational work (2010), DARPA funding (2011+), and growth to 15-20 companies developing quantum sensor technologies
- **Student opportunities** - NIST PREP (graduate) and SURF (undergraduate summer) research programs

**Why this matters for RAEFS:**
This lecture provides essential background on the real-world implementation and standardization of the exact technology this repository aims to simulate. Dr. Holloway's group at NIST pioneered the SI-traceable Rydberg sensor approach referenced throughout this project. The talk bridges fundamental atomic physics with practical metrology applications, offering context for why Rydberg sensors represent a paradigm shift from classical metal antennas.

**Recommended viewing sequence:**
- Start at ~12:00 for core Rydberg sensor physics
- Review full talk for metrology context and historical perspective
- Complements the included PDF documentation with visual explanations and experimental demonstrations

### External Resources
- **NIST Rydberg Group**: [https://www.nist.gov/pml/electromagnetics/](https://www.nist.gov/pml/electromagnetics/)
- **Toptica Photonics** (laser vendors): [https://www.toptica.com/](https://www.toptica.com/)
- **Thorlabs** (optics/vapor cells): [https://www.thorlabs.com/](https://www.thorlabs.com/)

---

## Contributing

We welcome contributions from the community! Here's how you can help:

### Ways to Contribute

1. **Report Issues**
   - Bug reports for simulation code
   - Documentation errors or unclear sections
   - Suggestions for improvements

2. **Code Contributions**
   - Optimize existing simulations
   - Add new features (e.g., visualization, analysis tools)
   - Port code to other languages (Julia, C++, etc.)
   - Improve code documentation and comments

3. **Documentation**
   - Write tutorials or how-to guides
   - Create example use cases
   - Improve mathematical explanations
   - Translate documentation

4. **Research Contributions**
   - Validate simulations against experiments
   - Extend theoretical models
   - Propose new applications
   - Share experimental data

### Contribution Process

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Make your changes
4. Test your changes thoroughly
5. Commit with clear messages (`git commit -m 'Add feature X'`)
6. Push to your fork (`git push origin feature/your-feature`)
7. Open a Pull Request with detailed description

### Code Standards

- **Octave/MATLAB**: Follow standard naming conventions, add comments for complex sections
- **Python**: Follow PEP 8 style guide, include docstrings
- **Documentation**: Use clear, concise language; include examples where appropriate

### Questions or Ideas?

- Open an issue on GitHub for discussions
- Tag issues appropriately (bug, enhancement, question, etc.)
- Be respectful and constructive in all interactions

---

## License

This project is released under the **MIT License**.

```
MIT License

Copyright (c) 2025 RAEFS Project Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

### Attribution

If you use this code or methodology in your research, please cite:

```
RAEFS Project (2025). "Rydberg Atom Electric Field Sensors: Simulations and Applications"
GitHub repository: [repository URL]
```

### Third-Party Resources

- Simulation physics based on established literature (see References section)
- No third-party libraries with restrictive licenses are used
- All external references are cited appropriately

---

**Acknowledgments**: This project draws inspiration from the pioneering work of research groups at NIST, MIT, and other institutions advancing Rydberg atom physics and quantum sensing. We thank the open-source community for tools like GNU Octave, Python, NumPy, and SciPy that make this research accessible.

**Disclaimer**: This is a research project. Simulations are provided for educational and scientific purposes. No guarantees are made regarding accuracy for production use. Always validate against experimental data before drawing conclusions.

---

*Last Updated: January 2026*
