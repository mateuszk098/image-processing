import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("images/park.jpg")


# -x --> Left
# -y --> Up
# +x --> Right
# +y --> Down
def translate(img, x, y):
    matrix = np.array([[1, 0, x], [0, 1, y]], dtype=np.float32)
    dims = (img.shape[1], img.shape[0])
    return cv2.warpAffine(img, matrix, dims)


def rotate(img, angle, rot_point=None):
    height, width = img.shape[:2]
    if rot_point is None:
        rot_point = (width // 2, height // 2)

    matrix = cv2.getRotationMatrix2D(rot_point, angle, scale=1.0)
    dims = (width, height)
    return cv2.warpAffine(img, matrix, dims)


translated_img = translate(img, 100, 100)
cv2.imshow("translated", translated_img)

rotated_img = rotate(img, 45)
cv2.imshow("rotated", rotated_img)

# Flipping.
# 0 --> Vertically.
# 1 --> Horizontally.
# -1 --> Both.
flip_img = cv2.flip(img, flipCode=0)  # Vertically.
cv2.imshow("flip", flip_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
