""" Module with routines for finding outliers
"""

from pathlib import Path
import nibabel as nib
import numpy as np


def detect_outliers(fname):
    """ Return outlier indices for image
    

    Parameters
    ----------
    fname : str
        Image file name.

    Returns
    -------
    list
        volume numbers of outliers.

    """
    img = nib.load(fname)
    data = img.get_fdata()
    
    overall_mean = np.mean(data)
    overall_std = np.std(data)
    thresh = overall_std*2
    
    means = np.mean(data,axis=3)

    is_outlier = (means-overall_mean) < -thresh
    indices = np.where(is_outlier)[0]
       
    return indices.tolist()


def find_outliers(data_directory):
    """ Return filenames and outlier indices for images in `data_directory`.

    Parameters
    ----------
    data_directory : str
        Directory containing containing images.

    Returns
    -------
    outlier_dict : dict
        Dictionary with keys being filenames and values being lists of outliers
        for filename.
    """
    image_fnames = Path(data_directory).glob('**/sub-*.nii.gz')
    outlier_dict = {}
    for fname in image_fnames:
        outliers = detect_outliers(fname)
        outlier_dict[fname] = outliers
    return outlier_dict
