# 얼음 틀과 크기
N, M = 4, 5
graph = [[0,0,1,1,0], [0,0,0,1,1], [1,1,1,1,1], [0,0,0,0,0]]

def dfs_stack_list(x, y):
    if graph[x][y] == 1: # 시작점이 벽이면 False
        return False
        
    stack = [(x, y)] # 1. 방문할 곳을 저장할 스택 (시작점 추가)

    while stack: # 2. 스택이 빌 때까지 반복
        curr_x, curr_y = stack.pop() # 3. 가장 나중에 추가된 곳을 꺼냄

        if graph[curr_x][curr_y] == 0:
            graph[curr_x][curr_y] = 1 # 방문 처리
            
            # 4. 상하좌우를 탐색하며 갈 수 있는 곳을 스택에 추가
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                nx, ny = curr_x + dx, curr_y + dy
                if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                    stack.append((nx, ny))
    return True

# 실행 부분
result = 0
for i in range(N):
    for j in range(M):
        if dfs_stack_list(i, j) == True:
            result += 1
print(f"리스트 스택 방식 결과: {result}")




from collections import deque

# 얼음 틀과 크기
N, M = 4, 5
graph = [[0,0,1,1,0], [0,0,0,1,1], [1,1,1,1,1], [0,0,0,0,0]]

def dfs_stack_deque(x, y):
    if graph[x][y] == 1:
        return False
        
    stack = deque([(x, y)]) # 1. deque를 스택으로 사용

    while stack:
        curr_x, curr_y = stack.pop() # 2. 동작 방식은 list와 동일

        if graph[curr_x][curr_y] == 0:
            graph[curr_x][curr_y] = 1
            
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                nx, ny = curr_x + dx, curr_y + dy
                if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                    stack.append((nx, ny))
    return True

# 실행 부분
result = 0
for i in range(N):
    for j in range(M):
        if dfs_stack_deque(i, j) == True:
            result += 1
print(f"Deque 스택 방식 결과: {result}")










# 얼음 틀과 크기 (모든 예제에서 공통으로 사용)
N, M = 4, 5
graph = [[0,0,1,1,0], [0,0,0,1,1], [1,1,1,1,1], [0,0,0,0,0]]

def dfs_recursive(x, y):
    # 1. 범위를 벗어나면 즉시 종료
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    
    # 2. 현재 위치가 빈 공간(0)이면
    if graph[x][y] == 0:
        graph[x][y] = 1 # 방문 처리
        # 3. 상하좌우에 대해 자기 자신을 다시 호출
        dfs_recursive(x - 1, y) # 상
        dfs_recursive(x + 1, y) # 하
        dfs_recursive(x, y - 1) # 좌
        dfs_recursive(x, y + 1) # 우
        return True # 새로운 덩어리를 찾았음을 알림
    return False

# 실행 부분
result = 0
for i in range(N):
    for j in range(M):
        if dfs_recursive(i, j) == True:
            result += 1
print(f"재귀 방식 결과: {result}")