import streamlit as st
from PIL import Image
import numpy as np
from rembg import remove
import io

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.image_utils import load_and_preprocess_image
from app.color_clustering import extract_dominant_colors

st.set_page_config(page_title="Yarn Color Recommender", layout="centered")
st.title("🎨 Yarn Color Recommender")

uploaded_file = st.file_uploader("Upload an image of yarn", type=["jpg", "jpeg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

    # Read image as bytes
    image_bytes = uploaded_file.read()

    # Step 1: Remove background using rembg
    output_bytes = remove(image_bytes)
    image_no_bg = Image.open(io.BytesIO(output_bytes)).convert("RGBA")

    st.subheader("Image After Background Removal")
    st.image(image_no_bg, use_container_width=True)

    # Step 2: Extract pixels
    pixels = load_and_preprocess_image(image_no_bg)

    # Step 3: Choose number of colors
    top_n = st.slider("Number of colors to extract", 1, 10, 5)

    # Step 4: Extract dominant colors using KMeans
    colors = extract_dominant_colors(pixels, top_n)

    # Step 5: Show color swatches
    st.subheader("Dominant Colors")
    cols = st.columns(len(colors))
    for i, color in enumerate(colors):
        with cols[i]:
            hex_color = '#%02x%02x%02x' % tuple(color)
            st.markdown(
                f'''
                <div style="width: 80px; height: 80px; background-color: {hex_color}; border-radius: 10px;"></div>
                <p style="text-align:center;">{hex_color}</p>
                ''',
                unsafe_allow_html=True
            )

    # save colors as text
    if st.button("Save Hex Colors to File"):
        hex_colors = ['#{:02x}{:02x}{:02x}'.format(*c) for c in colors]
        hex_text = "\n".join(hex_colors)
        st.download_button("Download Hex Colors", hex_text, file_name="yarn_colors.txt", mime="text/plain")
