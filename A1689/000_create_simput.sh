#!/bin/sh
# create a simput file for A1689

$SIMPUT/bin/simputfile       \
    Simput=sixte_files/A1689.simput \
    Src_Name=A1689       \
    RA=197.867750 Dec=-1.313722 \
    Emin=0.5 Emax=2.0          \
    srcFlux=9.322793005013373e-12    \
    Nbins=19900            \
    logEgrid=n            \
    Elow=0.1 Eup=15          \
    XSPECFile=sixte_files/A1689.xcm   \
    ImageFile=data/csm_sb_cropR500.fits \
    clobber=yes