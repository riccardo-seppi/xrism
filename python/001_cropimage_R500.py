from astropy.io import fits
from astropy.wcs import WCS
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Read the FITS image
p2data = '/home/riccardo/xrism/A1689/data/csm_sb.fits'
p2out = p2data.split('.fits')[0]+'_cropR500.fits'
hdul = fits.open(p2data)
image_data = hdul[0].data

wcs = WCS(hdul[0].header)
# Step 2: Define circular region parameters
# Define the center coordinates and radius in RA, DEC, and arcminutes
center_ra = 197.87233
center_dec = -1.341345
radius_arcmin = 7.59

# Convert the center coordinates to pixel coordinates
center_pixel = wcs.world_to_pixel_values(center_ra, center_dec)

# Convert the radius from arcminutes to degrees
radius_deg = radius_arcmin / 60.0

# Convert the radius from degrees to pixels
radius_pixel = radius_deg / np.abs(wcs.wcs.cdelt[0])

# Define the circular region in pixel coordinates
x_center_pixel, y_center_pixel = center_pixel
x_indices, y_indices = np.indices(hdul[0].data.shape)
mask = (x_indices - x_center_pixel)**2 + (y_indices - y_center_pixel)**2 <= radius_pixel**2

# Step 4: Apply the mask to crop the image
cropped_image = image_data.copy()  # Make a copy to preserve original data
cropped_image[~mask] = np.nan  # Mask out pixels outside the circular region

hdul_new = fits.HDUList(fits.PrimaryHDU(data=cropped_image, header=hdul[0].header))
hdul_new.writeto(p2out)

# Step 5: Save or display the cropped image
#plt.imshow(cropped_image, origin='lower', cmap='viridis')
#plt.colorbar(label='Intensity')
#plt.title('Cropped Image')
#plt.xlabel('X')
#plt.ylabel('Y')
#plt.show()
