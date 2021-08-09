import numpy as np
import matplotlib.pyplot as plt

nx,ny,nz = 128,1536,1536

tmp = np.fromfile('./subdomain_1.000361',dtype=np.float32,).reshape((nz,ny,nx))
tmp = tmp.transpose(2,0,1)
im = plt.imshow(tmp[64],origin='lower')
cb = plt.colorbar(im)
cb.set_label('Vz[km/s]')
plt.xlabel('Solar X[pixel]')
plt.ylabel('Solar Y[pixel]')
plt.show()

tmp = np.fromfile('./subdomain_5.000361',dtype=np.float32,).reshape((nz,ny,nx))
tmp = tmp.transpose(2,0,1)
im = plt.imshow(tmp[64],origin='lower')
cb = plt.colorbar(im)
cb.set_label('Bz[G]')
plt.xlabel('Solar X[pixel]')
plt.ylabel('Solar Y[pixel]')
plt.show()

