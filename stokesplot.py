import h5py
import matplotlib.pyplot as plt
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-p","--path", default='./3D/stokes.h5', help="which stokes file to visualize")
parser.add_argument("-s","--slice", type=int, default=0, help="which x slice to visualize QUV")
parser.add_argument("-w","--wl", type=int, default=0, help="which wl to visualize I")
parser.add_argument("-x","--px", type=int, default=-1, help="pixel col to plot")
parser.add_argument("-y","--py", type=int, default=-1, help="pixel row to plot")
parser.add_argument("-X","--x", type=int, default=0, help="x origin")
parser.add_argument("-Y","--y", type=int, default=0, help="y origin")
parser.add_argument("-W","--width", type=int, default=0, help="width")
parser.add_argument("-H","--height", type=int, default=0, help="height")
parser.add_argument("-I","--stokesI", dest='stokesI', action='store_true', help="plot Stokes I")
parser.add_argument("-Q","--stokesQ", dest='stokesQ', action='store_true', help="plot Stokes Q")
parser.add_argument("-U","--stokesU", dest='stokesU', action='store_true', help="plot Stokes U")
parser.add_argument("-V","--stokesV", dest='stokesV', action='store_true', help="plot Stokes V")
args = parser.parse_args()

stokesPath=args.path
x1=args.x
x2=x1 + args.width
y1=args.y
y2=y1 + args.height
XSlice=args.slice
WL=args.wl
if args.stokesI:
  S = 0
elif args.stokesQ:
  S = 1
elif args.stokesU:
  S = 2
elif args.stokesV:
  S = 3
else:
  S = 0

print("S == %d"%(S))

dataStokes = h5py.File(stokesPath, 'r')
print(dataStokes.keys())
stokes = dataStokes['stokes']
print(stokes.shape)

if (args.px + args.py > 0):
  fig, axs = plt.subplots(2, 2, figsize=(5, 5))
  lambdaIX = stokes[args.py,args.px,:,:]
  print(lambdaIX.shape)
  lambdaI = stokes[args.py,args.px,0,:]
  lambdaQ = stokes[args.py,args.px,1,:]
  lambdaU = stokes[args.py,args.px,2,:]
  lambdaV = stokes[args.py,args.px,3,:]
  wl = np.linspace(6300.8521, 6303.3119, num=276) / 10.0
  axs[0, 0].plot(wl, lambdaI)
  axs[0, 0].set_title('I')
  axs[0, 1].plot(wl, lambdaQ)
  axs[0, 1].set_title('Q')
  axs[1, 0].plot(wl, lambdaU)
  axs[1, 0].set_title('U')
  axs[1, 1].plot(wl, lambdaV)
  axs[1, 1].set_title('V')
  #plt.gca().invert_yaxis()
  plt.show()
else:
  if (args.width * args.height > 0):
    lambdaWL = stokes[y1:y2,x1:x2,:,WL]
  else:
    lambdaWL = stokes[:,:,:,WL]
  print(lambdaWL.shape)
  lambdaWLStokes = lambdaWL[:,:,S]
  print(lambdaWLStokes.shape)
  patch = lambdaWLStokes[:,:]
  print(patch.shape)
  print(patch.mean())
  print(patch.var())
  
  patch = np.clip(patch, 0, 10)
  print(patch.mean())
  print(patch.var())
  
  imgplot = plt.imshow(patch, cmap='gray')
  plt.colorbar();
  plt.gca().invert_yaxis()
  plt.show()
  
  if (XSlice == -1):
    if (x1 * x2 > 0):
      XSlice = int((x1 + x2) / 2)
    else:
      XSlice = int(stokes.shape[1] / 2)
  lambdaIX = stokes[:,XSlice,:,:]
  print(lambdaIX.shape)
  if (x1 * y1 * x2 * y2 > 0):
    quv = lambdaIX[y1:y2,:,:]
  else:
    quv = lambdaIX[:,:,:]
  print(quv.shape)
  
  fig, axs = plt.subplots(1, 3, figsize=(5, 5))
  patch = quv[:,1,:]
  print(patch.shape)
  axs[0].imshow(patch, cmap='gray')
  patch = quv[:,2,:]
  axs[1].imshow(patch, cmap='gray')
  patch = quv[:,3,:]
  axs[2].imshow(patch, cmap='gray')
  plt.gca().invert_yaxis()
  plt.show()
