#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 14:59:33 2021

@author: vegveg
"""

import os

# set wd to import functions from HVIs script
wd = "/home/vegveg/aviris_2017_cvalleyag/code"
imgfn = "../data/f170607t01p00r17_corr_v1g_img_clip_warp_sub.tif"
os.chdir(wd)

# import helper functions
from helper_functions import import_image, filter_erroneousdata, plot_VI
# import VIs
from HVIs import simple_ratio

# =============================================================================
# run analyses (import image apply VIs)
# =============================================================================
# import image
r, metadata = import_image(imgfn)

# filter bad values
rf = filter_erroneousdata(r.copy(), 0, 1)

# run simple_ratio
rf_simple_ratio = simple_ratio(rf, 31, 51)

# plot it 
plot_VI(rf_simple_ratio, "Simple Ratio", -1, 20)
