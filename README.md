
# Darktag

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A Python package for assigning stellar mass to dark matter particles in dark matter-only simulations. The primary goal is to accurately reproduce the sizes and stellar mass distributions of dwarf galaxies using advanced particle tagging methods.

## Features

- **Angular Momentum Tagging**: Associates stellar mass with dark matter particles using their angular momenta
- **Spatial Tagging**: Distributes stellar mass across the galaxy based on a Plummer Profile
- **Binding Energy Tagging**: Associates stellar mass with dark matter particles using their binding energies
- **Centralized Configuration**: JSON-based configuration system for easy path management
- **HALO Catalog Support**: Compatible with AHF and HOP halo catalogues

## Installation

### Full Installation (Recommended for Astrophysics Work)

**Required for stellar mass growth histories:**

```bash
# Install core package
pip install darktag

# Install darklight from Git (latest development version)
pip install darklight @ git+https://github.com/stacykim/darklight.git@main#egg=darklight
```

### Basic Installation (Core Functionality Only)

```bash
# Core functionality without darklight
pip install darktag
```

**Important:** The darklight package on PyPI is a different package and not compatible with this workflow. Always install darklight from Git for the correct stellar mass growth history functionality.

### Manual Installation (Troubleshooting)

If automatic installation fails, install dependencies manually:

```bash
# Install core astrophysics packages from PyPI
pip install pynbody tangos

# Install darklight manually from Git (if needed)
pip install darklight @ git+https://github.com/stacykim/darklight.git@main#egg=darklight
```

### Why Install darklight from Git?

**Git-based installation is required because:**
- **Latest features**: Access to the most recent updates and bug fixes
- **Active development**: Darklight is under active development with frequent improvements
- **Better compatibility**: Ensures compatibility with recent simulation formats
- **Different package**: The darklight package on PyPI is a completely different package, not the astrophysics library
- **Correct functionality**: Only the Git version provides the stellar mass growth history algorithms needed for particle tagging

### Verify Installation

```bash
python -c "import darktag; print('✓ Darktag package installed successfully!')"
```

## Manual Installation

For manual installation or troubleshooting, see [INSTALL.md](INSTALL.md) for detailed instructions.

### Dependencies

#### Core Dependencies
- **numpy** >= 1.20.0: Numerical computations
- **pandas** >= 1.3.0: Data manipulation  
- **matplotlib** >= 3.5.0: Basic plotting
- **seaborn** >= 0.11.0: Statistical visualization
- **scipy** >= 1.7.0: Scientific computing
- **scikit-learn** >= 0.24.0: Machine learning utilities

#### Astrophysics Dependencies 
- **pynbody** >= 2.1: Astrophysical simulation analysis (installed automatically)
- **tangos** >= 1.10.0: Simulation database management (installed automatically)
- **darklight**: Generates stellar mass growth histories (install with `[darklight]` extra)

## Quick Start

```python
import tangos
import darktag as dtag
from config import config

# Initialize tangos database
tangos.core.init_db('your_simulation.db')
DMO_database = tangos.get_simulation('your_simulation_name')

# Perform particle tagging (uses config paths automatically)
df_tagged_particles = dtag.tag_particles(
    DMO_database, 
    tagging_method='angular momentum',
    free_param_val=0.001
)

# Calculate half-mass radii
df_half_mass_tagged = dtag.calculate_rhalf(
    DMO_database, 
    df_tagged_particles
)
```

## Configuration

The package uses a simple JSON configuration system. Update paths in `config.json`:

```json
{
    "paths": {
        "tangos_path": "/path/to/your/tangos/databases/",
        "pynbody_path": "/path/to/your/pynbody/data/",
        "manual_halonum_path": "",
        "manual_mstar_path": ""
    },
    "tagging": {
        "method": "angular_momentum",
        "ftag": 0.01
    },
    "darklight": {
        "n": 500,
        "DMO_OR_HYDRO": "DMO",
        "poccupied": "all"
    }
}
```

### Accessing Configuration

