import cv2

img = cv2.imread('test.jpg')

# print(img.shape)
# img = cv2.resize(img, (200, 200))
# print(img.shape)

cv2.imshow('Result', img)
cv2.waitKey(0)