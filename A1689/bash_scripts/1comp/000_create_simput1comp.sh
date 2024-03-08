#!/bin/sh
# create a simput file for A1689
basedir=/home/riccardo/xrism/A1689

$SIMPUT/bin/simputfile       \
    Simput=${basedir}/sixte_files/1comp/A1689.simput \
    Src_Name=A1689       \
    RA=197.867750 Dec=-1.313722 \
    Emin=0.5 Emax=2.0          \
    srcFlux=9.92495883e-12    \
    Nbins=19900            \
    logEgrid=n            \
    Elow=0.1 Eup=30          \
    XSPECFile=${basedir}/sixte_files/1comp/A16891comp.xcm   \
    ImageFile=${basedir}/data/csm_sb_cropR500.fits \
    clobber=yes