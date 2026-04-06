class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        y = 0
        while y < len(matrix):
            x = 0
            while x < len(matrix[y]):
                if matrix[y][x] == 0:
                    for i in range(len(matrix[y])):
                        if matrix[y][i] != 0:
                            matrix[y][i] = None
                    break
                x += 1
            y += 1
        
        x = 0
        while x < len(matrix[0]):
            y = 0
            while y < len(matrix):
                if matrix[y][x] == 0:
                    for i in range(len(matrix)):
                        if matrix[i][x] != 0:
                            matrix[i][x] = None
                    break
                y += 1
            x += 1
        
        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                if matrix[y][x] is None:
                    matrix[y][x] = 0
