class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        i = 0
        islands = 0
        while i < len(grid):
            j = 0
            while j < len(grid[i]):
                stack = []
                stack.append((i, j))
                if grid[i][j] == "1":
                    islands += 1
                while stack:
                    u, v = stack.pop()
                    if grid[u][v] == "0":
                        continue
                    else:
                        grid[u][v] = "0"
                    stack.append((max(u-1,0),v))
                    stack.append((min(u+1, len(grid) - 1),v))
                    stack.append((u,max(v-1,0)))
                    stack.append((u,min(v+1, len(grid[i]) - 1)))
                j += 1
            i += 1
        
        return islands

