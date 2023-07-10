# Used DFS
# Time took: ~ 20 Minutes
# Time complexity: O(n)
# Space complexity: O(n)


from collections import defaultdict

data = [('A', 'B', "blue"), ('A', 'C', "red"), ('B', 'D', "blue"), ('B', 'E', "blue"), ('C', 'B', "red"), ('D', 'C', "blue"), ('A', 'D', "red"), ('D', 'E', "red"), ('E', 'C', "red")]

paths = defaultdict(list)

for f, s, c in data:
    paths[f].append((s,c))

def alternating_path(start, destination, graph):
    visited = set()
    stack = [start]
    paths = 0
    color = None

    met = False

    while stack:
        curr = stack.pop()
        if curr == destination:
            met = True
            
        for i in graph[curr]:
            if (i not in visited) and (i[1] != color):
                paths += 1
                color = i[1]
                stack.append(i[0])
                visited.add(i)

    if paths == 0 or met == False:
        return -1
        
    return paths


print(alternating_path("A","E", paths)) # expected = 4
print(alternating_path("E","D", paths)) # expected = -1