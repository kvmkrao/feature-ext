import cv2 

image = cv2.imread("Tank64229left.png")
#image = cv2.imread("Test1.png")

# grayscale the image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.imwrite("gray_tank64229.png",gray)
# apply a Gaussian blur
blur = cv2.GaussianBlur(gray, (5, 5), 0)
# threshold the image
(t, binary) = cv2.threshold(blur, 100, 255, cv2.THRESH_BINARY)
# find contours
(_, contours, _) = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
image_cropped_contoured_drawn = cv2.drawContours(image.copy(), contours, -1, (0, 255, 0), 3)
cv2.imwrite("exploration.jpg", image_cropped_contoured_drawn)

f = open('co_ordinates.txt', 'w+')
for c in range(len(contours)):
    n_contour = contours[c]
    for d in range(len(n_contour)):
        XY_Coordinates = n_contour[d]
        print(XY_Coordinates)
        f.write("%s\n" % (XY_Coordinates))
