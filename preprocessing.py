import cv2

img = cv2.imread('test 5.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
cv2.imshow('Original Image',img)
cv2.imshow('Thresh Image',thresh1)
# cv2.waitKey(0)


def get_contour_precedence(contour, cols):
    tolerance_factor = 61
    origin = cv2.boundingRect(contour)
    return ((origin[1] // tolerance_factor) * tolerance_factor) * cols + origin[0]

n = 13
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (n, n))
dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)
contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
                                       cv2.CHAIN_APPROX_NONE)
im2 = img.copy()
contours.sort(key=lambda x: get_contour_precedence(x, thresh1.shape[1]))

for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    area = cv2.contourArea(cnt)
    # print(area)
    if area < 400:
        continue
    im2 = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 100, 255), 2)
    # temp = cv2.bitwise_not(thresh1[y:y + h, x:x + w])
    # reactant += find_character(thresh1[y:y + h, x:x + w], im2)

cv2.imshow('Detected Image',im2)

cv2.waitKey(0)
cv2.destroyAllWindows()








