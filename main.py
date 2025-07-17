from app.image_utils import load_and_preprocess_image

pixels = load_and_preprocess_image("yarn_color_extractor/test_images/HangingPot.jpeg", resize_to=(200, 200))

print("Pixel array shape:", pixels.shape)
print("First 5 pixels:", pixels[:5])