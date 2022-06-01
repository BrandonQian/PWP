import cv2
import numpy

frame = cv2.VideoCapture("3686.mp4")
framecount = int(frame.get(cv2.CAP_PROP_FRAME_COUNT))
fps = frame.get(cv2.CAP_PROP_FPS)
print("FPS: " + str(fps))
print("Frame count: " + str(framecount))
print("Waitkey thing: " + str((1/(fps))*1000))
totalcirclecount = 0
frameswithcircles = 0
tempfram = 0
height = frame.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = frame.get(cv2.CAP_PROP_FRAME_WIDTH)
videodo = cv2.VideoWriter("can videoed.MOV", cv2.VideoWriter_fourcc(*"mp4v"), 10,(int(width),int(height)))  # [][][][][][][][][]][][][][][][][][][][]NOT WORKING
for x in range(framecount):
    ret, img = frame.read()
    img = img[4 * height/5 - height/5 * z:y - ything * z, 0:x]
    dimension = int(img.shape[1] / 4), int(img.shape[0] / 4)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 250, 275, None, 3)
    blur = cv2.blur(edges, (25, 25))
    lines = cv2.HoughLinesP(blur, rho=1, theta=numpy.pi / 180, threshold=2100, minLineLength=2700, maxLineGap=1700)
    if lines is None:
        lines = cv2.HoughLinesP(blur, rho=1, theta=numpy.pi / 180, threshold=1000, minLineLength=900, maxLineGap=1000)
    if lines is not None:
        for i in range(len(lines)):
            line = lines[i][0]
            cv2.line(img, (line[0], line[1]), (line[2], line[3]), (0, 255, 0), 1, cv2.LINE_AA)
    l1p1 = [1, 1, 1, 1]
    l1p2 = [1, 1, 1, 1]
    l1p1[0], l1p1[1], l1p2[0], l1p2[1] = lines[0][0]
    l2p1 = [1, 1, 1, 1]
    l2p2 = [1, 1, 1, 1]
    l2p1[0], l2p1[1], l2p2[0], l2p2[1] = lines[round(i / 2)][0]

    lst1 = (l1p1, l1p2)
    print(lst1)
    slst1 = sorted(lst1, key=lambda x: x[1])
    print(slst1)
    lst2 = (l2p1, l2p2)
    print(lst2)
    slst2 = sorted(lst2, key=lambda x: x[1])
    print(slst2)

    cv2.arrowedLine(img, (int((slst1[1][0] + slst2[1][0]) / 2), int((slst1[1][1] + slst2[1][1]) / 2)),
                    (int((slst1[0][0] + slst2[0][0]) / 2), int((slst1[0][1] + slst2[0][1]) / 2)), (0, 0, 0), 5,
                    cv2.LINE_AA)
    LinesImage = cv2.resize(img, dimension, interpolation=cv2.INTER_AREA)
    cv2.imshow("output", LinesImage)
    cv2.waitKey(round(((1/(fps))*1000)))
    videodo.write(LinesImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
videodo.release()
