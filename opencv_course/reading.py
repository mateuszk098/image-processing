import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("images/cat.jpg")
cv2.imshow("cat", img)
cv2.waitKey(0)  # wait for any key
cv2.destroyAllWindows()  # close the image window

vid = cv2.VideoCapture("videos/dog.mp4")

while True:
    ret, frame = vid.read()
    if ret:
        cv2.imshow("dog", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

vid.release()
cv2.destroyAllWindows()
