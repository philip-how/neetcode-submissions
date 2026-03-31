class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = []
        for i in range(n):
            paths.append([0] * m)
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    paths[i][j] = 1
                elif i == 0:
                    paths[i][j] = paths[i][j-1]
                elif j == 0:
                    paths[i][j] = paths[i-1][j]
                else:
                    paths[i][j] = paths[i-1][j] + paths[i][j-1]

        for path in paths:
            print(path)

        return paths[n-1][m-1]