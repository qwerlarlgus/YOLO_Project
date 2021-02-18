import sys
import numpy as np
import cv2

frame = cv2.imread('crop1.jpg')

hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

# Every color except white & Green
low = np.array([119, 100, 80]) #  0, 42, 0 - white
high = np.array([139, 120, 100])
mask = cv2.inRange(hsv_frame, low, high)
result = cv2.bitwise_and(frame, frame, mask=mask)

result1 = cv2.cvtColor(result, cv2.COLOR_RGB2GRAY)

ret, binary = cv2.threshold(result1, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
#ret, binary = cv2.threshold(result1, 70, 255, cv2.THRESH_BINARY )
#print(ret,binary)
binary = cv2.bitwise_not(binary)

cv2.imshow('Image', frame)
cv2.imshow('Result', result1)
cv2.imshow('Binary', binary)
cv2.waitKey(0)
cv2.destroyAllWindows()