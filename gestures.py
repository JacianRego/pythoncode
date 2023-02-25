import cv2
import mediapipe as mp
webcam = cv2.VideoCapture(0)
handsmp = mp.solutions.hands
connect = mp.solutions.drawing_utils
handsdetect = handsmp.Hands(min_detection_confidence = 0.8, min_tracking_confidence = 0.5)
def DrawLandmark(image, handlandmark):
    if handlandmark:
        for i in handlandmark:
            connect.draw_landmarks(image, i, handsmp.HAND_CONNECTIONS)

def CountFingers(image, handlandmark, handnumber=0):
    if handlandmark:
        fingers = handlandmark[handnumber].landmark
        list1 = []
        
while True:
    boolean, frames = webcam.read()
    frames = cv2.flip(frames, 1)
    result = handsdetect.process(frames)
    handlandmark = result.multi_hand_landmarks
    DrawLandmark(frames, handlandmark)
    CountFingers(frames, handlandmark)
    cv2.imshow("Webcam", frames)
    if cv2.waitKey(1) == 32:
        break
cv2.destroyAllWindows()