# Yarn Color Recommendation System (in progress)

This color recommender system is a Python-based tool that extracts dominant yarn colors from crochet project images. The system uses machine learning and computer vision techniques to help crocheters easily identify and replicate color palettes 

---

## Project Overview

The goal of this project is to analyze an image (such as a handmade crochet piece or pattern reference), preprocess the image, and extract the most prominent yarn colors using clustering. This allows crafters to match or recreate palettes from inspiration images. 

---

## Features

- **Background Removal**: Automatically isolates the yarn region using transparency masking and the rembg library.
- **Color Clustering**: Extracts the top N dominant yarn colors using KMeans clustering.
- **Color Swatch Visualization**: Plots color swatches of the extracted colors for easy viewing.
- **Modular Code**: Uses an `image_utils.py` module to streamline preprocessing.

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