import sys

class Solution:
    def find_longest(self, matrix, tracking_best, x, y):
        if tracking_best[y][x] != -1:
            return tracking_best[y][x]
        
        best_path = 1

        if x > 0 and matrix[y][x-1] > matrix[y][x]:
            best_path = max(best_path, self.find_longest(matrix, tracking_best, x-1, y) + 1)
        if x < len(matrix[y]) - 1 and matrix[y][x+1] > matrix[y][x]:
            best_path = max(best_path, self.find_longest(matrix, tracking_best, x+1, y) + 1)
        if y > 0 and matrix[y-1][x] > matrix[y][x]:
            best_path = max(best_path, self.find_longest(matrix, tracking_best, x, y-1) + 1)
        if y < len(matrix) - 1 and matrix[y+1][x] > matrix[y][x]:
            best_path = max(best_path, self.find_longest(matrix, tracking_best, x, y+1) + 1)

        tracking_best[y][x] = best_path

        return best_path


    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        sys.setrecursionlimit(100000)
        tracking_best = []

        for y in range(len(matrix)):
            tracking_best.append([])
            for x in range(len(matrix[0])):
                tracking_best[-1].append(-1)
        
        best_path = 0
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                best_path = max(self.find_longest(matrix, tracking_best, x, y), best_path)
        
        return best_path

