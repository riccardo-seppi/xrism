import os
import sys


class XRISM_source():
    def __init__(self, name, RA_src, DEC_src,
                XSPECFile, IMGFile, Flux, p2simput,
                Emin_flux=0.5, Emax_flux=2.0, Emin_spec=0.1, Emax_spec=30):
        self.name = name
        self.RA_src = RA_src
        self.DEC_src = DEC_src
        #self.RA_pnt = RA_pnt
        #self.DEC_pnt = DEC_pnt
        self.XSPECFile = XSPECFile
        self.IMGFile = IMGFile
        self.Flux = Flux
        self.Emin_flux = Emin_flux
        self.Emax_flux = Emax_flux
        self.Emin_spec = Emin_spec
        self.Emax_spec = Emax_spec
        self.p2simput = p2simput

        if os.path.isfile(self.XSPECFile):
            print('Using', self.XSPECFile)
        else:
            print(self.XSPECFile, 'does not exist!')
            sys.exit()

        if os.path.isfile(self.IMGFile):
            print('Using', self.IMGFile)
        else:
            print(self.IMGFile, 'does not exist!')
            sys.exit()


    def create_simput(self):

        if not os.path.isfile(self.p2simput):
            print('Creating', self.p2simput)
            cmd_list = ['$SIMPUT/bin/simputfile',
                'Simput=%s'%self.p2simput,
                'Src_Name=%s'%self.name,
                'RA=%.8f Dec=%.8f'%(self.RA_src, self.DEC_src),
                'Emin=%.3f Emax=%.3f'%(self.Emin_flux, self.Emax_flux),
                'srcFlux=%.5g'%self.Flux,
                'Nbins=19900',
                'logEgrid=n',
                'Elow=%.3f Eup=%.3f'%(self.Emin_spec, self.Emax_spec),
                'XSPECFile=%s'%self.XSPECFile,
                'ImageFile=%s'%self.IMGFile,
                'clobber=yes'
                        ]
            cmd = ' '.join(cmd_list)
            print(cmd)
            os.system(cmd)
        else:
            print(self.p2simput, 'already exists!')
            return

    def runSIXTE_resolve(self, p2evt, RA_pnt, DEC_pnt, texp, xmldir='$SIXTE/share/sixte/instruments/xrism'):
        if not os.path.isfile(p2evt):
            cmd_list = ['xifupipeline',
                'XMLFile=%s/resolve/resolve_baseline_GVclosed.xml'%xmldir,
                'AdvXml=%s/resolve/resolve_detector.xml'%xmldir,
                'Simput=%s'%self.p2simput,
                'EvtFile=%s'%p2evt,
                'RA=%.8f Dec=%.8f'%(RA_pnt, DEC_pnt),
                'Exposure=%d'%texp
                        ]

            cmd = ' '.join(cmd_list)
            print(cmd)
            os.system(cmd)

            # radec2xy adds WCS coordinates to an event file
            cmd_list = ['radec2xy',
                        'EvtFile=%s' % p2evt,
                        'RefRA=%.8f RefDec=%.8f' % (RA_pnt, DEC_pnt),
                        'Projection = TAN'
                        ]
            cmd = ' '.join(cmd_list)
            print(cmd)
            os.system(cmd)


        else:
            print(p2evt, 'already exists!')


    def runSIXTE_xtend(self, p2evt, RA_pnt, DEC_pnt, texp, xmldir='$SIXTE/share/sixte/instruments/xrism'):

        if not os.path.isfile(p2evt):

            cmd_list = ['runsixt',
                        'XMLFile=%s/xtend/xtend_ccd2.xml' % xmldir,
                        'Simput=%s' % self.p2simput,
                        'EvtFile=%s' % p2evt,
                        'RA=%.8f Dec=%.8f' % (RA_pnt, DEC_pnt),
                        'Exposure=%d' % texp
                        ]

            cmd = ' '.join(cmd_list)
            print(cmd)
            os.system(cmd)

            # radec2xy adds WCS coordinates to an event file
            cmd_list = ['radec2xy',
                        'EvtFile=%s' % p2evt,
                        'RefRA=%.8f RefDec=%.8f' % (RA_pnt, DEC_pnt),
                        'Projection = TAN'
                        ]
            cmd = ' '.join(cmd_list)
            print(cmd)
            os.system(cmd)
        else:
            print(p2evt, 'already exists!')


    def createIMAGE_resolve(self, p2evt, p2img, RA_pnt, DEC_pnt):
        if not os.path.isfile(p2img):
            cmd_list = ['$SIXTE/bin/imgev',
                'EvtFile=%s'%p2evt,
                'Image=%s'%p2img,
                'CoordinateSystem=0 Projection=TAN',
                'NAXIS1=6 NAXIS2=6',
                'CUNIT1=deg CUNIT2=deg',
                'CRVAL1=%.8f CRVAL2=%.8f'%(RA_pnt, DEC_pnt),
                'CRPIX1=3.5 CRPIX2=3.5',
                'CDELT1=-85.12516e-04 CDELT2=85.12516e-04',
                'history=true clobber=yes'
            ]

            cmd = ' '.join(cmd_list)
            print(cmd)
            os.system(cmd)
        else:
            print(p2img, 'already exists!')

    def createIMAGE_xtend(self, p2evt, p2img, RA_pnt, DEC_pnt):
        if not os.path.isfile(p2img):
            cmd_list = ['$SIXTE/bin/imgev',
                'EvtFile=%s'%p2evt,
                'Image=%s'%p2img,
                'CoordinateSystem=0 Projection=TAN',
                'NAXIS1=640 NAXIS2=640',
                'CUNIT1=deg CUNIT2=deg',
                'CRVAL1=%.8f CRVAL2=%.8f'%(RA_pnt, DEC_pnt),
                'CRPIX1=473.34 CRPIX2=473.34',
                'CDELT1=-4.9110668e-04 CDELT2=4.9110668e-04',
                'history=true clobber=yes'
            ]

            cmd = ' '.join(cmd_list)
            print(cmd)
            os.system(cmd)
        else:
            print(p2img, 'already exists!')

    def extractSPECTRUM_resolve(self, p2evt, p2spec, xmldir='$SIXTE/share/sixte/instruments/xrism'):
        if not os.path.isfile(p2spec):
            cmd_list = ['$SIXTE/bin/makespec',
              'EvtFile=%s'%p2evt,
              'Spectrum=%s'%p2spec,
              'RSPPath=%s/resolve'%xmldir,
              'clobber=yes',
                        ]

            cmd = ' '.join(cmd_list)
            print(cmd)
            os.system(cmd)

        else:
            print(p2spec, 'already exists!')

