# XRSIM Mocks #

This package is a wrapper around SIXTE (https://www.sternwarte.uni-erlangen.de/sixte/, Dauser+19) tailored to XRISM.
For installing SIXTE and SIMPUT follow https://www.sternwarte.uni-erlangen.de/sixte/installation/

The code assumes that you saved XRISM response files in

```
$SIXTE/share/sixte/instruments/xrism
```

This is the standard installation path.
For now (08.03.2024), it is possible to use the package by appending to your sys path.
The XRISM_source class allows the user to manage a source to simulate. For example:

```commandline
import sys, os
sys.path.append('/home/riccardo/xrism')
from xrism_mock import XRISMmock
from xrism_mock import spectral_fitting
```

Change your path to the xrism repo in the code above.
To initialize the source, you need to provide an image in fits format and an xcm file describing the model of the spectrum.
For a simple apec model, with kT=5 keV, Z=0.3, z=0.1, this is as simple as:
```
abund aspl
cosmo 70 0 0.73
systematic 0
model  apec
            5         0.01          0          0         20         20
            0.3       0.01          0          0          1          1
            0.1       0.01          0          0        0.2        0.2
            1         0.01       0.01      0.008      0.008         64
```
The normalization will be rescaled according to the total flux provided to our source. Notice that the flux is always in observer frame, make sure you account for any K-correction if you get the flux from luminosity.

Now we can initialize the source. Notice that the RA_src, DEC_src need to match the coordinates of the reference pixel in the image you provide!
Make sure that this is correct, not always the reference pixel of an image is set to the same exact coordinates of the source in the image.
```commandline
XSPECFile = path_to_xspecfile.xcm
IMGFile = path_to_image.fits
Flux = 1e-11
p2simput = path_to_file.simput
MySource = XRISMmock.XRISM_source(name = 'NAME', RA_src=180, DEC_src=-10,
    XSPECFile=XSPECFile, IMGFile=IMGFile, Flux=Flux, p2simput=p2simput,
    Emin_flux=0.5, Emax_flux=2.0, Emin_spec=0.1, Emax_spec=30
    )
```
Now create the simput and generate mock events with resolve and xtend.
You can specify the pointing and the exposure time. Make sure you change RA_pnt and DEC_pnt in the following code:
```commandline
MySource.create_simput()
RA_pnt = 180.1
DEC_pnt = -10.2
texp = 2e5 #200ks
p2evt_resolve = path_to_events_resolve.fits
MySource.runSIXTE_resolve(p2evt_resolve, RA_pnt, DEC_pnt, texp)

p2evt_xtend = path_to_events_xtend.fits
MySource.runSIXTE_xtend(p2evt_xtend, RA_pnt, DEC_pnt, texp)
```

Now you can create images. You can change the center of the images by specifying new RA_pnt, DEC_pnt, if needed.
```commandline
p2img = path_to_image_resolve.fits
MySource.createIMAGE_resolve(p2evt_resolve, p2img, RA_pnt, DEC_pnt)

p2img = path_to_image_xtend.fits
MySource.createIMAGE_xtend(p2evt_xtend, p2img, RA_pnt, DEC_pnt)
```

Extract the spectrum
```commandline
p2spec = p2spec_resolve.pha
MySource.extractSPECTRUM_resolve(p2evt_resolve, p2spec)
```

The package also allows you to do some simple spectral fits using XSPEC.
For now (08.03.2024), two models are available: Tbabs(bapec) and Tbabs(bapec + bapec). 
The galactic nH and the metallicity are frozen.
You need to provide the path to a file storing the output of the XSPEC fit.
```commandline
p2out = path_to_summaryfile.txt
spectral_fitting.fit_Tbabs_bapec(p2spec, p2out, Emin=2.0, Emax=10, nH=0.0167, kT=8.8, z=0.184, vel=180)
```

# Attitude files #
If you need specific information about the pointing of the telescope you can create and use attitude files