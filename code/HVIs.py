#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 14:36:48 2021

@author: vegveg
"""

import rasterio as rio
import numpy as np

# =============================================================================
# functions for each VI 
# =============================================================================
def simple_ratio(img, red, nir):
    """Calculates a simple ratio VI for an image
    

    Parameters
    ----------
    img : array
        image to calculate VI on, must have dimensions row x columns
    red : int
        band index for red (660nm)
    nir : int
        band index for nir (830nm)

    Returns
    -------
    simple_ratio : array
        numpy array with rows x columns of simple ratio

    """
    simple_ratio = img[nir]/img[red]
    return simple_ratio[None,:,:]
    
    
def evi(img, red, nir, blue):
    """Calculates enhanced vegetation index (EVI) for an image
    

    Parameters
    ----------
    img : array
        image to calculate VI on, must have dimensions row x columns
    red : int
        band index for red (660nm)
    nir : int
        band index for nir (830nm)
    blue : int
        band index for blue (480nm)

    Returns
    -------
    evi : array
        numpy array with rows x columns of the VI

    """
    evi = 2.5*(img[nir]-img[red])/(img[nir] + 6 * img[red] - 7.5 * img[blue] + 1)
    return evi[None,:,:]
    
    
def mcari(img, b700, b670, b550):
    """Calculates a XXX for an image
    

    Parameters
    ----------
    img : array
        image to calculate VI on, must have dimensions row x columns
    b700 : int
        band index for 700nm
    b670 : int
        band index for 670nm
    b550 : int
        band index for 550nm

    Returns
    -------
    mcari : array
        numpy array with rows x columns of the VI

    """
    mcari = ((img[b700] - img[b670]) - 0.2 * (img[b700] - img[b550])) * img[b700]/img[b670]
    return mcari[None,:,:]
    

def msi(img, nir, swir):
    """Calculates a moisture stress index (MSI) for an image
    

    Parameters
    ----------
    img : array
        image to calculate VI on, must have dimensions row x columns
    nir : int
        band index for nir (830nm)
    swir1 : int
        band index for swir1 (1650nm)

    Returns
    -------
    msi : array
        numpy array with rows x columns of the VI

    """
    msi = img[swir]/img[nir]
    return msi[None,:,:]
