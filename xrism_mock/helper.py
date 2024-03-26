import os
from astropy.io import fits
from astropy.io.fits import Column
from astropy.time import Time
from datetime import date
def create_attitude(p2att, time, ra, dec, roll, tstart, tstop, mjdref):
    if os.path.isfile(p2att):
        print(p2att, 'already exists!')
        return
    col00 = Column(name='TIME', array=time, format='D', unit='s')
    col01 = Column(name='VIEWRA', array=ra, format='D', unit='deg')
    col02 = Column(name='VIEWDEC', array=dec, format='D', unit='deg')
    col03 = Column(name='ROLL', array=roll, format='D', unit='deg')

    coldefs = fits.ColDefs([col00, col01, col02, col03])
    hdu = fits.BinTableHDU.from_columns(coldefs)
    hdu.header['EXTNAME'] = 'ATT'
    hdu.header['TSTART'] = tstart  # 30.July
    hdu.header['TSTOP'] = tstop  # 30.July + 6months
    hdu.header['MJDREF'] = mjdref  # 1990-06-01 21:06:50
    #hdu.header['UTCZERO'] = '644274410'  # 1990-06-01 21:06:50

    head = fits.Header()
    head['MISSION'] = 'XRISM'
    head['HISTORY'] = 'Created on '+str(date.today())
    primary = fits.PrimaryHDU(data=None, header=head)

    hdul = fits.HDUList([primary, hdu])

    hdul.writeto(p2att, overwrite=True)
    print('Saved in', p2att)


def get_date_from_MJD(mjd_value):
    # Convert MJD value to a Gregorian calendar date
    target_date = Time(mjd_value, format='mjd', scale='utc').to_datetime()

    # Print the corresponding Gregorian calendar date
    print("Corresponding Gregorian calendar date:", target_date)
    return target_date

def get_MJD_from_date(gregorian_date):
    # Convert Gregorian calendar date to MJD
    mjd_value = Time(gregorian_date, scale='utc').mjd

    # Print the corresponding MJD value
    print("Corresponding MJD value:", mjd_value)
    return mjd_value