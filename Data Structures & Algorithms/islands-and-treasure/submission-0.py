class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = []
        current = []
        for y in range(len(grid)):
            visited.append([])
            for x in range(len(grid[0])):
                if grid[y][x] == 0:
                    visited[-1].append(True)
                    current.append((x,y))
                else:
                    visited[-1].append(False)
        
        i = 0
        while current:
            new = []
            for x, y in current:
                if grid[y][x] == -1:
                    continue
                grid[y][x] = i
                if x > 0 and not visited[y][x-1]:
                    new.append((x-1, y))
                    visited[y][x-1] = True
                if y > 0 and not visited[y-1][x]:
                    new.append((x, y-1))
                    visited[y-1][x] = True
                if y < len(grid) - 1 and not visited[y+1][x]:
                    new.append((x, y+1))
                    visited[y+1][x] = True
                if x < len(grid[0]) - 1 and not visited[y][x+1]:
                    new.append((x+1, y))
                    visited[y][x+1] = True
            current = new
            i += 1
        
        return 


        # bfs, with all treasure points as starters