
def my_bfs(graph,start_node):
    queue=list()
    visited=list()

    queue.append(start_node)
    while queue:
        node= queue.pop(0)

        if node not in visited:
            queue.extend(graph[node])
            visited.append(node)
    print(f"bfs- {visited}")
    return visited

import graph1

my_bfs(graph1, "A")