```python
from config import config

# Get specific paths
tangos_path = config.get_path('tangos_path')
pynbody_path = config.get_path('pynbody_path')

# Get configuration values
ftag = config.get('tagging', 'ftag')
method = config.get('tagging', 'method')

# Get all paths
all_paths = config.get_all_paths()
```

Update the paths to point to your simulation data and tangos databases.

## Usage

### Available Tagging Methods

1. **Angular Momentum**: `tagging_method='angular momentum'`
2. **Angular Momentum Recursive**: `tagging_method='angular momentum recursive'`  
3. **Spatial**: `tagging_method='spatial'`

### Advanced Configuration

The package supports various parameters for fine-tuning:

- `free_param_val`: Free parameter for tagging method (default: 0.01)
- `include_mergers`: Whether to include merger events (default: True)
- `halonumber`: Specific halo number to analyze (default: 1)
- `path_to_particle_data`: Path to particle data (uses config if None)

### Complete Example

```python
import tangos
import darktag as dtag
from config import config

# Initialize tangos database
tangos.core.init_db('your_simulation.db')
DMO_database = tangos.get_simulation('your_simulation_name')

# Perform particle tagging with custom parameters
df_tagged_particles = dtag.tag_particles(
    DMO_database, 
    tagging_method='angular momentum',
    free_param_val=0.001,
    include_mergers=True,
    halonumber=1
)

# Calculate half-mass radii
df_half_mass_tagged = dtag.calculate_rhalf(
    DMO_database, 
    df_tagged_particles
)
```

### Available Tagging Methods

1. **Angular Momentum**: `tagging_method='angular momentum'`
2. **Spatial**: `tagging_method='spatial'`
3. **Binding Energy**: `tagging_method='binding energy'`

### Advanced Configuration

The package supports various parameters for fine-tuning:

- `free_param_val`: Free parameter for tagging method (default: 0.01)
- `include_mergers`: Whether to include merger events (default: True)
- `halonumber`: Specific halo number to analyze (default: 1)

## Examples

See the `examples/` directory for complete tutorial scripts:

- `tutorial_1_getting_started.py`: Basic particle tagging workflow
- `tutorial_2_plotting_stellar_mass_distributions.py`: Plotting and analysis

Run the example:
```bash
cd examples
python tutorial_1_getting_started.py
```

## Data Requirements

The tagging methods require:
- **Tangos databases** with merger trees
- **Pynbody particle data** 
- **AHF or HOP halo catalogues**

## Testing

Run the test suite to verify installation:

```bash
python test.py
```

## Examples

See the `examples/` directory for complete tutorial scripts:

- `tutorial_1_getting_started.py`: Basic particle tagging workflow
- `tutorial_2_plotting_stellar_mass_distributions.py`: Plotting and analysis
- `config_demo.py`: Configuration system demonstration

Run the examples:
```bash
cd examples
python tutorial_1_getting_started.py
```

## Performance Considerations

- **Memory usage**: Large simulations may require substantial RAM
- **Computational time**: Angular momentum tagging is typically faster than binding energy methods
- **Parallel processing**: Use appropriate HPC resources for large simulation batches
- **Storage**: Ensure adequate disk space for intermediate particle storage files

## Troubleshooting

### Common Issues

1. **Path not found**: Check `config.json` paths are correct and accessible
2. **Database errors**: Ensure tangos_path points to valid .db files
3. **Particle data missing**: Verify pynbody_path contains simulation outputs
4. **Permission errors**: Make sure paths are accessible with current permissions
5. **Memory errors**: Reduce simulation size or use a machine with more RAM

### Debug Mode

Add debug prints to verify configuration:
```python
from config import config
print(f"Using tangos path: {config.get_path('tangos_path')}")
print(f"Using pynbody path: {config.get_path('pynbody_path')}")
```

## Contributing

1. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Citation

If you use this package in your research, please cite:

```bibtex
@software{darktag,
  title={Darktag: Particle Tagging for Dark Matter Simulations},
  author={Nigudkar, Sushanta},
  year={2024},
  url={https://github.com/nsushantnigudkar/darktag}
}
```

## Support

For questions, issues, or contributions, please open an issue on the GitHub repository.
