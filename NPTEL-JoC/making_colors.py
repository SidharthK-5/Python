import numpy as np
from PIL import Image

width = 5
height = 4

array = np.zeros([height, width, 3], dtype=np.uint8)
image = Image.fromarray(array)
# image.save("data/black_image.png")  # This will create a black image

array_1 = np.zeros([100, 200, 3], dtype=np.uint8)
array_1[:, :100] = [255, 128, 0]  # Orange
array_1[:, 100:] = [0, 0, 255]  # Blue
image_1 = Image.fromarray(array_1)
image_1.save(
    "data/orange_blue.png"
)  # This will create an image with left half orange and right half blue
