import turtle

turtle.title("거북이 그래픽스")
turtle.setup(410,310)
turtle.bgcolor("beige")
# turtle.bgcolor("tomato")
t=turtle

t.shape("turtle")
t.color('black','green')

t.right(180)
t.left(90)
t2=turtle.Turtle()
t2.shape('square')
t2.left(90)
t2.forward(100)
t2.home()
t2.speed(1)

t.write("거북이 글 작성해줘", font=("맑은 고딕", 50,  'normal'))
t.forward(10)

t.right()
turtle.mainloop()

turtle.exitonclick()

