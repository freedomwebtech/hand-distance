import cv2
from cvzone.HandTrackingModule import HandDetector
detector=HandDetector(detectionCon=0.5,maxHands=2)

cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    hands,frame=detector.findHands(frame)
    if hands:
        hands1=hands[0]
        bbox=hands1["bbox"]
        x,y,w,h=bbox
        fingers1=detector.fingersUp(hands1)
#        print(fingers1)
        print(bbox)
    if len(hands)==2:
        hands2=hands[1]
        fingers2=detector.fingersUp(hands2)
#        print(fingers1,fingers2)
        
        
           
   
        
    frame=cv2.imshow("FRAME",frame)
   
    if cv2.waitKey(1)&0xFF==27:
        break
cap.relase()
cv2.destroyAllWindows()
