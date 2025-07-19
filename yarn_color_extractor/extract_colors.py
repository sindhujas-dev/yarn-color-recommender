# testing file for yarn color extractor

# import rembg to remove background
from rembg import remove

# for seeing the plot in the backend
import matplotlib
matplotlib.use("TkAgg") 

# import libraries for image processign and visualization
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# import custom function to load and preprocess image
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))
from image_utils import load_and_preprocess_image

# variables for file paths and parameters
input_path = "yarn_color_extractor/test_images/AppaBucketHat.jpeg"
output_path = "yarn_color_extractor/bg_removed_images/AppaBucketHat_no_bg.png"
top_n_colors = 5
save_hex_path = "yarn_color_extractor/color_results_files/color_results_appa.txt"

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

# 2. extract top N colors from the image
pixels = load_and_preprocess_image(output_path)

# use KMeans to find the top N colors
kmeans_model = KMeans(n_clusters=top_n_colors, random_state=42, n_init='auto')
kmeans_model.fit(pixels)

# get the top colors (cluster centers)
colors = kmeans_model.cluster_centers_.astype(int)

# function to display color swatches
def plot_colors(color_array):
    plt.figure(figsize=(8,2))
    for i, color in enumerate(color_array):
        plt.subplot(1, len(color_array), i + 1)
        plt.axis("off")
        swatch = np.ones((100, 100, 3), dtype=np.uint8) * color
        plt.imshow(swatch)
    plt.tight_layout()
    plt.show()

plot_colors(colors)

# conver RGB to hex format
def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(*rgb)
hex_colors = [rgb_to_hex(color) for color in colors]

# save hex values to a text file
with open(save_hex_path, "w") as f:
    for hex_color in hex_colors:
        f.write(hex_color + "\n")

print(f"🎨 Top {top_n_colors} colors saved to {save_hex_path}")
