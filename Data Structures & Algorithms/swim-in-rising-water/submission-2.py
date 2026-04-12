import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited = []
        for y in range(len(grid)):
            visited.append([])
            for x in range(len(grid[y])):
                visited[-1].append(False)
        
        # dijk

        fringe = [(grid[0][0], 0, 0)]
        heapq.heapify(fringe)
        while fringe:
            depth, x, y = heapq.heappop(fringe)

            if x == len(grid[y]) - 1 and y == len(grid) - 1:
                return depth
            
            visited[y][x] = True
            
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if nx < 0 or ny < 0 or nx >= len(grid[y]) or ny >= len(grid):
                    continue
                if visited[ny][nx]:
                    continue
                visited[ny][nx] = True
                heapq.heappush(fringe, (max(grid[ny][nx], depth), nx, ny))
            

            
            