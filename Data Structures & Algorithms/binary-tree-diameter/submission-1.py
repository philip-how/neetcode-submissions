# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.depth = 0

class Solution:
    def __init__(self):
        self.best = 0
        self.depthrun = False

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not self.depthrun:
            self.maxDepth(root)

        if root is None:
            return self.best
        
        self.diameterOfBinaryTree(root.left)
        self.diameterOfBinaryTree(root.right)

        if self.getDepth(root.left) + self.getDepth(root.right) > self.best:
            self.best = self.getDepth(root.left) + self.getDepth(root.right)
        
        return self.best
        
    def getDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            return root.depth


    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        root.depth = max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
    
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1