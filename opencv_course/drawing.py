import cv2
import matplotlib.pyplot as plt
import numpy as np

blank_img = np.zeros(shape=(512, 512, 3), dtype=np.uint8)
# cv2.imshow("blank", blank_img)

cat_img = cv2.imread("images/cat.jpg")
# cv2.imshow("cat", cat_img)

cv2.rectangle(blank_img, pt1=(0, 0), pt2=(256, 256), color=(0, 255, 0), thickness=2)
# cv2.imshow("rectangle", blank_img)

# Open circle.
cv2.circle(blank_img, center=(256, 256), radius=100, color=(0, 0, 255), thickness=2)
# cv2.imshow("circle", blank_img)

# Closed circle.
cv2.circle(blank_img, center=(256, 256), radius=100, color=(0, 0, 255), thickness=-1)
# cv2.imshow("circle", blank_img)

cv2.line(blank_img, pt1=(0, 0), pt2=(256, 256), color=(255, 255, 255), thickness=2)
# cv2.imshow("line", blank_img)

cv2.putText(
    blank_img,
    text="Hello",
    org=(256, 256),
    fontFace=cv2.FONT_HERSHEY_TRIPLEX,
    fontScale=1.0,
    color=(255, 255, 255),
    thickness=2,
)
cv2.imshow("text", blank_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
