import cv2
import matplotlib.pyplot as plt
import numpy as np


def rescale_frame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    return cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)


vid = cv2.VideoCapture("videos/dog.mp4")

while True:
    ret, frame = vid.read()
    if ret:
        frame_resized = rescale_frame(frame, scale=0.75)
        cv2.imshow("dog", frame)
        cv2.imshow("dog_resized", frame_resized)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

vid.release()
cv2.destroyAllWindows()
