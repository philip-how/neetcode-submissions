class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        x_way_cap = (len(matrix[0]) + 1) // 2
        y_way_cap = len(matrix) // 2

        for j in range(x_way_cap):
            for i in range(y_way_cap):
                prev = matrix[j][len(matrix[0]) - 1 - i]
                matrix[j][len(matrix[0]) - 1 - i] = matrix[i][j]
                next_prev = matrix[len(matrix[0]) - 1 - i][len(matrix) - 1 - j]
                matrix[len(matrix[0]) - 1 - i][len(matrix) - 1 - j] = prev
                prev = next_prev
                next_prev = matrix[len(matrix) - 1 - j][i]
                matrix[len(matrix) - 1 - j][i] = prev
                prev = next_prev
                matrix[i][j] = prev

