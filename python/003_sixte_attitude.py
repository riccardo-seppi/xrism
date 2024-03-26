import sys, os
import numpy as np
sys.path.append('/home/riccardo/xrism')
from xrism_mock import XRISMmock
from xrism_mock import helper

#create attitude file
p2att = '/home/riccardo/xrism/A1689/Attitude_test.fits'
time = np.array([0., 2e5])
ra = np.array([197.87233, 197.87233])
dec = np.array([-1.341345, -1.341345])
roll = np.array([150., 150.])
tstart = 0
tstop = 2e5
#mjdref = helper.get_MJD_from_date(datetime.utcnow())
mjdref = 60395.38870714722
helper.create_attitude(p2att=p2att, time=time, ra=ra, dec=dec, roll=roll,
                       tstart=tstart, tstop=tstop, mjdref=mjdref)

basedir='/home/riccardo/xrism/A1689'
XSPECFile = os.path.join(basedir, 'sixte_files/1comp/A16891comp.xcm')
IMGFile = os.path.join(basedir, 'data/csm_sb_cropR500.fits')
#Lx_obs = 9.49665e+44
#Flux = Lx_obs / ( 4. * np.pi * (cosmo.luminosity_distance(z=0.1842).to(u.cm)**2))
Flux = 9.92495883e-12
p2simput = os.path.join(basedir, 'sixte_files/1comp/A1689.simput')

A1689 = XRISMmock.XRISM_source(name = 'A1689', RA_src=197.867750, DEC_src=-1.313722,
    XSPECFile=XSPECFile, IMGFile=IMGFile, Flux=Flux, p2simput=p2simput,
    Emin_flux=0.5, Emax_flux=2.0, Emin_spec=0.1, Emax_spec=30, attitude=p2att
    )

RA_pnt = 197.87233
DEC_pnt = -1.341345
texp = 2e5 #200ks
p2evt_resolve = os.path.join(basedir, 'sixte_files/1comp/A1689_evts_resolve_attitude.fits')
A1689.runSIXTE_resolve_attitude(p2evt_resolve, RA_pnt, DEC_pnt, texp, mjdref=mjdref)

p2evt_xtend = os.path.join(basedir, 'sixte_files/1comp/A1689_evts_xtend_attitude.fits')
A1689.runSIXTE_xtend_attitude(p2evt_xtend, RA_pnt, DEC_pnt, texp, mjdref=mjdref)
