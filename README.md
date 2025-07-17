__init__.py	 - Makes this a Python package (you can import from app)
image_utils.py - Loads and preprocesses images (resizing, converting to arrays, etc.)
color_clustering.py	- Runs KMeans to find dominant colors in the image
color_theory.py	- Uses simple color rules (complementary, analogous, etc.) to recommend yarn pairings
ui_streamlit.py	- Code for your interactive web app UI (only needed on Day 3)

data - includes datasets
test_images - sample images to train with
main.py - Run the pipeline from the command line, Call functions from your app/ files, Good for testing logic before building the UI

# Yarn Color Recommendation System (in progress)

This color recommender system is a Python-based tool that extracts dominant yarn colors from crochet project images. The system uses machine learning and computer vision techniques to help crocheters easily identify and replicate color palettes 

---

## Project Overview

The goal of this project is to analyze an image (such as a handmade crochet piece or pattern reference), preprocess the image, and extract the most prominent yarn colors using clustering. This allows crafters to match or recreate palettes from inspiration images. 

---

## Features

- 🎯 **Background Removal**: Automatically isolates the yarn region using transparency masking and the rembg library.
- 🎨 **Color Clustering**: Extracts the top N dominant yarn colors using KMeans clustering.
- 🖼️ **Color Swatch Visualization**: Plots color swatches of the extracted colors for easy viewing.
- 🔧 **Modular Code**: Uses an `image_utils.py` module to streamline preprocessing.

---

## Project Structure


---

## Tech Stack

- Python
- NumPy
- Pillow (PIL)
- scikit-learn
- matplotlib
- rembg

---