from app.image_utils import load_and_preprocess_image

pixels = load_and_preprocess_image("yarn_color_extractor/test_images/HangingPot.jpeg", resize_to=(200, 200))

print("Pixel array shape:", pixels.shape)
print("First 5 pixels:", pixels[:5])

# __init__.py	 - Makes this a Python package (you can import from app)
# image_utils.py - Loads and preprocesses images (resizing, converting to arrays, etc.)
# color_clustering.py	- Runs KMeans to find dominant colors in the image
# color_theory.py	- Uses simple color rules (complementary, analogous, etc.) to recommend yarn pairings
# ui_streamlit.py	- Code for your interactive web app UI (only needed on Day 3)

# data - includes datasets
# test_images - sample images to train with
# main.py - Run the pipeline from the command line, Call functions from your app/ files, Good for testing logic before building the UI