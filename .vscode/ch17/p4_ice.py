

# 1단계: 전체 얼음 틀 준비 및 카운터 설정
N, M = 4, 5  # 얼음 틀의 세로(N)와 가로(M) 크기
graph = [
    [0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]
]
result = 0 # 만들 수 있는 얼음의 개수

# 2단계: DFS 함수 정의 (연결된 모든 빈 공간을 찾아주는 로봇)
def dfs(x, y):                                      
    # (x, y) 좌표가 얼음 틀을 벗어나면 즉시 종료
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False

    # 현재 위치가 아직 방문하지 않은 빈 공간(0)이라면
    if graph[x][y] == 0:
        # 해당 위치를 방문 처리 (물을 채워 1로 만듦)
        graph[x][y] = 1
        
        # 상, 하, 좌, 우 위치도 재귀적으로 모두 방문 처리
        dfs(x - 1, y) # 상
        dfs(x + 1, y) # 하
        dfs(x, y - 1) # 좌
        dfs(x, y + 1) # 우
        
        # 새로운 얼음 덩어리를 성공적으로 채웠음을 알림
        return True
    
    # 현재 위치가 벽(1)이거나 이미 방문했다면 False 반환
    return False

# 3단계: 모든 칸을 확인하며 얼음 덩어리 개수 세기
for i in range(N):
    for j in range(M):
        # 현재 위치에서 DFS를 실행해서 새로운 얼음 덩어리를 만들 수 있다면
        if dfs(i, j) == True:
            result += 1 # 얼음 개수를 1 증가

print(result) # 최종 개수 출력

n=len(graph) #행
m=len(graph[0]) #열

# print(f"n:{n}")
# print(f"m:{m}")


def dfs_stack(x,y):
    start_node = (x,y)
    stack=[start_node]

    while stack:
        x,y=stack.pop()

        # 주어진 범위를 벗어나면 무시
        if x<0 or x >=n or y <0 or y >=m:
            # 범위를 벗어나는 경우
            continue
        # 현재 노드를 아직 방문하지 않았다면
        if graph[x][y] == 0:

            graph[x][y]=1

            stack.append((x - 1, y)) # 상
            stack.append((x, y - 1)) # 좌
            stack.append((x + 1, y)) # 하
            stack.append((x, y + 1)) # 우
            # 방문 처리, 인접 노드를 스택 추가
            print("이동 경로 확인=",stack)
            for i in graph:
                print(i)


    return True



for i in range(n):
    for j in range(m):
        # 한번 얼음 개수로 카운트된 얼음은 다시 카운트되면 안됌


        if graph[i][j]==0:
            if dfs_stack(i,j)== True:
                result+=1
print(result)