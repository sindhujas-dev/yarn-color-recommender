from PIL import Image
import numpy as np

# load image, resize, and create a 2d array of rgb pixels
def load_and_preprocess_image(image_path, resize_to=(200, 200)):
    # load image and convert image to RGB color mode
    im = Image.open(image_path).convert('RGB')

    # print("Image size before resizing:", im.size)

    # resize image to default 200x200 pixels
    im = im.resize(resize_to)

    # convert image to numpy array
    im_array = np.array(im)

    # reshaping image array to flat list of pixels 
    # ex: (200x200=40000 pixels, 3 RGB values per pixel)
    pixels = im_array.reshape(-1, 3)

    return pixels


