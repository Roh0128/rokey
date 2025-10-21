import cv2

image=cv2.imread(r"C:\Users\jhroh\Downloads\rocket-launch-67723_1280.jpg")

blurred=cv2.GaussianBlur(image, (101,101), 0)
# 홀수로만 처리
cv2.imshow("gaussian Blur", blurred)
cv2.waitKey(0)    #무한대기
cv2.destroyAllWindows()

