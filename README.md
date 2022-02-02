# par-sir
**Parallel SIR Stokes synthesis from MURaM cubes**
**par-sir** is tested and optimized for HPC MPI execution using gfortran and Intel compilers
with support for batch job submission in PBS and Slurm.

**par-sir** is derived from, and depends upon,
the [3d_sir code](https://github.com/aasensio/3d_sir): Copyright (c) 2018 Andrés Asensio Ramos
The 3d_sir code is included a submodule of **par-sir** with code overlays in the synth subdirectory.

| Filename | Description |
| -------- | ----------- |
| cube2sir.py    | deprecated |
| cubeplot.py    | plot one MURaM subdomain |
| dopplerplot.py | plot 3 Stokes curves for the same LoS with Vz +/- a differential  |
| kappa.py       | plot the SIR kappa 5000 eos table |
| LICENSE        | GPL3 license |
| README.md | read this first! |
| stokesplot.py | plot synthesized stokes profiles |
| synth.ini | 3D-SIR configuration file modified for SPIN4D MURaM cubes |
| synthlos.py | synthesize a single line of sight |
| synth.py | synthesize a cube or a subset of a cube |
| synth.sh | batch synthesis of cubes  |

## Release Notes v1.0.0
### MURaM cube and 3d_sir axes
The **MURaM** simulation uses a solar Y, X, Z reference frame. This is the order the axes are written to disk.
The 3d_sir ini file parsing has been modified to allow explicit declaration of the ordering in the cube
of the solar cartesian coordinate axes.  The configuration below specifies 
Solar Y (+=North,-=South) is MURaM axis 0,
Solar X (+=West,-=East) is MURaM axis 1 and
Line of Sight (Z) is MURaM axis 2. 

- **Type** ` Type = 'MURAM'`
- **XYZ** `XYZ = 1, 0, 2`
- **Dimensions** `Dimensions = 1536, 1536, 128`

### source code mods to 3d_sir

The par-sir mods directory contains source code tree with all the par-sir modifications to 3d_sir.
After cloning the repo you can run build_3d_sir.sh to copy the par-sir modifications into
the 3d_sir source hierarchy and automatically compile and install 3d_sir.
Be sure to "conda activate SIR" or use pip to configure your local env to meet the 3d_sir requirements. 

### spectral line configuration

3d_sir includes a data file "LINEAS" to define each available line to synthesize.
To synthesize the 1565nm Fe lines the LINEAS file and interface.f90 were updated
with the following integer and half-integer spin encodings:
- S:0 P:1 D:2 F:3 G:4 H:5 I:6 K:7 L:8 M:9 N:10 O:11 Q:12`
- p:1/2 f:3/2 h:5/2 k:7/2 m:9/2 o:11/2 r:13/2 t:15/2 u:17/2 v:19/2 w:21/2`

### Note regarding solar abundances of atomic alements

The 3d_sir code includes a data file "THEVENIN" with solar abundances from Grevesse (1984):
	Abundances quoted by THEVENIN and taken from Grevesse, 1984, Physica Scripta, Vol.T8,49-58.
	Abundances for Na,Mg,Al,Si,K,Ca,Sc,Ti,V,Cr,Mn,Fe,Co,Ni,Cu,
	Zn,Ge,Sr,Y,Zr,Nb,Mo,Ru,Rh,Ba,La,Ce,Pr,Nd,Sm,Eu,Gd,Dy,W and Ir from Holweger
	as quoted by Thevenin, 1989, Astron. Astrophys. Suppl.Ser 77, 137-154.

It appears that for 3d_sir to avoid I/O overhead which is indeed a problem for MPI performance,
the initialization of abundances from the file THEVENIN has been commented out.
The values from THEVENIN are hard-coded in leyendo.f and interface.f90.

For our project we use the abundances from Grevesse (1998):
	Abundances are taken from Grevesse, N., Sauval, A. Standard Solar Composition. Space Science Reviews 85, 161–174 (1998).
	Abundances for As, Se, Br, Kr, Te, I, Xe, Cs, Ta, Re, Hg, Bi, Th are determined from meteorites.

We have changed the hard-coded values in leyendo.f and interface.f90 and provided the Grevesse (1998) values
in the currently unused data file "ABUNDANCES".
**TODO** replace hard-coded abundances with a vector intialized from a configured abundance file
and passed to sir_code.synth() once per worker thread.

### changes to model.py and multiprocessing.py

There are three significant modifications to these two files.
1. Parsing the configuration file for new configuration settings
1. Reordering the axes to be consistent with solar coordinates and optimum for Python
1. Replacing the interpolated atmosphere with the values from the MURaM cube
1. Changing the 5h dataset schema

## Helper scripts
The script "synth.sh" can be used to automatically create a cube specific ini file from the synth.ini template. 
This is useful when running a pipeline on an HPC cluster.

## Visualizations
The **stokesplot.py** python program produces various plots:
- Single wavelength spatial Stokes profile image (specify WL and I, Q, U or V)
  - `python stokesplot.py -V --colormap=inferno --path=stokes-038817-15648.h5`
- Single pixel Stokes profile plots (specify pixel y and x)
  - `python stokesplot.py --px=100 --py=100 --path=stokes-038817-6302.h5`
- Polarization butterfly plots for a single line (specify column x)
  - `python stokesplot.py --slice=100 --path=stokes-038817-6302.h5`

