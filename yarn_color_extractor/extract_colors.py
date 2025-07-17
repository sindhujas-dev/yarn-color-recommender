from rembg import remove

# set input and output image paths
input_path = "yarn_color_extractor/test_images/HangingPot.jpeg"
output_path = "yarn_color_extractor/bg_removed_images/HangingPot_no_bg.png"

# read input image as bytes
with open(input_path, "rb") as input_file:
    input_data = input_file.read()

# remove background
output_data = remove(input_data)

# save result as a PNG with transparent background
with open(output_path, "wb") as output_file:
    output_file.write(output_data)

print(f"✅ Background removed and saved to {output_path}")