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
    
    
