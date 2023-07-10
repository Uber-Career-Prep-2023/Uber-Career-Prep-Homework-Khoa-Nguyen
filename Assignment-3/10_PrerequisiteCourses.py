# Took ~ 25 minutes
# implemented topological sort using DFS
# Time complexity O(n+m)
# Space complexity O(n)


from collections import defaultdict

def prereq(courses, order):
    visited = set()
    arr = []

    def dfs(node):
        visited.add(node)

        for neighbor in order[node]:
            if neighbor not in visited:
                dfs(neighbor)
            
        arr.append(node)

    for i in courses:
        if i not in visited:
            dfs(i)

    return arr

courses = ["Intro to Programming", "Data Structures", "Advanced Algorithms", "Operating Systems", "Databases"]
order = defaultdict(list)
temp = { "Data Structures": ["Intro to Programming"], "Advanced Algorithms": ["Data Structures"], "Operating Systems": ["Advanced Algorithms"], "Databases": ["Advanced Algorithms"] }

for i in temp: # this just makes the dictionary work properly
    order[i] = temp[i]

print(prereq(courses,order)) #expected = ['Intro to Programming', 'Data Structures', 'Advanced Algorithms', 'Operating Systems', 'Databases']

courses = ["Intro to Writing", "Contemporary Literature", "Ancient Literature", "Comparative Literature", "Plays & Screenplays"]
order = defaultdict(list)
temp = { "Contemporary Literature": ["Intro to Writing"], "Ancient Literature": ["Intro to Writing"], "Comparative Literature": ["Ancient Literature", "Contemporary Literature"], "Plays & Screenplays": ["Intro to Writing"] }

for i in temp:
    order[i] = temp[i]

print(prereq(courses,order)) #expected = ['Intro to Writing', 'Contemporary Literature', 'Ancient Literature', 'Comparative Literature', 'Plays & Screenplays']
