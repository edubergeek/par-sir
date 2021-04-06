import h5py
import matplotlib.pyplot as plt
import numpy as np
import argparse

parser = argparse.ArgumentParser()
#parser.add_argument("timestep", help="which cube timestep to convert")
#parser.add_argument("-p","--cubepath", default='./3D', help="where to read the cube files")
parser.add_argument("--sirpath", default='./3D', help="where to write the sir files")
parser.add_argument("-x","--xdim", type=int, default=128, help="cube x dimension, defaults to 128")
parser.add_argument("-y","--ydim", type=int, default=1536, help="cube y dimension, defaults to 1536")
parser.add_argument("-z","--zdim", type=int, default=1536, help="cube z dimension, defaults to 1536")
args = parser.parse_args()

#timeStep = args.timestep
sirPath = args.sirpath
#paramList = ('rho','vx','vy','vz','eint','Bx','By','Bz','T','P','ne','tau500')
filePath = args.sirpath + '/subdomain_0.float'

#yzxShape = (args.xdim, args.ydim, args.zdim)
zxyShape = (args.zdim, args.xdim, args.ydim)

#yzxArray = np.memmap(filePath, dtype='float32', mode='r', shape=zxyShape, order='C')
zxyArray = np.memmap(filePath, dtype='float32', mode='r', shape=zxyShape, order='C')

#data = yzxArray[:,640:896,640:896]
data = zxyArray[:,:,:]
print(data.shape)
patch = data[:,100,:]
print(patch.shape)

imgplot = plt.imshow(patch, cmap='plasma')
plt.colorbar();
plt.show()

