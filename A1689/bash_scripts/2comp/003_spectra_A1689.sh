#!/bin/bash

xmldir=$SIXTE/share/sixte/instruments/xrism
basedir=/home/riccardo/xrism/A1689

# Resolve
$SIXTE/bin/makespec \
  EvtFile=${basedir}/sixte_files/2comp/A1689_evts_resolve.fits \
  Spectrum=${basedir}/sixte_files/2comp/A1689_SPEC_resolve.pha \
  RSPPath=${xmldir}/resolve \
  clobber=yes