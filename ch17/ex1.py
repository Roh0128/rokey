
graph1={
    1:[2,3,4],
    2:[1,5],
    3:[1,6],
    4:[1,6],
    5:[2,6],
    6:[3,5]
}
def my_dfs(graph,start_node):
    stack=list()
    visited=list()

    stack.append(start_node)

    while graph:
        node=stack.pop()

        if node not in visited:
            stack.extend(reversed(graph[node]))
            visited.append(node)
    return visited

print(my_dfs(graph1,1))

def my_bfs(graph,start_node):
    queue=list()
    visited=list()

    queue.append(start_node)

    while graph:
        node=queue.pop(0)

        if node not in visited:
            queue.extend(graph[node])
            visited.append(node)
    return visited
