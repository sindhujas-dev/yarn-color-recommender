# import rembg to remove background
from rembg import remove

# import libraries for image processign and visualization
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import os

# variables for file paths and parameters
input_path = "yarn_color_extractor/test_images/HangingPot.jpeg"
output_path = "yarn_color_extractor/bg_removed_images/HangingPot_no_bg.png"
top_n_colors = 5
save_hex_path = "yarn_color_extractor/color_results.txt"

# 1. remove background from an image
# read input image as bytes
with open(input_path, "rb") as input_file:
    input_data = input_file.read()

# remove background
output_data = remove(input_data)

# save result as a PNG with transparent background
with open(output_path, "wb") as output_file:
    output_file.write(output_data)

print(f"✅ Background removed and saved to {output_path}")

# ---------------------------------------------------------------