#  벽은 어두운 색

map={[0,0,1,0,1],
     [1,0,1,0,0],
     [0,0,1,1,0],
     [0,1,0,0,0],
     [0,0,0,1,1]
}

def dfs_on_grid(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    stack = [(start, [start])]  # (현재 위치, 현재까지의 경로)
    visited = set()

    while stack:
        (r, c), path = stack.pop()

        if (r, c) == end:
            print("DFS 경로를 찾았습니다!")
            return path

        if (r, c) not in visited:
            visited.add((r, c))

            # 인접 노드 (상, 하, 좌, 우) 탐색
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc

                # 1. 맵 경계 안에 있고
                if 0 <= nr < rows and 0 <= nc < cols:
                    # 2. 벽(1)이 아니며
                    if grid[nr][nc] == 0:
                        # 3. 방문한 적 없는 곳이라면 스택에 추가
                        if (nr, nc) not in visited:
                            stack.append(((nr, nc), path + [(nr, nc)]))
    
    return "경로를 찾을 수 없습니다."

# 출발점 (0,0)에서 도착점 (4,3)까지 경로 탐색
start_node = (0, 0)
end_node = (4, 3) # 도착점은 벽이 아니어야 함

dfs_path = dfs_on_grid(map_data, start_node, end_node)
print(f"DFS 탐색 경로: {dfs_path}")