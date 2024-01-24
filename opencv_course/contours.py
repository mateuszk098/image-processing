import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("images/cats.jpg")
# cv2.imshow("cats", img)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow("gray", gray_img)

blur_img = cv2.GaussianBlur(gray_img, ksize=(7, 7), sigmaX=1.0, sigmaY=1.0, borderType=cv2.BORDER_DEFAULT)
canny_img = cv2.Canny(blur_img, threshold1=125, threshold2=175)
cv2.imshow("canny", canny_img)

# ret, thresh = cv2.threshold(gray_img, 125, 255, cv2.THRESH_BINARY)
# cv2.imshow("thresh", thresh)

contours, hierarchies = cv2.findContours(canny_img, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_NONE)
print(f"Found {len(contours)} contours.")

blank_img = np.zeros_like(img, dtype=np.uint8)
cv2.drawContours(blank_img, contours=contours, contourIdx=-1, color=(0, 0, 255), thickness=1)
cv2.imshow("contours drawn", blank_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
