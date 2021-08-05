import h5py
import matplotlib.pyplot as plt
import numpy as np
import argparse

parser = argparse.ArgumentParser()
#parser.add_argument("-p","--path", default='./3D/stokes.h5', help="which stokes file to visualize")
parser.add_argument("-p","--path", default='./3D-000361/stokes-000361-0_0.h5', help="which stokes file to visualize")
parser.add_argument("-i","--inc", default='./3D-000361+/stokes-000361-0_0.h5', help="which stokes file to visualize")
parser.add_argument("-d","--dec", default='./3D-000361-/stokes-000361-0_0.h5', help="which stokes file to visualize")
parser.add_argument("-s","--slice", type=int, default=0, help="which x slice to visualize QUV")
parser.add_argument("-w","--wl", type=int, default=0, help="which wl to visualize I")
parser.add_argument("-X","--x1", type=int, default=0, help="x origin")
parser.add_argument("-Y","--y1", type=int, default=0, help="y origin")
parser.add_argument("-W","--width", type=int, default=0, help="width")
parser.add_argument("-H","--height", type=int, default=0, help="height")
parser.add_argument("-I","--stokesI", dest='stokesI', action='store_true', help="plot Stokes I")
parser.add_argument("-Q","--stokesQ", dest='stokesQ', action='store_true', help="plot Stokes Q")
parser.add_argument("-U","--stokesU", dest='stokesU', action='store_true', help="plot Stokes U")
parser.add_argument("-V","--stokesV", dest='stokesV', action='store_true', help="plot Stokes V")
args = parser.parse_args()

stokesPath=args.path
x1=args.x1
x2=x1 + 1
y1=args.y1
y2=y1 + 1
WL=args.wl
S = 0

print("S == %d"%(S))

dataStokes = h5py.File(stokesPath, 'r')
print(dataStokes.keys())
lambdaStokes = dataStokes['lambda']
wl = lambdaStokes[:]
print(wl.shape)
wl = wl.flatten()
wl /= 1000.0
wl += 6301.508
print('WL[0] to WL[-1] is %f to %f'%(wl[0], wl[-1]))

stokes = dataStokes['stokes']
print(stokes.shape)

curve = stokes[y1:y2,x1:x2,S,:]
print(curve.shape)
curve = curve.flatten()
print(curve.shape)

incStokes = h5py.File(args.inc, 'r')
stokesAdd = incStokes['stokes']
curveAdd = stokesAdd[y1:y2,x1:x2,S,:]
curveAdd = curveAdd.flatten()

decStokes = h5py.File(args.dec, 'r')
stokesSub = decStokes['stokes']
curveSub = stokesSub[y1:y2,x1:x2,S,:]
curveSub = curveSub.flatten()

p = plt.plot(wl, curve, color='green', label='Vz')
p = plt.plot(wl, curveAdd, color='blue', label='Vz+')
p = plt.plot(wl, curveSub, color='red', label='Vz-')
plt.legend()
plt.xlabel('WL')
plt.ylabel('Stokes I')
plt.title('Vz 3D-SIR Doppler Shift at [0,0]')
plt.show()

