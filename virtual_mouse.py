import cv2
import mediapipe as mp
import numpy as np
import time
import autopy 
import Hand_detection_module as hdm

################
Wcam , Hcam = 640 , 480
frameR = 100
smooth = 8
################

cap = cv2.VideoCapture(0)
cap.set(3 , Wcam)
cap.set(4 , Hcam)
pTime = 0
cTime = 0
plocX , plocY = 0, 0
clocX , clocY = 0 ,0

Wsc , Hsc = autopy.screen.size()

print(Wsc , Hsc)

detector = hdm.HandDetection(0.5)

while True:
    rec , frame = cap.read()

    frame = detector.findHand(frame )
    lmList = detector.findPosition(frame , draw=True)
    fingerList = detector.handUp(frame)
    # print(fingerList)

    if len(lmList) != 0:
        # index Finger
        x1, y1 = lmList[8][1] , lmList[8][2]

        # Middle Finger
        x2 , y2 = lmList[12][1] , lmList[12][2]

        # print(x1 , x2 , y1 , y2)
        cv2.rectangle(frame , (frameR , frameR) , (Wcam - frameR , Hcam - frameR) , (0 , 255 , 0) , 4 )

        if fingerList[1] == 1 and fingerList[2] == 0:

            # find new cooridnates
            x3 = np.interp(x1 , (frameR , Wcam - frameR) , (0 , Wsc))
            y3 = np.interp(y1 , (frameR, Hcam - frameR) , (0 , Hsc))

            #Smooth 

            clocX = plocX + (x3 - plocX) / smooth
            clocY = plocY + (y3 - plocY) / smooth


            #move
            autopy.mouse.move(Wsc- clocX , clocY)
            cv2.circle(frame , (x1 , y1) , 15 , (255 , 9, 255) , -1)
            plocX , plocY = clocX , clocY

            #click 

        elif fingerList[1] == 1 and fingerList[2] == 1:

            if lmList[8] and lmList[12]:
                dis, frame , cx , cy = detector.findDistance(frame, 8, 12)
                print(dis)
                if dis < 45:
                    cv2.circle(frame , (cx , cy) , 15 , (0, 255, 0) , -1)
                    autopy.mouse.click()
            # print("heyy")



            # print("open")
             





    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    cv2.putText(frame , f'Frame : {str(int(fps))}' , (20 , 40) , cv2.FONT_HERSHEY_COMPLEX , 1 , (0 , 255 , 0) , 2 )

    cv2.imshow("Webcam" , frame)
    if cv2.waitKey(1) & 0xFF == ord("x"):
        break

cap.release()
cv2.destroyAllWindows()