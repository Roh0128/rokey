import cv2

image=cv2.imread(r"C:\Users\jhroh\Downloads\rocket-launch-67723_1280.jpg")
resized=cv2.resize(image, (300,300))
# 픽셀값들의 배열
# print(type(resized))

gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
rgb=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
hsv=cv2.cvtColor(image, cv2.COLOR_BGR2HSV)



cv2.imshow('loaded image',rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()   #모든 opencv항 닫기


# 그레이 방식: 1채널만 사용, 채널수 3개->1개로 줄어듬, 이미지 연산의 양 줄임

# HSV 방식: 3개의 채널을 갖는 이미지 표현법
# HUE 색조, Saturation 채도, Value 명도


