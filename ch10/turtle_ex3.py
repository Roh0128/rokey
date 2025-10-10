import turtle

# 1. 준비
t = turtle.Turtle()
screen = turtle.Screen()

# 2. 꾸미기
screen.bgcolor("lightgreen") # 배경색
t.color("blue")              # 펜 색상
t.pensize(3)                 # 펜 두께
t.shape("turtle")            # 거북이 모양

# 3. 사각형 그리기
t.forward(150) # 150만큼 직진
t.left(90)     # 왼쪽으로 90도 회전
t.forward(150)
t.left(90)
t.forward(150)
t.left(90)
t.forward(150)
t.left(90)

# 4. 창 유지 (화면 클릭 시 종료)
screen.exitonclick()