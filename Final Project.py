import cv2
import numpy

frame = cv2.VideoCapture("3686.mp4")
framecount = int(frame.get(cv2.CAP_PROP_FRAME_COUNT))
fps = frame.get(cv2.CAP_PROP_FPS)
for z in range(framecount):
    ret, img = frame.read()
    dimension = int(img.shape[1]/4),int(img.shape[0]/4)
    img = cv2.resize(img,dimension,interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,0,25,None,3)
    blur = cv2.blur(edges,(5,5))
    thresh1 = cv2.threshold(blur,10,255,cv2.THRESH_BINARY)[1]
    y, x = thresh1.shape[0:2]
    ything = round(y/5)
    thresh = thresh1[4*ything:y,100:280]
    lines = cv2.HoughLinesP(thresh,rho=1,theta=numpy.pi/180,threshold=10,minLineLength=10,maxLineGap=1700)
    lst1 = (lines[0][0][0:2],lines[0][0][2:4])
    slst1 = sorted(lst1,key=lambda x:x[1])
    lst2 = (lines[round((len(lines)-1)/2)][0][0:2],lines[round((len(lines)-1)/2)][0][2:4])
    slst2 = sorted(lst2,key=lambda x:x[1])
    LinesImage = cv2.resize(img,dimension,interpolation=cv2.INTER_AREA)
    if 180<= int((int((slst1[1][0]+slst2[1][0])/2+100)+int((slst1[0][0]+slst2[0][0])/2+120))/2)<= 230:
        cv2.circle(LinesImage,(x-50,50),25,(0,255,0),-1)
    else:
        cv2.circle(LinesImage,(x-50,50),25,(0,255,255),-1)
    cv2.putText(LinesImage,"Frame: "+str(z+1),(10,70),cv2.FONT_HERSHEY_SIMPLEX,fontScale=2,color=(255,0,255),thickness=8)
    output = numpy.concatenate((img,LinesImage),1)
    cv2.imshow("output",output)
    cv2.waitKey(round(((1/(fps))*1000)))
cv2.waitKey(0)
