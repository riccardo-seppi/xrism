#!/bin/bash

xmldir=$SIXTE/share/sixte/instruments/xrism

# Resolve
$SIXTE/bin/makespec \
  EvtFile=sixte_files/A1689_evts_resolve.fits \
  Spectrum=sixte_files/A1689_SPEC_resolve.pha \
  RSPPath=${xmldir}/resolve \
  clobber=yes

# Offset
$SIXTE/bin/makespec \
  EvtFile=sixte_files/A1689_evts_resolve_off.fits \
  Spectrum=sixte_files/A1689_SPEC_resolve_off.pha \
  RSPPath=${xmldir}/resolve \
  clobber=yes