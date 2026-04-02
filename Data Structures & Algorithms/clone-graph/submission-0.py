"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}
        return self.dfs(node, visited)

    def dfs(self, old_node, visited):
        if old_node is None:
            return None
        if old_node.val in visited:
            return visited[old_node.val]

        node = Node(old_node.val)
        visited[node.val] = node

        for neighbour in old_node.neighbors:
            node.neighbors.append(self.dfs(neighbour, visited))
        
        return node
