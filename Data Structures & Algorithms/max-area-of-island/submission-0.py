class Solution:
    def dfs(self, visited, grid, x, y):
        print(x, y)
        if visited[y][x]:
            return 0
        if grid[y][x] == 0:
            return 0
        
        visited[y][x] = True

        result = 1
        if x > 0:
            result += self.dfs(visited, grid, x-1, y)
        if y > 0:
            result += self.dfs(visited, grid, x, y-1)
        if x < len(grid[0]) - 1:
            result += self.dfs(visited, grid, x+1, y)
        if y < len(grid) - 1:
            result += self.dfs(visited, grid, x, y+1)
        
        return result


    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = []
        for y in range(len(grid)):
            visited.append([])
            for x in range(len(grid[0])):
                visited[-1].append(False)
        
        best_size = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                best_size = max(best_size, self.dfs(visited, grid, x, y))
        
        return best_size