import numpy as np
from scipy.ndimage import convolve


def loadbayer(path):
    """ Load data from file

    Args:
        path: Path of the .npy file
    Returns:
        Data as numpy array (H,W)
    """
    #
    # You code here
    #


def separatechannels(bayerdata):
    """ Separate bayer data into RGB channels so that
    each color channel retains only the respective
    values given by the bayer pattern and missing values
    are filled with zero

    Args:
        bayerdata: Numpy array containing bayer data (H,W)
    Returns:
        red, green, and blue channel as numpy array (H,W)
    """
    #
    # You code here
    #


def assembleimage(r, g, b):
    """ Assemble separate channels into image

    Args:
        r: red channel as numpy array (H,W)
        g: green channel as numpy array (H,W)
        b: blue channel as numpy array (H,W)
    Returns:
        Image as numpy array (H,W,3)
    """
    #
    # You code here
    #


def interpolate(r, g, b):
    """ Interpolate missing values in the bayer pattern
    by using bilinear interpolation

    Args:
        r: red channel as numpy array (H,W)
        g: green channel as numpy array (H,W)
        b: blue channel as numpy array (H,W)
    Returns:
        Interpolated image as numpy array (H,W,3)
    """
    #
    # You code here
    #
