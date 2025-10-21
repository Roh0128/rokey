
myGraph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['A', 'H'],
    'E': ['B', 'I'],
    'F': ['C', 'J'],
    'G': ['C'],
    'H': ['D'],
    'I': ['E'],
    'J': ['F']
}

# stack=list()  # 스택( 빈 리스트 생성)

# visited= list()  # 방문 확인용 리스트 생성

# stack.append(start_node)

def my_dfs(graph,start_node):
    stack=list()
    visited=list()
    stack.append(start_node) #시작 노드 스택에 푸시
    
    
    while stack:
        node= stack.pop()  #스택에서 노드 꺼냄
        if node not in visited:  #방문하지 않았다면 방문 처리
            visited.append(node)
            stack.extend(reversed(graph[node]))
    print(f"dfs-{visited}")
    return visited

my_dfs(myGraph,'A')

