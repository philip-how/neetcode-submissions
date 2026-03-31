class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        i = 0
        while i < len(board):
            j = 0
            while j < len(board[i]):
                if board[i][j] in board[i][:j] and board[i][j] != ".":
                    print(board[i][j], board[i][:j], "HI")
                    return False
                j += 1
            i += 1

        i = 0
        while i < len(board[0]):
            j = 0
            digits = []
            while j < len(board):
                if board[j][i] in digits and board[j][i] != ".":
                    print(digits, "HII")
                    return False
                
                digits.append(board[j][i])
                j += 1
            i += 1

        i = 0
        while i < 3:
            j = 0
            while j < 3:
                digits = board[3*j][3*i:3*i + 3] + board[3*j+1][3*i:3*i + 3] + board[3*j+2][3*i:3*i + 3]

                k = 0
                while k < len(digits):
                    if digits[k] in digits[:k] and digits[k] != ".":
                        print(digits, "HIII")
                        return False
                    k += 1

                j += 1
            i += 1

        return True




