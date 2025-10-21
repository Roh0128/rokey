def calculate_postfix(expression):
    stack = []
    for token in expression.split():
        if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
            stack.append(int(token))
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            if token == '+':
                stack.append(op1 + op2)
            elif token == '-':
                stack.append(op1 - op2)
            elif token == '*':
                stack.append(op1 * op2)
            elif token == '/':
                stack.append(int(op1 / op2))
    return stack.pop()

# 예시: "3 4 + 2 *"는 (3+4)*2 와 같으므로 결과는 14
print(f"'3 4 + 2 *'의 계산 결과: {calculate_postfix('3 4 + 2 *')}")







class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, x):
        self.items.append(x)

    def dequeue(self):
        return self.items.pop(0) if self.items else -1

    def front(self):
        return self.items[0] if self.items else -1

    def is_empty(self):
        return not self.items
    



    class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, x):
        if not self.is_full():
            if self.is_empty():
                self.front = 0
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = x

    def dequeue(self):
        if not self.is_empty():
            value = self.queue[self.front]
            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.front = (self.front + 1) % self.size
            return value
        return -1
    


    class Deque:
    def __init__(self):
        self.items = []

    def push_front(self, x):
        self.items.insert(0, x)

    def push_back(self, x):
        self.items.append(x)

    def pop_front(self):
        return self.items.pop(0) if self.items else -1

    def pop_back(self):
        return self.items.pop() if self.items else -1
    

    maze = [
    [1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 1],
    [1, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 1]
]
    

for row in maze:
    for cell in row:
        print(cell, end=" ")
    print()for row in maze:
    for cell in row:
        print(cell, end=" ")
    print()


rows = int(input("세로 크기: "))
cols = int(input("가로 크기: "))
input_map = []
for i in range(rows):
    row_data = list(map(int, input(f"{i+1}번째 행 데이터: ").split()))
    input_map.append(row_data)



def dfs_search(grid, start):
    rows, cols = len(grid), len(grid[0])
    stack = [start]
    visited = set()
    path = []
    while stack:
        x, y = stack.pop()
        if (x, y) in visited or grid[x][y] == 1:
            continue
        visited.add((x, y))
        path.append((x, y))
        # 상하좌우 노드를 스택에 추가
        if x > 0: stack.append((x - 1, y))
        if x < rows - 1: stack.append((x + 1, y))
        if y > 0: stack.append((x, y - 1))
        if y < cols - 1: stack.append((x, y + 1))
    return path





from collections import deque

def bfs_search(grid, start):
    rows, cols = len(grid), len(grid[0])
    queue = deque([start])
    visited = {start}
    path = []
    while queue:
        x, y = queue.popleft()
        if grid[x][y] == 1: continue
        path.append((x, y))
        # 상하좌우 이웃 노드 확인
        for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny))
    return path





import turtle

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Turtle Screen")
screen.exitonclick() # 클릭 시 종료


import turtle

def drawStar(size, color):
    t = turtle.Turtle()
    t.color(color)
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()
    t.hideturtle()

# 함수 호출 예시
# drawStar(100, "yellow")
# turtle.done()




import turtle

def drawStar(x, y, size, color):
    t = turtle.Turtle()
    t.speed(5)
    t.pensize(1)
    t.hideturtle()

    t.penup()
    t.goto(x, y)
    t.pendown()

    t.color(color)
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()


import turtle

def drawMoon(x, y, size, color):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(size)
    t.end_fill()

# 함수 호출 예시
# screen = turtle.Screen()
# screen.bgcolor("black")
# drawMoon(200, 150, 50, "lightyellow")
# turtle.done()




import turtle
import random

# 화면 설정
screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Night Sky")
turtle.tracer(0) # 그리는 과정 생략, 속도 향상

# 위에서 정의한 drawStar, drawMoon 함수 필요

# 달 그리기
drawMoon(250, 180, 60, "ivory")

# 무작위 별 그리기
for _ in range(50):
    x = random.randint(-390, 390)
    y = random.randint(-290, 290)
    size = random.randint(5, 20)
    color = random.choice(["white", "gold", "lightblue"])
    drawStar(x, y, size, color)

screen.update() # tracer(0) 사용 시 화면 업데이트 필수
screen.exitonclick()