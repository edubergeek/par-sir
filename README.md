# par-sir
Parallel SIR Stokes synthesis from MURaM cubes

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

**Note regarding LINEAS**
Following are valid integer spin encodings:
`S:0 P:1 D:2 F:3 G:4 H:5 I:6 K:7 L:8 M:9 N:10 O:11 Q:12`

Following are valid half-integer spin encodings:
`p:1/2 f:3/2 h:5/2 k:7/2 m:9/2 o:11/2 r:13/2 t:15/2 u:17/2 v:19/2 w:21/2`
