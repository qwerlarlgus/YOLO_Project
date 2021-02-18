import sys
import numpy as np
import cv2

#frame = cv2.imread('signal1.jpg')
frame = cv2.imread('tomato.jpg')

hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

# Red color
low_red = np.array([161,155,84])
high_red = np.array([179, 255, 255])
red_mask = cv2.inRange(hsv_frame, low_red, high_red)
red = cv2.bitwise_and(frame, frame, mask=red_mask)

# Blue color
low_blue = np.array([94, 80, 2])
high_blue = np.array([126, 255, 255])
blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
blue = cv2.bitwise_and(frame, frame, mask=blue_mask)

# Green color
low_green = np.array([25, 52, 72])
high_green = np.array([102, 255, 255])
green_mask = cv2.inRange(hsv_frame, low_green, high_green)
green = cv2.bitwise_and(frame, frame, mask=green_mask)

# Every color except white
low = np.array([0, 42, 0])
high = np.array([179, 255, 255])
mask = cv2.inRange(hsv_frame, low, high)
result = cv2.bitwise_and(frame, frame, mask=mask)

cv2.imshow('Image', frame)
#cv2.imshow('Blue mask', blue)
#cv2.imshow('Red mask', red)
cv2.imshow('Green mask', green)
cv2.waitKey(0)
cv2.destroyAllWindows()