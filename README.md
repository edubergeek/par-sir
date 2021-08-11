# par-sir
**Parallel SIR Stokes synthesis from MURaM cubes**
**par-sir** is tested and optimized for HPC MPI execution using gfortran or Intel compilers and includes support for batch job submission in PBS and Slurm.

**par-sir** is derived from, and depends upon, the [3d_sir code](https://github.com/aasensio/3d_sir): Copyright (c) 2018 Andrés Asensio Ramos
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

**Note regarding MURaM cube and 3d_sir axes**
The MURaM simulation uses a solar Y, X, Z reference frame. This is the order the axes are written to disk.
The 3d_sir ini file parsing has been modified to allow explicit declaration of the ordering in the cube of the solar cartesian coordinate axes using:
- **Type** ` Type = 'MURAM'`
- **XYZ** `XYZ = 1, 0, 2`
- **Dimensions** `Dimensions = 1536, 1536, 128`
This configuration specifies that Solar Y (+=North,-=South) is MURaM axis 0, Solar X (+=West,-=East) is MURaM axis 1 and Line of Sight (Z) is MURaM axis 2. 

**Note regarding LINEAS**

Following are valid integer spin encodings:
`S:0 P:1 D:2 F:3 G:4 H:5 I:6 K:7 L:8 M:9 N:10 O:11 Q:12`

Following are valid half-integer spin encodings:
`p:1/2 f:3/2 h:5/2 k:7/2 m:9/2 o:11/2 r:13/2 t:15/2 u:17/2 v:19/2 w:21/2`
