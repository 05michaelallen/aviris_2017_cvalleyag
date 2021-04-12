#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 15:04:17 2021

@author: vegveg
"""


import os
import rasterio as rio
import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# helper functions  
# =============================================================================
def import_image(imgfn):
    """import the AVIRIS image

    Parameters
    ----------
    img : img
        relative path to image

    Returns
    -------
    img : array
        numpy array of bands x rows x columns
    metadata : dict
        dictionary of metadata
    
    """
    r = rio.open(imgfn)
    metadata = r.meta.copy()
    img = r.read()
    
    return img, metadata
    

def filter_baddata(img, nodatavalues):
    """Filters no data values. Returns float32 numpy array.
    

    Parameters
    ----------
    img : array
        numpy array of bands x rows x columns
    nodatavalues : list
        list of bad data values

    Returns
    -------
    img: array
        float32 numpy array of same dimensions as input, bad values masked as nan

    """
    if img.dtype != 'float32':
        img = img.astype(np.float32)
    for val in nodatavalues:
        img[img == val] = np.nan
    return img


def filter_erroneousdata(img, minval, maxval):
    """Filters values outside of the range of possible values. Returns float32 numpy array.
    

    Parameters
    ----------
    img : array
        numpy array of bands x rows x columns
    minval : int
        minimum reflectance value
    maxval : int
        maximum reflectance value

    Returns
    -------
    img: array
        float32 numpy array of same dimensions as input, bad values masked as nan

    """
    if img.dtype != 'float32':
        img = img.astype(np.float32)
    img[img > maxval] = np.nan
    img[img < minval] = np.nan
    return img


def plot_VI(vi, vi_name, minval, maxval, cmap = plt.cm.viridis, output = False, *args):
    """ Plot the VI (note: this is not a geospatial plot, simply a heatmap)
    

    Parameters
    ----------
    vi : numpy array
        VI image
    vi_name : str
        Name of VI
    minval : int
        minimum VI value
    maxval : int
        maximum VI value
    cmap : matplotlib/colorcet/cmocean colormap object
        colormap. The default value is plt.cm.viridis.
    output : Boolean
        do you want to output the plot? The default value is False.
    Returns
    -------
    
    Plot (or output) of the VI.

    """
    fig, ax = plt.subplots(1, 1, figsize = [4.5, 6])
    try:
        a = ax.imshow(vi[0], vmin = minval, vmax = maxval, cmap = cmap)
        plt.colorbar(a, ax = ax, label = vi_name)
        plt.show()
    except:
        print("Error. The first dimension of the VI array is likely >1. Shape should be band*row*col")
    
    
def output_VI(vi, metadata, outfn):
    """Output the VI as a tif
    

    Parameters
    ----------
    outfn : numpy array
        VI image
    metadata : dict
        dictionary with image metadata (from Rasterio)
    outfn : str
        path + name for output

    Returns
    -------
    None.

    """
    try:
        with rio.open(outfn, mode = 'w', **metadata) as dst:
            dst.write(vi)
    except:
        print("Error. The first dimension of the VI array is likely >1. Shape should be band*row*col")