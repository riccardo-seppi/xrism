#!/bin/bash

xmldir=$SIXTE/share/sixte/instruments/xrism

SrcRA=197.87233
SrcDec=-1.341345

SrcRA_off=197.91
SrcDec_off=-1.37

#resolve center
xifupipeline \
  XMLFile=${xmldir}/resolve/resolve_baseline_GVclosed.xml \
  AdvXml=${xmldir}/resolve/resolve_detector.xml \
  Simput=sixte_files/A1689.simput \
  EvtFile=sixte_files/A1689_evts_resolve.fits \
  RA=${SrcRA} Dec=${SrcDec} \
  Exposure=100000

# radec2xy adds WCS coordinates to an event file
radec2xy \
  EvtFile=sixte_files/A1689_evts_resolve.fits \
  RefRA=${SrcRA} RefDec=${SrcDec} Projection=SIN

#resolve off
xifupipeline \
  XMLFile=${xmldir}/resolve/resolve_baseline_GVclosed.xml \
  AdvXml=${xmldir}/resolve/resolve_detector.xml \
  Simput=sixte_files/A1689.simput \
  EvtFile=sixte_files/A1689_evts_resolve_off.fits \
  RA=${SrcRA_off} Dec=${SrcDec_off} \
  Exposure=100000

# radec2xy adds WCS coordinates to an event file
radec2xy \
  EvtFile=sixte_files/A1689_evts_resolve_off.fits \
  RefRA=${SrcRA_off} RefDec=${SrcDec_off} Projection=SIN


# Xtend on
runsixt \
  XMLFile=${xmldir}/xtend/xtend_ccd2.xml \
  Simput=sixte_files/A1689.simput \
  EvtFile=sixte_files/A1689_evts_xtend.fits \
  RA=${SrcRA} Dec=${SrcDec} \
  Exposure=10000

# radec2xy adds WCS coordinates to an event file
radec2xy \
  EvtFile=sixte_files/A1689_evts_xtend.fits \
  RefRA=${SrcRA} RefDec=${SrcDec} Projection=SIN

#Xtend off
runsixt \
  XMLFile=${xmldir}/xtend/xtend_ccd2.xml \
  Simput=sixte_files/A1689.simput \
  EvtFile=sixte_files/A1689_evts_xtend_off.fits \
  RA=${SrcRA_off} Dec=${SrcDec_off} \
  Exposure=10000

# radec2xy adds WCS coordinates to an event file
radec2xy \
  EvtFile=sixte_files/A1689_evts_xtend_off.fits \
  RefRA=${SrcRA_off} RefDec=${SrcDec_off} Projection=SIN