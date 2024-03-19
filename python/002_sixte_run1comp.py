import sys, os
import numpy as np
sys.path.append('/home/riccardo/xrism')
from xrism_mock import XRISMmock
from xrism_mock import spectral_fitting
from astropy.cosmology import FlatLambdaCDM
import astropy.units as u

cosmo = FlatLambdaCDM(70, 0.3)

basedir='/home/riccardo/xrism/A1689'

XSPECFile = os.path.join(basedir, 'sixte_files/1comp/A16891comp.xcm')
IMGFile = os.path.join(basedir, 'data/csm_sb_cropR500.fits')
#Lx_obs = 9.49665e+44
#Flux = Lx_obs / ( 4. * np.pi * (cosmo.luminosity_distance(z=0.1842).to(u.cm)**2))
Flux = 9.92495883e-12
p2simput = os.path.join(basedir, 'sixte_files/1comp/A1689.simput')
A1689 = XRISMmock.XRISM_source(name = 'A1689', RA_src=197.867750, DEC_src=-1.313722,
    XSPECFile=XSPECFile, IMGFile=IMGFile, Flux=Flux, p2simput=p2simput,
    Emin_flux=0.5, Emax_flux=2.0, Emin_spec=0.1, Emax_spec=30
    )

#Create simput
A1689.create_simput()

# Now do 1 component, 1 pointing in the center with resolve, xtend
RA_pnt = 197.87233
DEC_pnt = -1.341345
texp = 2e5 #200ks
#Generate events
p2evt_resolve = os.path.join(basedir, 'sixte_files/1comp/A1689_evts_resolve.fits')
A1689.runSIXTE_resolve(p2evt_resolve, RA_pnt, DEC_pnt, texp)

p2evt_xtend = os.path.join(basedir, 'sixte_files/1comp/A1689_evts_xtend.fits')
A1689.runSIXTE_xtend(p2evt_xtend, RA_pnt, DEC_pnt, texp)

#Make images
p2img = os.path.join(basedir,'sixte_files/1comp/A1689_IMG_resolve.fits')
A1689.createIMAGE_resolve(p2evt_resolve, p2img, RA_pnt, DEC_pnt)

p2img = os.path.join(basedir,'sixte_files/1comp/A1689_IMG_xtend.fits')
A1689.createIMAGE_xtend(p2evt_xtend, p2img, RA_pnt, DEC_pnt)

#Extract and fit resolve spectrum
p2spec = os.path.join(basedir, 'sixte_files/1comp/A1689_SPEC_resolve.pha')
A1689.extractSPECTRUM_resolve(p2evt_resolve, p2spec)

p2out = os.path.join(basedir, 'sixte_files/1comp/A1689_spec_result.txt')
spectral_fitting.fit_Tbabs_bapec(p2spec, p2out, Emin=2.0, Emax=10, nH=0.0167, kT=8.8, z=0.184, vel=180)


# Now do 1 component, second pointing off-center with resolve, xtend
RA_pnt = 197.92
DEC_pnt = -1.29
texp = 2e5 #200ks
#Generate events
p2evt_resolve = os.path.join(basedir, 'sixte_files/1comp/A1689_evts_resolve_off.fits')
A1689.runSIXTE_resolve(p2evt_resolve, RA_pnt, DEC_pnt, texp)

p2evt_xtend = os.path.join(basedir, 'sixte_files/1comp/A1689_evts_xtend_off.fits')
A1689.runSIXTE_xtend(p2evt_xtend, RA_pnt, DEC_pnt, texp)

#Make images
p2img = os.path.join(basedir,'sixte_files/1comp/A1689_IMG_resolve_off.fits')
A1689.createIMAGE_resolve(p2evt_resolve, p2img, RA_pnt, DEC_pnt)

p2img = os.path.join(basedir,'sixte_files/1comp/A1689_IMG_xtend_off.fits')
A1689.createIMAGE_xtend(p2evt_xtend, p2img, RA_pnt, DEC_pnt)

#Extract and fit resolve spectrum
p2spec = os.path.join(basedir, 'sixte_files/1comp/A1689_SPEC_resolve_off.pha')
A1689.extractSPECTRUM_resolve(p2evt_resolve, p2spec)

p2out = os.path.join(basedir, 'sixte_files/1comp/A1689_spec_result_off.txt')
spectral_fitting.fit_Tbabs_bapec(p2spec, p2out, Emin=2.0, Emax=10, nH=0.0167, kT=8.8, z=0.184, vel=180)