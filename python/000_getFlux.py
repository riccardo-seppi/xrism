import numpy as np
from astropy.cosmology import FlatLambdaCDM
import astropy.units as u

cosmo = FlatLambdaCDM(67.74, 0.3112)

def getFX_from_Lx_obsframe(Lx, z):
    dl = cosmo.luminosity_distance(z).to(u.cm)
    Fx = Lx / (4. * np.pi *dl**2)
    return Fx

Lx_A1689 = 9.49665e+44
z = 0.1842
Fx = getFX_from_Lx_obsframe(Lx_A1689, z)
print(Fx)