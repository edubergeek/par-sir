import h5py
import matplotlib.pyplot as plt
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-p","--path", default='./3D/stokes.h5', help="which stokes file to visualize")
parser.add_argument("-s","--slice", type=int, default=-1, help="which x slice to visualize QUV")
parser.add_argument("-c","--clip", dest='clipOutliers', default=False, action='store_true', help="clip outliers")
parser.add_argument("-m","--colormap", default="gray", help="which colormap to plot with")
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
cmap = args.colormap

#print("S == %d"%(S))

dataStokes = h5py.File(stokesPath, 'r')
#print(dataStokes.keys())
sI = dataStokes['I']
sQ = dataStokes['Q']
sU = dataStokes['U']
sV = dataStokes['V']
zp = dataStokes.attrs["lambda_zeropoint"]
wl = 1e-4 * (dataStokes["lambda"][:] + zp)

# plotSstokes profiles for a single pixel
if (args.px + args.py > 0):
  fig, axs = plt.subplots(2, 2, figsize=(10, 8), constrained_layout=True)
  wI = sI[args.py,args.px,:]
  wQ = sQ[args.py,args.px,:]
  wU = sU[args.py,args.px,:]
  wV = sV[args.py,args.px,:]
  axs[0, 0].plot(wl, wI)
  axs[0, 0].set_title('I')
  axs[0, 1].plot(wl, wQ)
  axs[0, 1].set_title('Q')
  axs[1, 0].plot(wl, wU)
  axs[1, 0].set_title('U')
  axs[1, 1].plot(wl, wV)
  axs[1, 1].set_title('V')
  plt.show()
elif (XSlice >= 0):
  fig, axs = plt.subplots(1, 3, figsize=(6, 6), constrained_layout=True)
  butterfly = sQ[:,XSlice,:]
  axs[0].imshow(butterfly, cmap=cmap, interpolation='nearest')
  butterfly = sU[:,XSlice,:]
  axs[1].imshow(butterfly, cmap=cmap, interpolation='nearest')
  butterfly = sV[:,XSlice,:]
  axs[2].imshow(butterfly, cmap=cmap, interpolation='nearest')
  plt.gca().invert_yaxis()
  for ax in axs.flatten():  # flatten in case you have a second row at some point
    ax.set_aspect('auto')
  plt.show()
else:
  imgs = (sI, sQ, sU, sV)
  if (args.width * args.height > 0):
    img = imgs[S][y1:y2,x1:x2,WL]
  else:
    img = imgs[S][:,:,WL]
  if args.clipOutliers:
    print("original: %6.4f %6.4f %6.4f %6.4f"%(img.mean(), img.var(), img.min(), img.max()))
    img = np.clip(img, 0, 10)
    print("Clipped:  %6.4f %6.4f %6.4f %6.4f"%(img.mean(), img.var(), img.min(), img.max()))
  
  imgplot = plt.imshow(img, cmap=cmap)
  plt.colorbar();
  plt.gca().invert_yaxis()
  plt.show()
