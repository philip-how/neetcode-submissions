class Solution:
    def works(self, my_proposed_word, x, y, word, used_indexes):
        if my_proposed_word == word:
            return True
        
        if (x, y) in used_indexes:
            return False
        
        if word[len(my_proposed_word)] != self.board[y][x]:
            return False
        
        used_indexes[(x, y)] = True

        new_proposed_word = my_proposed_word + self.board[y][x]

        if new_proposed_word == word:
            return True

        if x > 0:
            if self.works(new_proposed_word, x-1, y, word, used_indexes):
                used_indexes.pop((x, y))
                return True
        if y > 0:
            if self.works(new_proposed_word, x, y-1, word, used_indexes):
                used_indexes.pop((x, y))
                return True
        if y < len(self.board) - 1:
            if self.works(new_proposed_word, x, y+1, word, used_indexes):
                used_indexes.pop((x, y))
                return True
        if x < len(self.board[y]) - 1:
            if self.works(new_proposed_word, x+1, y, word, used_indexes):
                used_indexes.pop((x, y))
                return True

        used_indexes.pop((x, y))

        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board

        for y in range(len(board)):
            for x in range(len(board[y])):
                if self.works("", x, y, word, {}):
                    return True
        
        return False
        