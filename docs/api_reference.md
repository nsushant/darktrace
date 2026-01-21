# API Reference

This document provides detailed API documentation for the Darktrace package.

## Core Functions

### `tag_particles`

**Location**: `darktrace.tagging.tagging_wrapper_func`

```python
def tag_particles(DMO_database, 
                path_to_particle_data=None, 
                tagging_method='angular momentum', 
                free_param_val=0.01, 
                include_mergers=True, 
                halonumber=1) -> pd.DataFrame
```

Performs particle tagging using the specified method.

**Parameters**:
- `DMO_database` (tangos simulation): Tangos simulation database object
- `path_to_particle_data` (str, optional): Path to particle data. Uses config if None
- `tagging_method` (str): Tagging method. Options:
  - `'angular momentum'` - Standard angular momentum tagging
  - `'angular momentum recursive'` - Recursive tagging with merger handling
  - `'spatial'` - Position-based tagging
- `free_param_val` (float): Free parameter for tagging fraction (default: 0.01)
- `include_mergers` (bool): Whether to include merger events (default: True)
- `halonumber` (int): Halo number to analyze (default: 1)

**Returns**:
- `pd.DataFrame`: DataFrame containing tagged particles with their properties

**Example**:
```python
import darktrace as dtrace
from config import config

df_tagged = dtrace.tag_particles(
    DMO_database,
    tagging_method='angular momentum',
    free_param_val=0.001,
    include_mergers=True
)
```

---

### `calculate_rhalf`

**Location**: `darktrace.tagging.tagging_wrapper_func`

```python
def calculate_rhalf(DMOsim, 
                   data_particles_tagged, 
                   pynbody_path=None, 
                   path_AHF_halonums=None, 
                   from_dataframe=True, 
                   from_file=False) -> pd.DataFrame
```

Calculates half-mass radii from tagged particles.

**Parameters**:
- `DMOsim` (tangos simulation): Simulation object
- `data_particles_tagged` (pd.DataFrame or str): Tagged particles data or file path
- `pynbody_path` (str, optional): Path to particle data. Uses config if None
- `path_AHF_halonums` (str, optional): Path to AHF halo numbers file
- `from_dataframe` (bool): Whether input is DataFrame (default: True)
- `from_file` (bool): Whether input is file path (default: False)

**Returns**:
- `pd.DataFrame`: DataFrame containing half-mass radius calculations

---

## Tagging Methods

### Angular Momentum Tagging

#### `angmom_tag_over_full_sim`

**Location**: `darktrace.tagging.angular_momentum_tagging`

```python
def angmom_tag_over_full_sim(DMOsim, 
                           halonumber=1, 
                           free_param_value=0.01, 
                           particle_storage_filename=None, 
                           mergers=True) -> pd.DataFrame
```

Performs angular momentum based tagging over full simulation.

**Parameters**:
- `DMOsim` (tangos simulation): Simulation object
- `halonumber` (int): Halo number to tag (default: 1)
- `free_param_value` (float): Free parameter for tagging fraction (default: 0.01)
- `particle_storage_filename` (str, optional): File to store tagged particles
- `mergers` (bool): Whether to include merger events (default: True)

**Returns**:
- `pd.DataFrame`: DataFrame with tagged particles

---

### Spatial Tagging

#### `spatial_tag_over_full_sim`

**Location**: `darktrace.tagging.spatial_tagging`

```python
def spatial_tag_over_full_sim(DMOsim, 
                           pynbody_path=None, 
                           occupation_frac='all', 
                           particle_storage_filename=None, 
                           mergers=True) -> pd.DataFrame
```

Tags particles based on spatial distribution using Plummer profile.

**Parameters**:
- `DMOsim` (tangos simulation): Simulation object
- `pynbody_path` (str, optional): Path to particle data. Uses config if None
- `occupation_frac` (str or float): Occupation fraction (default: 'all')
- `particle_storage_filename` (str, optional): File to store tagged particles
- `mergers` (bool): Whether to include merger events (default: True)

**Returns**:
- `pd.DataFrame`: DataFrame with spatially tagged particles

---

### Binding Energy Tagging

#### `BE_tag_over_full_sim`

**Location**: `darktrace.tagging.binding_energy_tagging`

```python
def BE_tag_over_full_sim(DMOsim, 
                        halonumber, 
                        free_param_value=0.01, 
                        PE_file=None, 
                        pynbody_path=None) -> pd.DataFrame
```

Tags particles based on binding energy (most bound particles first).

**Parameters**:
- `DMOsim` (tangos simulation): Simulation object
- `halonumber` (int): Halo number to tag
- `free_param_value` (float): Free parameter for tagging fraction (default: 0.01)
- `PE_file` (str, optional): File containing potential energies
- `pynbody_path` (str, optional): Path to particle data. Uses config if None

**Returns**:
- `pd.DataFrame`: DataFrame with binding energy tagged particles

---

## Analysis Functions

### Plotting Functions

#### `plot_tagged_vs_hydro_mass_dist`

**Location**: `darktrace.analysis.plotting`

```python
def plot_tagged_vs_hydro_mass_dist(DMO_halo_particles, 
                                 HYDRO_halo_particles, 
                                 file_with_tagged_particles, 
                                 time_to_plot, 
                                 plot_type='2D Mass Distribution')
```

Plot comparison between tagged and hydro simulation particles.

