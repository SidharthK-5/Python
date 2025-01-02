"""
Program to flip an image vertically
"""

from PIL import Image

img = Image.open("data/naruto.jpg")
img.show()

flipped_img = img.transpose(Image.DEFAULT_STRATEGY)
flipped_img.show()
flipped_img.save("data/naruto_flipped.jpg")
