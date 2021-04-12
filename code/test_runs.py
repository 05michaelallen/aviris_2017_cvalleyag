#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 14:59:33 2021

@author: vegveg
"""

import os
import colorcet

# set wd to import functions from HVIs script
wd = "/home/vegveg/aviris_2017_cvalleyag/code"
imgfn = "../data/f170607t01p00r17_corr_v1g_img_clip_warp_sub.tif"
os.chdir(wd)

# import helper functions
from helper_functions import import_image, filter_erroneousdata, plot_VI, output_VI
# import VIs
from HVIs import simple_ratio, evi, mcari, msi

# =============================================================================
# run analyses (import image apply VIs)
# =============================================================================
# import image
r, metadata = import_image(imgfn)

# specify bands
red = 31
nir = 51
blue = 13
swir1 = 137
b700 = 38
b670 = 35
b550 = 20
 
# filter bad values
rf = filter_erroneousdata(r.copy(), 0, 1)

# run VIs
rf_simple_ratio = simple_ratio(rf, red, nir)
rf_evi = evi(rf, red, nir, blue)
rf_mcari = mcari(rf, b700, b670, b550)
rf_msi = msi(rf, nir, swir1)

# plot
plot_VI(rf_simple_ratio, "Simple Ratio", -1, 20, cmap = colorcet.cm.bgy)
plot_VI(rf_evi, "EVI", 0, 1, cmap = colorcet.cm.bgy)
plot_VI(rf_mcari, "MCARI", 0, 1, cmap = colorcet.cm.bgy)
plot_VI(rf_msi, "MSI", 0, 1, cmap = colorcet.cm.bgy)

# output
# modify metadata
metadata.update({'count' : 1})
outfn = "../data/VIs/f170607t01p00r17_corr_v1g_img_clip_warp_sub_simple_ratio.tif"
output_VI(rf_simple_ratio, metadata, outfn)
outfn = "../data/VIs/f170607t01p00r17_corr_v1g_img_clip_warp_sub_evi.tif"
output_VI(rf_evi, metadata, outfn)
outfn = "../data/VIs/f170607t01p00r17_corr_v1g_img_clip_warp_sub_mcari.tif"
output_VI(rf_mcari, metadata, outfn)
outfn = "../data/VIs/f170607t01p00r17_corr_v1g_img_clip_warp_sub_msi.tif"
output_VI(rf_msi, metadata, outfn)
