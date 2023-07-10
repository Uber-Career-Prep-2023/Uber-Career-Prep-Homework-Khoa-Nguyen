# Used bfs to traverse this graph
# Time spent: ~ 40 mins
# Time complexity: O(r*c)
# Space Complexity: O(n)

def numIsland(grid: list[list[str]]) -> int:

    def bfs(start, visited, directions):
        queue = [start]
        visited.add(start)

        while queue:
            curr = queue.pop(0)

            for dr, dc in directions:
                nr = dr + curr[0]
                nc = dc + curr[1]
                if nr in range(rows) and nc in range(cols):
                    if grid[nr][nc] == 1 and (nr,nc) not in visited:
                        visited.add((nr,nc))
                        queue.append((nr,nc))
                    # print(f"{nr,nc}", island[nr][nc])

    if not grid:
        return 0

    num_islands = 0
    visited = set()

    rows = len(grid)
    cols = len(grid[0])

    directions = [[-1,0],[1,0],[0,-1],[0,1]] 

    for r in range(rows):
        for c in range(cols):
            # print(f"Neighbors of {r,c}:", grid[r][c])
            if (r, c) not in visited and grid[r][c] == 1:
                num_islands += 1
                #BFS here
                bfs((r,c), visited, directions)

    return num_islands

island = [[1,0,1,1,1],
          [1,1,0,1,1],
          [0,1,0,0,0],
          [0,0,0,1,0],
          [0,0,0,0,0]
          ]

island2 = [[1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1]
          ]

island3 = [[1, 0, 0, 0, 0],
           [0, 1, 0, 0, 0],
           [0, 0, 1, 0, 0],
           [0, 0, 0, 1, 0],
           [0, 0, 0, 0, 1]
          ]


print(numIsland(island))
print(numIsland(island2))
print(numIsland(island3))
