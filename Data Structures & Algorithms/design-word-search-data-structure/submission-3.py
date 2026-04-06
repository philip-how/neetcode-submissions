class Node:

    def __init__(self, leaf=False):
        self.children = {}
        self.leaf = leaf


class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
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
            
        

    def search(self, word: str) -> bool:
        return self.search_helper(word, 0, self.root)
    
    def search_helper(self, word: str, index: int, node) -> bool:
        if index >= len(word):
            return node.leaf

        sol_found = False
        
        if word[index] == ".":
            for val in node.children.values():
                sol_found = sol_found or self.search_helper(word, index+1, val)
        else:
            if word[index] in node.children:
                sol_found = self.search_helper(word, index+1, node.children[word[index]])
        return sol_found
        
