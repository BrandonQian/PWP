import cv2
import numpy

for x in range(2):
    name = "IMG-548{0}.png".format(x+7)
    image = cv2.imread(name)
    dimension = int(image.shape[1]/4),int(image.shape[0]/4)
    image = cv2.resize(image, dimension, interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    # cv2.imshow("asdsa", gray)
    # cv2.waitKey(0)
    edges = cv2.Canny(gray,200,200,None,3)
    # cv2.imshow("asdsa", edges)
    # cv2.waitKey(0)
    blur = cv2.blur(edges,(15,15))
    # cv2.imshow("asdsa", blur)
    # cv2.waitKey(0)
    thresh1 = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)[1]
    cv2.imshow("asdsa", thresh1)
    cv2.waitKey(0)

    # mask = numpy.ones(thresh1.shape, dtype=numpy.uint8)
    # mask.fill(0)
    # cv2.imshow("asdsa",mask)
    # cv2.waitKey(0)
    #
    # zaa = 745*4/5
    # four = 745
    # eight = 1008
    # # points to be cropped
    # roi_corners = numpy.array([[(0, zaa), (eight, zaa), (eight, four), (0, four)]], dtype=numpy.int32)
    # # fill the ROI into the mask
    # cv2.fillPoly(mask, roi_corners, 0)
    # # applying th mask to original image
    # masked_image = cv2.bitwise_or(thresh1, mask)
    y,x = image.shape[0:2]
    print(x)
    print(y)
    ything = round(y/5)
    for z in range(5):
        masked_image = thresh1[4*ything-ything*z:y-ything*z,0:x]
        cv2.imshow("asdsa",masked_image)
        cv2.waitKey(0)

        lines = cv2.HoughLinesP(masked_image, rho=1, theta=numpy.pi / 180, threshold=100, minLineLength=100, maxLineGap=1700)
        # if lines is None:
        #     lines = cv2.HoughLinesP(masked_image, rho=1, theta=numpy.pi / 180, threshold=1000, minLineLength=900, maxLineGap=1000)
        if lines is not None:
            for i in range(len(lines)):
                line = lines[i][0]
                # cv2.line(image, (line[0], line[1]+4*ything-ything*z), (line[2], line[3]+4*ything-ything*z), (0, 0, 255), 1, cv2.LINE_AA)
        l1p1 = [1, 1]
        l1p2 = [1, 1]
        l1p1[0], l1p1[1], l1p2[0], l1p2[1] = lines[0][0]
        l2p1 = [1, 1]
        l2p2 = [1, 1]
        l2p1[0], l2p1[1], l2p2[0], l2p2[1] = lines[round(i / 2)][0]
        print(i)
        # l1p1

        lst1 = (l1p1, l1p2)
        print(lst1)
        slst1 = sorted(lst1, key=lambda x: x[1])
        print(slst1)
        lst2 = (l2p1, l2p2)
        print(lst2)
        slst2 = sorted(lst2, key=lambda x: x[1])
        print(slst2)

        cv2.arrowedLine(image, (int((slst1[1][0] + slst2[1][0]) / 2), int((slst1[1][1] + slst2[1][1]) / 2)+4*ything-ything*z),
                        (int((slst1[0][0] + slst2[0][0]) / 2), int((slst1[0][1] + slst2[0][1]) / 2)+4*ything-ything*z), (0, 0, 255), 5,
                        cv2.LINE_AA)
        # LinesImage = cv2.resize(image, dimension, interpolation=cv2.INTER_AREA)
        # image = cv2.resize(image, dimension, interpolation=cv2.INTER_AREA)
        cv2.imshow("asdsa", image)

        # snes = 15
        # white = cv2.inRange(thresh1, numpy.array([0, 0, 255-snes]), numpy.array([255, snes, 255]))
        # circle = cv2.circle(image, cv2.findNonZero(white)[0][0], 20, (255, 0, 0), 2)
        # cv2.imshow("image", circle)

        # cv2.imwrite("Lines of {0}".format(name),LinesImage)
        # cv2.imshow("output",LinesImage)
        cv2.waitKey(0)
