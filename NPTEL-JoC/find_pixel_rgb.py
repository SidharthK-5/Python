"""
Load an image and find the RGB values of a specific pixel.
"""

from PIL import Image

image = Image.open("data/naruto.jpg")
rgb_image = image.convert("RGB")
red, green, blue = rgb_image.getpixel((100, 150))
print(f"Red: {red}, Green: {green}, Blue: {blue}")
