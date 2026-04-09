class Solution:
    def not_surrounded(self, board, visited, x, y, loop_no, loops):
        if visited[y][x] or board[y][x] == "X":
            return False

        if board[y][x] != "O":
            return loops[board[y][x]]
        visited[y][x] = True

        board[y][x] = loop_no

        truthy = False

        if x == 0 or x == len(board[y]) - 1 or y == 0 or y == len(board) - 1:
            truthy = True

        if x < len(board[0]) - 1:
            truthy = self.not_surrounded(board, visited, x+1, y, loop_no, loops) or truthy
        if x > 0:
            truthy = self.not_surrounded(board, visited, x-1, y, loop_no, loops) or truthy
        if y > 0:
            truthy = self.not_surrounded(board, visited, x, y-1, loop_no, loops) or truthy
        if y < len(board) - 1:
            truthy = self.not_surrounded(board, visited, x, y+1, loop_no, loops) or truthy
        
        return truthy

    def solve(self, board: List[List[str]]) -> None:
        visited = []
        for y in range(len(board)):
            visited.append([])
            for x in range(len(board[0])):
                visited[-1].append(False)

        loops = []

        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == "O" and not visited[y][x]:
                    loops.append(self.not_surrounded(board, visited, x, y, len(loops), loops))

        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] != "X":
                    if loops[board[y][x]]:
                        board[y][x] = "O"
                    else:
                        board[y][x] = "X"
        