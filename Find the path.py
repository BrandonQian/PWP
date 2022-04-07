import cv2
import numpy

for x in range(1):
    name = "IMG_5487.png"#{0}.png".format(x+6)
    image = cv2.imread(name)
    dimension = int(image.shape[1]/4),int(image.shape[0]/4)
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imshow("asdsa", gray)
    cv2.waitKey(0)
    edges = cv2.Canny(gray,170,170,None,3)
    cv2.imshow("asdsa", edges)
    cv2.waitKey(0)
    blur = cv2.blur(edges,(25,25))
    cv2.imshow("asdsa", blur)
    cv2.waitKey(0)
    thresh1 = cv2.threshold(edges, 100, 255, cv2.THRESH_BINARY_INV)[1]
    cv2.imshow("asdsa", thresh1)
    cv2.waitKey(0)


    # white = cv2.inRange(image, numpy.array([200, 200, 200]), numpy.array([255, 255, 255]))
    # circle = cv2.circle(image, cv2.findNonZero(white)[0][0], 20, (255, 0, 0), 2)
    # cv2.imshow("image", circle)
    # # cv2.imwrite("Lines of {0}".format(name),LinesImage)
    # # cv2.imshow("output",LinesImage)
    # cv2.waitKey(0)
