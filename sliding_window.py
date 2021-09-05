import cv2
import imutils


def pyramid(image, scale=1.5, minSize=(30, 30)):
    yield image
    while True:
        w = int(image.shape[1] / scale)
        image = imutils.resize(image, width=w)
        if image.shape[0] < minSize[1] or image.shape[1] < minSize[0]:
            break

        yield image


def sliding_window(image, stepSize, windowSize):
    for y in range(0, image.shape[0], stepSize):
        for x in range(0, image.shape[1], stepSize):
            Y = y+windowSize[1]//2
            # X = x+windowSize[0]/2

            yield x, Y, image[y:y + windowSize[1], x:x + windowSize[0]]


# def check(image, texts, locations, x, y, multiplier):
    # temp = model(image)
    # if temp and (x*multiplier,y*multiplier) not in locations:
        # text = ocr_model(image)
        # texts.append(text)
        # locations.append((x*multiplier,y*multiplier))
    # else:
        # pass


def increase_shape(img,name):
    if img.shape < (50, 250, 3):
        img = cv2.resize(img, (img.shape[0] * 5, img.shape[1] * 2), interpolation=cv2.INTER_AREA)
    else:
        pass
    cv2.imshow(f'{name}', img)
