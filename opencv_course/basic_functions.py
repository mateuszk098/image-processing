import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("images/cat.jpg")
# cv2.imshow("cat", img)

# Convert to grayscale.
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow("gray", gray_img)

# Blur.
blur_img = cv2.GaussianBlur(img, ksize=(5, 5), sigmaX=1.0, sigmaY=1.0, borderType=cv2.BORDER_DEFAULT)
# cv2.imshow("blur", blur_img)

# Edge Cascade
canny_img = cv2.Canny(blur_img, threshold1=125, threshold2=175)
cv2.imshow("canny", canny_img)

# Dilating.
dilated_img = cv2.dilate(canny_img, kernel=(3, 3), iterations=1)  # type: ignore
cv2.imshow("dilated", dilated_img)

# Eroding.
eroded_img = cv2.erode(canny_img, kernel=(3, 3), iterations=1)  # type: ignore
cv2.imshow("eroded", eroded_img)

# Resizing.
resized_img = cv2.resize(img, dsize=(512, 512), interpolation=cv2.INTER_AREA)
# cv2.imshow("resized", resized_img)

# Cropping
cropped_img = img[50:200, 200:400]
cv2.imshow("cropped", cropped_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
