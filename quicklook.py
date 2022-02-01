import numpy as np
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
#parser.add_argument("timestep", help="which cube timestep to convert")
#parser.add_argument("-p","--cubepath", default='./3D', help="where to read the cube files")
parser.add_argument("--path", default='./3D', help="file path of cube to plot")
parser.add_argument("-X","--x", type=int, default=0, help="x origin")
parser.add_argument("-Y","--y", type=int, default=0, help="y origin")
parser.add_argument("-W","--width", type=int, default=0, help="width")
parser.add_argument("-H","--height", type=int, default=0, help="height")
args = parser.parse_args()
x1=args.x
x2=x1 + args.width
y1=args.y
y2=y1 + args.height

#timeStep = args.timestep
cubePath = args.path
fileName = cubePath.split('/')[-1]
print(fileName)
fileNumber = fileName.split('_')
fileNumber = fileNumber[1].split('.')
print(fileNumber[0])
ind = int(fileNumber[0])
cubeList = ('rho','vx','vy','vz','eint','Bx','By','Bz','T','P','ne','tau500')
parameter = cubeList[ind]
#parameter = fileNumber
title = "%s - %s" % (fileName, parameter)

nx,ny,nz = 128,1536,1536

tmp = np.fromfile(cubePath,dtype=np.float32,).reshape((nz,ny,nx))
tmp = tmp.transpose(2,0,1)
slice = tmp[64]
if (args.width * args.height > 0):
  patch = slice[y1:y2,x1:x2]
else:
  patch = slice
print(patch.shape)
im = plt.imshow(patch,origin='lower', cmap='plasma')
cb = plt.colorbar(im)
cb.set_label(title)
plt.xlabel('Solar X[pixel]')
plt.ylabel('Solar Y[pixel]')
plt.show()

mean = patch.mean()
std = patch.std()
max = patch.max()
print(title)
print("Mean: %e"%(mean))
print("Std:  %e"%(std))
print("Max:  %e"%(max))
#tmp = np.fromfile('./subdomain_5.000361',dtype=np.float32,).reshape((nz,ny,nx))
#tmp = tmp.transpose(2,0,1)
#im = plt.imshow(tmp[64],origin='lower')
#cb = plt.colorbar(im)
#cb.set_label('Bz[G]')
#plt.xlabel('Solar X[pixel]')
#plt.ylabel('Solar Y[pixel]')
#plt.show()

