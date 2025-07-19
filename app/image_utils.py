from PIL import Image
import numpy as np

# load image, resize, and create a 2d array of rgb pixels
def load_and_preprocess_image(image_path, resize_to=(200, 200)):
    # load image and convert image to RGBA color mode
    im = Image.open(image_path).convert('RGBA')

    # print("Image size before resizing:", im.size)

    # resize image to default 200x200 pixels
    im = im.resize(resize_to)

    # convert image to numpy array
    im_array = np.array(im)

    # reshaping image array to flat list of pixels 
    # keep only RGB values (ignore alpha)
    mask = im_array[:, :, 3] > 0 
    rgb_pixels = im_array[:, :, :3][mask]

    return rgb_pixels


