import cv2
import numpy

for x in range(2):
    name = "IMG-548{0}.png".format(x+7)
    image = cv2.imread(name)
    dimension = int(image.shape[1]/4),int(image.shape[0]/4)
    image = cv2.resize(image, dimension, interpolation=cv2.INTER_AREA)
    cv2.imshow("Cool Image", image)
    cv2.waitKey(0)
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,200,200,None,3)
    blur = cv2.blur(edges,(15,15))
    thresh1 = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)[1]

    ex = []
    #try dictionary
    
    y,x = image.shape[0:2]
    print(x)
    print(y)
    ything = round(y/5)
    for z in range(5):
        masked_image = thresh1[4*ything-ything*z:y-ything*z,0:x]
        lines = cv2.HoughLinesP(masked_image, rho=1, theta=numpy.pi / 180, threshold=100, minLineLength=100, maxLineGap=1700)
        if lines is not None:
            for i in range(len(lines)):
                ex.append(lines[i][0][0])
                #make this dictionary and assign each x value to i
        
        print(ex)
        print(sorted(ex))
        #find lowest and highest ex and use their i value
        #print it and find out how to apply it to the other stuff

        print("1\n")
        lst1 = (lines[0][0][0:2], lines[0][0][2:4])
        print(lst1[1])
        slst1 = sorted(lst1, key=lambda x: x[1])
        print(slst1[1])
        print("2\n")
        lst2 = (lines[round(i/2)][0][0:2], lines[round(i/ 2)][0][2:4])
        print(lst2[1])
        slst2 = sorted(lst2, key=lambda x: x[1])
        print(slst2[1])

        cv2.arrowedLine(image, (int((slst1[1][0] + slst2[1][0]) / 2), int((slst1[1][1] + slst2[1][1]) / 2)+4*ything-ything*z),(int((slst1[0][0] + slst2[0][0]) / 2), int((slst1[0][1] + slst2[0][1]) / 2)+4*ything-ything*z), (0, 0, 255), 5,cv2.LINE_AA)
        cv2.imshow("Cool Image", image)
        cv2.imwrite("Path of {0}".format(name),image)
        cv2.waitKey(0)
