import cv2
import numpy

for x in range(3):
    name = "paper{0}.png".format(x+1)
    img = cv2.imread(name)
    dimension = int(img.shape[1]/4),int(img.shape[0]/4)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,250,275,None,3)
    blur = cv2.blur(edges,(25,25))

    lines = cv2.HoughLinesP(blur,rho=1,theta=numpy.pi/180,threshold = 2100,minLineLength = 2700,maxLineGap = 1700)
    if lines is None:
        lines = cv2.HoughLinesP(blur,rho = 1,theta = numpy.pi/180,threshold = 1000,minLineLength = 900,maxLineGap = 1000)
    if lines is not None:
        for i in range(len(lines)):
            line = lines[i][0]
            cv2.line(img,(line[0],line[1]),(line[2],line[3]),(0,255,0),1,cv2.LINE_AA)
    l1p1 = [1,1,1,1]
    l1p2 = [1,1,1,1]
    l1p1[0],l1p1[1],l1p2[0],l1p2[1] = lines[0][0]
    l2p1 = [1,1,1,1]
    l2p2 = [1,1,1,1]
    l2p1[0],l2p1[1],l2p2[0],l2p2[1] = lines[round(i/2)][0]

    lst1 = (l1p1, l1p2)
    slst1 = sorted(lst1,key = lambda x:x[1])
    lst2 = (l2p1, l2p2)
    slst2 = sorted(lst2,key = lambda x:x[1])

    cv2.arrowedLine(img,(int((slst1[1][0]+slst2[1][0])/2),int((slst1[1][1]+slst2[1][1])/2)),(int((slst1[0][0]+slst2[0][0])/2),int((slst1[0][1]+slst2[0][1])/2)),(0,0,0),5,cv2.LINE_AA)
    LinesImage = cv2.resize(img,dimension,interpolation = cv2.INTER_AREA)
    cv2.imwrite("Lines of {0}".format(name),LinesImage)
    cv2.imshow("output",LinesImage)
    cv2.waitKey(0)