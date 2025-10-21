import cv2
image=cv2.imread(r"C:\Users\jhroh\Downloads\rocket-launch-67723_1280.jpg")
gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

edges=cv2.Canny(gray,
                threshold1=100,
                threshold2=300)

cv2.imshow('Canny Edge Detection', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()