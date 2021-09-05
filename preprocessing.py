# import cv2
import numpy as np
from sliding_window import *

image = cv2.imread('test_images\\test 16.png')
# img = cv2.GaussianBlur(image, (5, 5), 0)
img = cv2.Canny(image, 0, 255)
img = cv2.bitwise_not(img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
print(img.shape)
cv2.imshow('Original Image', img)
# cv2.imshow('Thresh Image', thresh1)
thresh = cv2.bitwise_not(thresh1)

# def get_contour_precedence(contour, cols):
#     tolerance_factor = 61
#     origin = cv2.boundingRect(contour)
#     return ((origin[1] // tolerance_factor) * tolerance_factor) * cols + origin[0]


# n = 13
# rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (n, n))
# dilation = cv2.dilate(thresh1, rect_kernel, iterations=1)
# contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
#                                        cv2.CHAIN_APPROX_NONE)
im2 = img.copy()
# contours.sort(key=lambda x: get_contour_precedence(x, thresh1.shape[1]))
#
# for cnt in contours:
#     x, y, w, h = cv2.boundingRect(cnt)
#     area = cv2.contourArea(cnt)
#     # print(area)
#     if area < 400:
#         continue
#     im2 = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 100, 255), 2)
# temp = cv2.bitwise_not(thresh1[y:y + h, x:x + w])
# reactant += find_character(thresh1[y:y + h, x:x + w], im2)

# Detection of corner


des = cv2.cornerHarris(thresh, 4, 5, 0.07)
increase_shape(des.copy(), 'des')
des = cv2.dilate(des, None)
temp = img.copy()
# print(temp[des > 0.01 * des.max()])
# print('des: \n', des)
# print('des shape: ', des.shape)
temp[des > 0.01 * des.max()] = [0, 0, 0]
temp[des <= 0.01 * des.max()] = [255, 255, 255]
# temp = cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY)

# Making bounding lines 

contours, _ = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# print(len(contours))
print('Lengths of Approx:')
for cnt in contours[1:]:
    tem = []
    epsilon = 0.05 * cv2.arcLength(cnt, False)
    approx = cv2.approxPolyDP(cnt, epsilon, False)
    # for i in approx:
    #     tem.append(list(i[0]))
    # tem = np.array(tem).reshape((-1, 1, 2))
    cv2.polylines(temp, [approx], False, (0, 100, 255), 2)
    print(approx)
    # cv2.drawContours(img, [approx], 0, (0), 3)
    # print(len(approx))
# temp = cv2.approxPolyDP(temp, 0.23, False)
print(temp.shape)
increase_shape(temp, 'detected_image')

# cv2.imshow('Original Image', img)
# cv2.imshow('Detected Image', im2)

cv2.waitKey(0)
cv2.destroyAllWindows()
