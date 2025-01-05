"""
Image enhancing using CLAHE
"""

import cv2

img = cv2.imread("data/low_contrast.jpg")
clahe = cv2.createCLAHE()

# Convert to gray scale
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Apply CLAHE
enhanced = clahe.apply(gray_image)
cv2.imwrite("data/low_contrast_enhanced.jpg", enhanced)