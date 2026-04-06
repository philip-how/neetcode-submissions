class Node:
    def __init__(self, val, exists=False):
        self.val = val
        self.children = {}
        self.exists = exists

class PrefixTree:

    def __init__(self):
        self.root = Node("")

    def insert(self, word: str) -> None:
        curr_node = self.root

        i = 0
        while i < len(word):
            sofar = word[i]
            if sofar in curr_node.children:
                curr_node = curr_node.children[sofar]
            else:
                new_node = Node(sofar)
                curr_node.children[sofar] = new_node
                curr_node = new_node
            i += 1

        curr_node.exists = True

    def search(self, word: str) -> bool:
        curr_node = self.root
        i = 0
        while i < len(word):
            sofar = word[i]
            if sofar in curr_node.children:
                curr_node = curr_node.children[sofar]
            else:
                return False
            i += 1
        
        if curr_node.exists:
            return True
        else:
            return False

        

    def startsWith(self, prefix: str) -> bool:
        curr_node = self.root
        i = 0
        while i < len(prefix):
            sofar = prefix[i]
            if sofar in curr_node.children:
                curr_node = curr_node.children[sofar]
            else:
                return False
            i += 1
        
        return True
        
        
