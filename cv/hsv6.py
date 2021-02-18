import sys
import numpy as np
import cv2
import random

frame = cv2.imread('crop1.jpg')

hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

# Every color except white & Green
low = np.array([119, 100, 80]) #  0, 42, 0 - white
high = np.array([139, 120, 100])
mask = cv2.inRange(hsv_frame, low, high)
result = cv2.bitwise_and(frame, frame, mask=mask)

result = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)

ret, binary = cv2.threshold(result, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
binary = cv2.bitwise_not(binary)

h, w = binary.shape[:2]
dst1 = np.zeros((h, w, 3), np.uint8)
dst2 = np.zeros((h, w, 3), np.uint8)

_, src_bin = cv2.threshold(binary, 0, 255, cv2.THRESH_OTSU)

# 외곽선 검출
contours1, _ = cv2.findContours(src_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
contours2, _ = cv2.findContours(src_bin, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
print(len(contours1), contours1)
print(len(contours2), contours2)


for i in range(len(contours1)):
    c = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    cv2.drawContours(dst1, contours1, i, c, 1)

for i in range(len(contours2)):
    c = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    cv2.drawContours(dst2, contours2, i, c, 1)


cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.imshow('src_bin', src_bin)
cv2.waitKey(0)
cv2.destroyAllWindows()