**Parameters**:
- `DMO_halo_particles` (pynbody snapshot): DMO simulation particles
- `HYDRO_halo_particles` (pynbody snapshot): Hydro simulation particles
- `file_with_tagged_particles` (str): Path to tagged particles file
- `time_to_plot` (float): Time/Redshift to plot
- `plot_type` (str): Type of plot. Options:
  - `'2D Mass Distribution'` - 2D KDE mass plot
  - `'1D Mass Distribution'` - 1D histogram
  - `'1D Mass Enclosed'` - Cumulative mass profile
  - `'1D Luminosity Distribution'` - Luminosity histogram
  - `'2D Luminosity Distribution'` - 2D luminosity plot
  - `'1D Density Distribution'` - Density profile
  - `'2D SB profile'` - Surface brightness profile
  - `'Median Age Vs Radius'` - Age profile

**Example**:
```python
from darktrace.analysis.plotting import plot_tagged_vs_hydro_mass_dist

plot_tagged_vs_hydro_mass_dist(
    DMO_halo_particles,
    HYDRO_halo_particles, 
    'tagged_particles.hdf5',
    13.8,  # Gyr
    plot_type='2D Mass Distribution'
)
```

---

## Configuration System

### Config Class

**Location**: `config.py`

```python
class Config:
    def __init__(self, config_file=None)
    def get_path(self, key) -> str
    def get(self, key, param) -> Any
    def get_all_paths(self) -> dict
```

Centralized configuration management for paths and parameters.

#### Methods

**`get_path(key)`**
Retrieves a path from the configuration.
- `key` (str): Path key (e.g., 'tangos_path', 'pynbody_path')
- Returns: `str` - Path value

**`get(key, param)`**
Retrieves a parameter from any configuration section.
- `key` (str): Section name (e.g., 'tagging', 'darklight')
- `param` (str): Parameter name
- Returns: `Any` - Parameter value

**`get_all_paths()`**
Returns all available paths.
- Returns: `dict` - Dictionary of all paths

#### Configuration File Structure

```json
{
    "paths": {
        "tangos_path": "/path/to/tangos/databases/",
        "pynbody_path": "/path/to/particle/data/",
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

---

## Utility Functions

### `os.path` Utilities

The package uses standard `os.path` functions for path manipulation:

```python
import os
from config import config

# Join paths safely
db_path = os.path.join(config.get_path('tangos_path'), 'simulation.db')
sim_path = os.path.join(config.get_path('pynbody_path'), 'output_00000')
```

### Error Handling

Common error handling patterns:

```python
try:
    df_tagged = tag_particles(DMO_database)
except FileNotFoundError as e:
    print(f"File not found: {e}")
except MemoryError:
    print("Insufficient memory - try smaller simulation")
except Exception as e:
    print(f"Unexpected error: {e}")
```

---

## Data Structures

### Tagged Particles DataFrame

The `tag_particles` function returns a DataFrame with the following typical columns:

- `iord`: Particle ID
- `x`, `y`, `z`: Particle positions
- `vx`, `vy`, `vz`: Particle velocities
- `mass`: Particle mass
- `stellar_mass`: Assigned stellar mass
- `angmom`: Angular momentum
- `binding_energy`: Binding energy (if applicable)
- `halo_id`: Parent halo identifier
- `tag_type`: Type of tagging applied

### Half-Mass Radius DataFrame

The `calculate_rhalf` function returns a DataFrame with:

- `halo_id`: Halo identifier
- `rhalf_mass`: Half-mass radius
- `rhalf_light`: Half-light radius
- `total_mass`: Total stellar mass
- `total_luminosity`: Total luminosity
- `time`: Simulation time/scale factor

---

## Performance Notes

### Memory Usage

- Angular momentum tagging: ~2x particle data size
- Spatial tagging: ~1.5x particle data size  
- Binding energy tagging: ~3x particle data size (due to energy calculations)

### Computational Complexity

- Angular momentum: O(N log N) - sorting by angular momentum
- Spatial: O(N) - distance calculations
- Binding energy: O(N²) - pairwise energy calculations (expensive)

### Optimization Tips

1. **Use recursive tagging sparingly** - can be memory intensive
2. **Limit occupation fractions** - use specific fractions instead of 'all' for large halos
3. **Store intermediate results** - use `particle_storage_filename` parameter
4. **Consider particle downsampling** - for exploratory analysis

---

## Examples

### Complete Workflow

```python
import tangos
import darktrace as dtrace
from config import config

# 1. Load simulation
tangos.init_db(os.path.join(config.get_path('tangos_path'), 'simulation.db'))
DMO_database = tangos.get_simulation('my_simulation')

# 2. Tag particles
df_tagged = dtrace.tag_particles(
    DMO_database,
    tagging_method='angular momentum',
    free_param_val=0.01
)

# 3. Calculate radii
df_radii = dtrace.calculate_rhalf(DMO_database, df_tagged)

# 4. Analyze results
print(f"Tagged {len(df_tagged)} particles")
print(f"Average half-mass radius: {df_radii['rhalf_mass'].mean():.2f} kpc")
```

### Multiple Methods Comparison

```python
methods = ['angular momentum', 'spatial']
results = {}

for method in methods:
    df_tagged = dtrace.tag_particles(DMO_database, tagging_method=method)
    df_radii = dtrace.calculate_rhalf(DMO_database, df_tagged)
    results[method] = df_radii['rhalf_mass'].mean()

print("Half-mass radii comparison:")
for method, radius in results.items():
    print(f"{method}: {radius:.2f} kpc")
```