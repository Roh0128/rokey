import cv2

cap= cv2.VideoCapture(r"C:\Users\jhroh\OneDrive\rokey\ch21\opencv\244754_small.mp4")

while True:
    ret, frame=cap.read()
    
    if not ret:
        break

    edges=cv2.Canny(frame,100,200)


    cv2.imshow('Video Capture', edges)

    if cv2.waitKey(1) == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
