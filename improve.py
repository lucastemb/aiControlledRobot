from cvzone.HandTrackingModule import HandDetector #imports the hand detector from cvzone
import cvzone
import cv2 
import serial
import time

cap = cv2.VideoCapture(0) #captures video from the webcam 
detector = HandDetector(maxHands = 1, detectionCon = 0.8) #the detector variable will hold a hand detector object
#arduino = serial.Serial(port="/dev/tty.usbmodem1101", baudrate = 9600)



while True: 
    success, img = cap.read() #first element is a boolean, if true it runs
    hands, img = detector.findHands(img) #hands is an array all info for each hand on screen will be stored there 
    
    if hands:
        #lmList1 = hands[0]["lmList"] #maps out all joints on given hand (i think lm is short for ligament? so maybe it's ligament list)
        #bbox1 = hands[0]["bbox"] #creates the bounding box for the hand on screen
        #centerPoint1 = hands[0]["center"] #identifies the center point for the given hand on screen
        #handType1 = hands[0]["type"] #classifies the hand as being right or left
        
        fingers = detector.fingersUp(hands[0])
        serialstr = "$"
        for num in fingers: 
            serialstr+=str(num)
        cv2.putText(img, str(fingers), (50,50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255),2, cv2.LINE_AA)
        time.sleep(0.5)
        #arduino.write(bytes(serialstr,'utf-8'))
        


    cv2.imshow("Hand (Demo)", img) #creates a window called hand(demo) using the live feed from img
    if cv2.waitKey(1) & 0xFF == ord('q'): #waitKey cycles through frames after waiting for at least 1ms. 
        #cv2.waitKey(1) returns the value of the key pressed and & 0xFF applies a bit mask that allows for a proper comparison
                        #ord returns the UNICODE (numerical) value of a given character, in this case, q
        break

cap.release() #stops webcam
cv2.destroyAllWindows() #self-explanatory destroys all windows created

