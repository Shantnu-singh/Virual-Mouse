import cv2
import time
import mediapipe as mp
import numpy as np

# mode = False , maxHands = 2 , detectionCon = 0.5 , TrackCon = 0.5
class HandDetection:
    def __init__(self , min_detection_confidence = 0.5):
        # self.mode = mode
        # self.maxHand = maxHands
        self.min_detection_confidence = min_detection_confidence
        # self.TrackCon = TrackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands( self.min_detection_confidence )
        self.mpDraw = mp.solutions.drawing_utils


    def findHand(self , frame , flag = True):
        RGB_frame = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(RGB_frame)

        # print(self.results.multi_hand_landmarks)

        if self.results.multi_hand_landmarks:
            for multihands in self.results.multi_hand_landmarks:
                if flag:
                    self.mpDraw.draw_landmarks(frame , multihands , self.mpHands.HAND_CONNECTIONS)

        return frame
    
    
    def findPosition(self , frame , handno = 0 , draw = True):

        lmList = []
        
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handno]

            for id , lm in enumerate(myHand.landmark):
                h , w , c = frame.shape
                cx , cy = int(lm.x*w) , int(lm.y*h)
                # print(id , cx , cy)
                lmList.append([id , cx , cy])

                if draw:
        
                    cv2.circle(frame , (cx , cy) , 7 , (255 , 0 , 9) , cv2.FILLED)

        return lmList
    
    def findDistance(self , frame , point1 , point2 , draw = True):

        lmList = self.findPosition(frame)

        if len(lmList) != 0:
            x1 , y1 = lmList[point1][1] , lmList[point1][2]
            x2 , y2 = lmList[point2][1] , lmList[point2][2]
            cx , cy = (x1 + x2)//2 , (y1+y2)//2

            
            if draw:
                cv2.circle(frame , (x1, y1) ,15 , (0, 0 ,255) , -1 )
                cv2.circle(frame , (x2, y2) ,15 , (0, 0 ,255) , -1 )
                cv2.line(frame , (x1, y1) , (x2 , y2) , (0, 255 , 0), 3)
                dis = np.hypot(x2-x1 , y2-y1)
                cv2.circle(frame , (cx , cy) ,15 , (255, 0 ,255) , -1 )

            return  dis , frame , cx , cy
    
    def handUp(self , frame):
        lmList = self.findPosition(frame)
        fingers = []
        
        if len(lmList) != 0:
                    #Thumb 
                if lmList[4][1] > lmList[2][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)



                for i in range(8 , 21 , 4):
                    if lmList[i][2] < lmList[i-2][2]:
                        fingers.append(1)
                    else:
                        fingers.append(0)

        return fingers
    







            
            

    


    
def main():
    pTime = 0
    cTime = 0


    cap = cv2.VideoCapture(0)
    
    detector = HandDetection()


    while True:

        rec , frame = cap.read()

        frame = detector.findHand(frame)
        lmlist = detector.findPosition(frame)
        
        if len(lmlist) != 0:
            
            print(lmlist[4])
            if lmlist[8] and lmlist[12]:
                dis, frame , a , b = detector.findDistance(frame, 8, 12)
                print("Distance between points 8 and 12:", dis)
        
        cTime  =time.time()
        Fps = 1/(cTime - pTime)
        pTime = cTime
        # dis , frame = detector.findPosition(frame , 8 , 12  )


        cv2.putText(frame , str(int(Fps)) , (10 , 40) , cv2.FONT_HERSHEY_COMPLEX , 1 , (0,255 , 0) , 2 )
        

    
        cv2.imshow("webcam" , frame)
        if cv2.waitKey(1) & 0xFF == ord("x"):
         break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()