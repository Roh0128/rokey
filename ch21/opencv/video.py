import cv2

cap= cv2.VideoCapture(r"C:\Users\jhroh\OneDrive\rokey\ch21\opencv\244754_small.mp4")

while True:
    frame=cap.read()
    

    cv2.imshow('Video Capture', frame)

    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
s