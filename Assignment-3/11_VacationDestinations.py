# Took ~ 40min
# Used DFS
# Time complexity: O(cities + connections)
# Space complexity: O(n)

from collections import defaultdict

data = [
    ("Boston", "New York", 4),
    ("New York", "Philadelphia", 2),
    ("Boston", "Newport", 1.5),
    ("Washington, D.C.", "Harper's Ferry", 1),
    ("Boston", "Portland", 2.5),
    ("Philadelphia", "Washington, D.C.", 2.5)
]

paths = defaultdict(list)

for f, s, c in data:
    paths[f].append((s, c))
    
    if (f, c) not in paths[s]:
        paths[s].append((f, c))


def vaca_destination(paths, start, k):
    
    visited = set()
    visited.add(start)

    stack = [(start, k)]
    num_places = 0


    while stack:
        curr = stack.pop()

        for place, dis in paths[curr[0]]:
            if place not in visited and (curr[1] - dis) >= 0 :
                stack.append((place, curr[1] - dis - 1))
                visited.add(place)
                num_places += 1

    visited.remove(start)
    print(visited)
    return num_places


# Test Case 1
origin = "New York"
k = 5
print(vaca_destination(paths, origin, k))  # Output: 2 (["Boston", "Philadelphia"])

# Test Case 2
origin = "New York"
k = 7
print(vaca_destination(paths, origin, k))  # Output: 4 (["Boston", "Philadelphia", "Washington, D.C", "Newport"])

# Test Case 3
origin = "New York"
k = 8
print(vaca_destination(paths, origin, k))  # Output: 6 (["Boston", "Philadelphia", "Washington, D.C", "Newport", "Harper's Ferry", "Portland"])
