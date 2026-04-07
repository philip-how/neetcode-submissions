class Solution:
    def dfs_spread_ocean(self, heights, x, y, ocean):
        if ocean[y][x]:
            return 
        
        ocean[y][x] = True

        if x > 0:
            if heights[y][x] <= heights[y][x-1]:
                self.dfs_spread_ocean(heights, x-1, y, ocean)
        if y > 0:
            if heights[y][x] <= heights[y-1][x]:
                self.dfs_spread_ocean(heights, x, y-1, ocean)
        if x < len(heights[y]) - 1:
            if heights[y][x] <= heights[y][x+1]:
                self.dfs_spread_ocean(heights, x+1, y, ocean)
        if y < len(heights) - 1:
            if heights[y][x] <= heights[y+1][x]:
                self.dfs_spread_ocean(heights, x, y+1, ocean)
        


    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # store a 2D list for whether it is in each ocean
        # and a 2D list for whether it can flow to each ocean

        # run a bfs (or dfs) with each edge as starting_point

        pacific_ocean = []
        atlantic_ocean = []
        for y in range(len(heights)):
            pacific_ocean.append([])
            atlantic_ocean.append([])
            for x in range(len(heights[y])):
                pacific_ocean[-1].append(False)
                atlantic_ocean[-1].append(False)

        for y in range(len(heights)):
            self.dfs_spread_ocean(heights, 0, y, pacific_ocean)
            self.dfs_spread_ocean(heights, len(heights[y]) - 1, y, atlantic_ocean)
        
        for x in range(len(heights[0])):
            self.dfs_spread_ocean(heights, x, 0, pacific_ocean)
            self.dfs_spread_ocean(heights, x, len(heights) - 1, atlantic_ocean)

        output = []
        for y in range(len(heights)):
            for x in range(len(heights[0])):
                if pacific_ocean[y][x] and atlantic_ocean[y][x]:
                    output.append([y, x])

        return output
        
        