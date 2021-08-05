import h5py
import matplotlib.pyplot as plt
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-p","--path", default='~/3d_sir/sir3d/synth/data/kappa5000_eos_sir.h5', help="Path to kappa5000 eos table")
args = parser.parse_args()

kePath=args.path

ke = h5py.File(kePath, 'r')
print(ke.keys())
kappa = ke['kappa5000']
print(kappa.shape)
Pe = ke['Pe']
print(Pe.shape)
patch = kappa[:,:]

imgplot = plt.imshow(patch, cmap='gray')
plt.colorbar()
plt.gca().invert_yaxis()
plt.show()

