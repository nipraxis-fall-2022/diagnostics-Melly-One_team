""" Scan outlier metrics
"""

# Any imports you need
# +++your code here+++
import numpy as np
import nibabel as nib

def dvars(img):
    """ Calculate dvars metric on Nibabel image `img`

    The dvars calculation between two volumes is defined as the square root of
    (the mean of the (voxel differences squared)).

    Parameters
    ----------
    img : nibabel image

    Returns
    -------
    dvals : 1D array
        One-dimensional array with n-1 elements, where n is the number of
        volumes in `img`.
    """
    # Hint: remember 'axis='.  For example:
    # In [2]: arr = np.array([[2, 3, 4], [5, 6, 7]])
    # In [3]: np.mean(arr, axis=1)
    # Out[2]: array([3., 6.])
    #
    # You may be be able to solve this in four lines, without a loop.
    # But solve it any way you can.
    data = img.get_fdata()
    prev_vol = data[:,:,:,0:-1]
    this_vol = data[:,:,:,1:]
    vol_diff = this_vol-prev_vol
    dvar_val = np.sqrt(np.mean(vol_diff**2,axis=(0,1,2)))
    return dvar_val
