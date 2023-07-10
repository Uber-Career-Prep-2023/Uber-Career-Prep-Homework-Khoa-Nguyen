# Took about 30 minutes
# Used DFS method
# Time complexity: O(cities + connections)
# Space complexity: O(n)



from collections import defaultdict, deque

cities = ["Skagway", "Juneau", "Gustavus", "Homer", "Port Alsworth", "Glacier Bay", "Fairbanks", "McCarthy", "Copper Center", "Healy", "Anchorage"], [("Anchorage", "Homer"), ("Glacier Bay", "Gustavus"), ("Copper Center", "McCarthy"), ("Anchorage", "Copper Center"), ("Copper Center", "Fairbanks"), ("Healy", "Fairbanks"), ("Healy", "Anchorage")]
cities2 = ["Kona", "Hilo", "Volcano", "Lahaina", "Hana", "Haiku", "Kahului", "Princeville", "Lihue", "Waimea"], [("Kona", "Volcano"), ("Volcano", "Hilo"), ("Lahaina", "Hana"), ("Kahului", "Haiku"), ("Hana", "Haiku"), ("Kahului", "Lahaina"), ("Princeville", "Lihue"), ("Lihue", "Waimea")]




def RoadNetworks(cities, connections):
    visited = set()
    networks = 0

    for i in cities:
        if i not in visited and (len(connections[i]) != 0):
            networks += 1
            stack = [i]

            while stack: #DFS
                curr = stack.pop()
                visited.add(curr)
                
                for n in connections[curr]:
                    if n not in visited:
                        visited.add(n)
                        stack.append(n)
    
    return networks




connections = defaultdict(list)

for one, two in cities[1]:
    if two not in connections[one]:
        connections[one].append(two)
    
    if one not in connections[two]:
        connections[two].append(one)

print(connections)


print(RoadNetworks(cities[0],connections)) # Expected: 2

connections = defaultdict(list)


for one, two in cities2[1]:
    if two not in connections[one]:
        connections[one].append(two)
    
    if one not in connections[two]:
        connections[two].append(one)

# print(connections)
print(RoadNetworks(cities2[0],connections)) # Expected: 3

connections = defaultdict(list)

cities3 = ["testing1", "testing2", "testing3"]

print(RoadNetworks(cities3, connections)) # Expected: 0










