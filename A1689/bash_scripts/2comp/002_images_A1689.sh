#!/bin/bash

basedir=/home/riccardo/xrism/A1689

SrcRA=197.87233
SrcDec=-1.341345

SrcRA_off=197.91
SrcDec_off=-1.37

# Since this source is no longer at (0,0), we need to adjust
# CRVAL in imgev

# Resolve
$SIXTE/bin/imgev \
    EvtFile=${basedir}/sixte_files/2comp/A1689_evts_resolve.fits \
    Image=${basedir}/sixte_files/2comp/A1689_IMG_resolve.fits \
    CoordinateSystem=0 Projection=TAN \
    NAXIS1=6 NAXIS2=6 \
    CUNIT1=deg CUNIT2=deg \
    CRVAL1=${SrcRA} CRVAL2=${SrcDec} \
    CRPIX1=3.5 CRPIX2=3.5 \
    CDELT1=-85.12516e-04 CDELT2=85.12516e-04 \
    history=true clobber=yes

#SAme, with xtend
# Xtend
$SIXTE/bin/imgev \
    EvtFile=${basedir}/sixte_files/2comp/A1689_evts_xtend.fits \
    Image=${basedir}/sixte_files/2comp/A1689_IMG_xtend.fits \
    CoordinateSystem=0 Projection=TAN \
    NAXIS1=640 NAXIS2=640 \
    CUNIT1=deg CUNIT2=deg \
    CRVAL1=${SrcRA} CRVAL2=${SrcDec} \
    CRPIX1=473.34 CRPIX2=473.34 \
    CDELT1=-4.9110668e-04 CDELT2=4.9110668e-04  \
    history=true clobber=yes