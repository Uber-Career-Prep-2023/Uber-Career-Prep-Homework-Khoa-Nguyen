from collections import defaultdict

def create_adjacency_set(edges):
    adjacency = defaultdict(list)

    for edge in edges:
        adjacency[edge[0]].append(edge[1])
        if edge[1] not in adjacency:
            adjacency[edge[1]] = []

    return dict(adjacency)

# print(create_adjacency_set([(1, 2), (2, 3), (1, 3), (3, 2), (2, 0)]))

def bfs(start, graph, target) -> bool:
    queue = [start]
    visited = [start]

    while queue:
        curr = queue.pop(0)
        if curr == target:
            return True
        for neighbour in graph[curr]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.append(neighbour)

    return False

def dfs(node, graph, target) -> bool:
    visited = set()

    def dfs_helper(visited, node, graph, target):
        if node == target: return True

        if node not in visited:
            visited.add(node)
            for neighbours in graph[node]:
                if dfs_helper(visited,neighbours,graph,target):
                    return True
                
        return False

    return dfs_helper(visited, node, graph, target) is True

def topological_sort(graph) -> list[int]:
    arr = []
    visited = set()

    def dfs(node):
        if node not in visited:
            visited.add(node)
            for neighbours in graph[node]:
                dfs(neighbours)

            arr.insert(0,node)

    for node in graph:
        if node not in visited:
            dfs(node)

    return arr






# graph = create_adjacency_set([(1, 2), (2, 3), (1, 3), (3, 2), (2, 0)])
# print(bfs(1,graph, 0)) #Expected True
# print(dfs(1,graph, 0)) #Expected True
# print(topological_sort(graph))









