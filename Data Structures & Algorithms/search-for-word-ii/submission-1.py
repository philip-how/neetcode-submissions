class Node:
    def __init__(self, leaf=False):
        self.children = {}
        self.leaf = leaf

class Trie:
    def __init__(self):
        self.root = Node()
    
    def add_word(self, word):
        curr_node = self.root

        i = 0
        while i < len(word):
            if word[i] in curr_node.children:
                curr_node = curr_node.children[word[i]]
            else:
                new_node = Node()
                curr_node.children[word[i]] = new_node
                curr_node = new_node
            i += 1
        
        curr_node.leaf = True
    
    def search_start(self, word):
        curr_node = self.root

        i = 0
        while i < len(word):
            if word[i] not in curr_node.children:
                return False
            curr_node = curr_node.children[word[i]]
            i += 1
        
        return True
    
    def search_start_from(self, char, node):
        if char in node.children:
            return node.children[char]
        else:
            return None
        

    def search(self, word):
        curr_node = self.root

        i = 0
        while i < len(word):
            if word[i] not in curr_node.children:
                return False
            curr_node = curr_node.children[word[i]]
            i += 1
        
        return curr_node.leaf
    
    def search_from(self, char, node):
        if char in node.children:
            return node.children[char].leaf
        else:
            return None



class Solution:

    def dfs_searching(self, x, y, trie, board, reachable_dict, rolling_word, curr_stack, running_node):
        if (x, y) in curr_stack:
            return
        curr_stack[(x, y)] = True
        new_rolling_word = rolling_word + board[y][x]
        if trie.search_from(board[y][x], running_node):
            reachable_dict[new_rolling_word] = True
        
        search_from = trie.search_start_from(board[y][x], running_node)
        if search_from is not None:
            if x > 0:
                self.dfs_searching(x-1, y, trie, board, reachable_dict, new_rolling_word, curr_stack, search_from)
            if y > 0:
                self.dfs_searching(x, y-1, trie, board, reachable_dict, new_rolling_word, curr_stack, search_from)
            if x < len(board[y]) - 1:
                self.dfs_searching(x+1, y, trie, board, reachable_dict, new_rolling_word, curr_stack, search_from)
            if y < len(board) - 1:
                self.dfs_searching(x, y+1, trie, board, reachable_dict, new_rolling_word, curr_stack, search_from)
        
        curr_stack.pop((x, y))
                


    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        reachable_dict = {}
        for word in words:
            trie.add_word(word)
            reachable_dict[word] = False

        curr_stack = {}
        
        for y in range(len(board)):
            for x in range(len(board[y])):
                self.dfs_searching(x, y, trie, board, reachable_dict, "", curr_stack, trie.root)

        output = []
        
        for key, value in reachable_dict.items():
            if value:
                output.append(key)
        
        return output

        