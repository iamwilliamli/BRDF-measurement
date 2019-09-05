import cv2

i = 0
while (1):
    cap = cv2.VideoCapture(1)
    ret, frame = cap.read()
    cv2.imshow("capture", ret)
    k = cv2.waitKey(1)
    if k == 27:
        break
    elif k == ord('s'):
        cap = cv2.VideoCapture(1)
        ret, frame = cap.read()
        cv2.imwrite('/Users/William/brdfm/restor/tet ' + str(1) + '.jpg', ret)
