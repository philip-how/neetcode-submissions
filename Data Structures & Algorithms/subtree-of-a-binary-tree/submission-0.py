# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        elif subRoot is None:
            return True
        if self.sameCheck(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    def sameCheck(self, root, subRoot):
        if root is None and subRoot is None:
            return True
        elif root is None or subRoot is None:
            return False
        return root.val == subRoot.val and self.sameCheck(root.left, subRoot.left) and self.sameCheck(root.right, subRoot.right)