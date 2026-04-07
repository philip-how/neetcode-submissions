class Solution:
    def dfs_spread_ocean(self, heights, x, y, ocean, reachables):
        if ocean[y][x]:
            return 
        
        ocean[y][x] = True
        reachables[y][x] = True

        if x > 0:
            if heights[y][x] <= heights[y][x-1]:
                self.dfs_spread_ocean(heights, x-1, y, ocean, reachables)
            else:
                self.dfs_spread_reachability(heights, x-1, y, ocean, reachables)
        if y > 0:
            if heights[y][x] <= heights[y-1][x]:
                self.dfs_spread_ocean(heights, x, y-1, ocean, reachables)
            else:
                self.dfs_spread_reachability(heights, x, y-1, ocean, reachables)
        if x < len(heights[y]) - 1:
            if heights[y][x] <= heights[y][x+1]:
                self.dfs_spread_ocean(heights, x+1, y, ocean, reachables)
            else:
                self.dfs_spread_reachability(heights, x+1, y, ocean, reachables)
        if y < len(heights) - 1:
            if heights[y][x] <= heights[y+1][x]:
                self.dfs_spread_ocean(heights, x, y+1, ocean, reachables)
            else:
                self.dfs_spread_reachability(heights, x, y+1, ocean, reachables)


    def dfs_spread_reachability(self, heights, x, y, ocean, reachables):
        return
        if reachables[y][x]:
            return
        


    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # store a 2D list for whether it is in each ocean
        # and a 2D list for whether it can flow to each ocean

        # run a bfs (or dfs) with each edge as starting_point

        pacific_ocean = []
        atlantic_ocean = []
        pacific_reachable = []
        atlantic_reachable = []
        for y in range(len(heights)):
            pacific_ocean.append([])
            atlantic_ocean.append([])
            pacific_reachable.append([])
            atlantic_reachable.append([])
            for x in range(len(heights[y])):
                pacific_ocean[-1].append(False)
                atlantic_ocean[-1].append(False)
                pacific_reachable[-1].append(False)
                atlantic_reachable[-1].append(False)

        for y in range(len(heights)):
            self.dfs_spread_ocean(heights, 0, y, pacific_ocean, pacific_reachable)
            self.dfs_spread_ocean(heights, len(heights[y]) - 1, y, atlantic_ocean, atlantic_reachable)
        
        for x in range(len(heights[0])):
            self.dfs_spread_ocean(heights, x, 0, pacific_ocean, pacific_reachable)
            self.dfs_spread_ocean(heights, x, len(heights) - 1, atlantic_ocean, atlantic_reachable)

        output = []
        for y in range(len(heights)):
            for x in range(len(heights[0])):
                if pacific_ocean[y][x] and atlantic_ocean[y][x]:
                    output.append([y, x])

        return output
        
        