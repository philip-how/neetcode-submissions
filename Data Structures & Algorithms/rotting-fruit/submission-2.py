class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fringe = []
        DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == 2:
                    fringe.append((x, y))
            
        output = 0
        while fringe:
            new_fringe = []
            while fringe:
                x, y = fringe.pop()
                for dx, dy in DIRECTIONS:
                    nx, ny = dx + x, dy + y

                    if nx >= 0 and nx < len(grid[0]) and ny >= 0 and ny < len(grid):
                        if grid[ny][nx] == 1:
                            new_fringe.append((ny, nx))
                            grid[ny][nx] = 2
            fringe = new_fringe
            if fringe:
                output += 1
        
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == 1:
                    return -1
        
        return output