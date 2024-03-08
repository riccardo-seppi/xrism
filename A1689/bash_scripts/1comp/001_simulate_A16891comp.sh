#!/bin/bash

xmldir=$SIXTE/share/sixte/instruments/xrism
basedir=/home/riccardo/xrism/A1689

SrcRA=197.87233
SrcDec=-1.341345

SrcRA_off=197.92
SrcDec_off=-1.29

#resolve center
xifupipeline \
  XMLFile=${xmldir}/resolve/resolve_baseline_GVclosed.xml \
  AdvXml=${xmldir}/resolve/resolve_detector.xml \
  Simput=${basedir}/sixte_files/1comp/A1689.simput \
  EvtFile=${basedir}/sixte_files/1comp/A1689_evts_resolve.fits \
  RA=${SrcRA} Dec=${SrcDec} \
  Exposure=100000

# radec2xy adds WCS coordinates to an event file
radec2xy \
  EvtFile=${basedir}/sixte_files/1comp/A1689_evts_resolve.fits \
  RefRA=${SrcRA} RefDec=${SrcDec} Projection=SIN

#resolve off
xifupipeline \
  XMLFile=${xmldir}/resolve/resolve_baseline_GVclosed.xml \
  AdvXml=${xmldir}/resolve/resolve_detector.xml \
  Simput=${basedir}/sixte_files/1comp/A1689.simput \
  EvtFile=${basedir}/sixte_files/1comp/A1689_evts_resolve_off.fits \
  RA=${SrcRA_off} Dec=${SrcDec_off} \
  Exposure=200000

# radec2xy adds WCS coordinates to an event file
radec2xy \
  EvtFile=${basedir}/sixte_files/1comp/A1689_evts_resolve_off.fits \
  RefRA=${SrcRA_off} RefDec=${SrcDec_off} Projection=SIN