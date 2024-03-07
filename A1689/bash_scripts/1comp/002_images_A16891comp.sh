#!/bin/bash

basedir=/home/riccardo/xrism/A1689

SrcRA=197.87233
SrcDec=-1.341345

SrcRA_off=197.9031984
SrcDec_off=-1.3928054

# Since this source is no longer at (0,0), we need to adjust
# CRVAL in imgev

# Resolve
$SIXTE/bin/imgev \
    EvtFile=${basedir}/sixte_files/1comp/A1689_evts_resolve.fits \
    Image=${basedir}/sixte_files/1comp/A1689_IMG_resolve.fits \
    CoordinateSystem=0 Projection=TAN \
    NAXIS1=6 NAXIS2=6 \
    CUNIT1=deg CUNIT2=deg \
    CRVAL1=${SrcRA} CRVAL2=${SrcDec} \
    CRPIX1=3.5 CRPIX2=3.5 \
    CDELT1=-85.12516e-04 CDELT2=85.12516e-04 \
    history=true clobber=yes

#Offset
$SIXTE/bin/imgev \
    EvtFile=${basedir}/sixte_files/1comp/A1689_evts_resolve_off.fits \
    Image=${basedir}/sixte_files/1comp/A1689_IMG_resolve_off.fits \
    CoordinateSystem=0 Projection=TAN \
    NAXIS1=6 NAXIS2=6 \
    CUNIT1=deg CUNIT2=deg \
    CRVAL1=${SrcRA_off} CRVAL2=${SrcDec_off} \
    CRPIX1=3.5 CRPIX2=3.5 \
    CDELT1=-85.12516e-04 CDELT2=85.12516e-04 \
    history=true clobber=yes