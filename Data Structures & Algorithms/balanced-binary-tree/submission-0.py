# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        leftReturn = self.isBalancedHelper(root.left)
        rightReturn = self.isBalancedHelper(root.right)
        
        if leftReturn == -1:
            return False
        
        if rightReturn == -1:
            return False
        
        if leftReturn - rightReturn <= 1 and leftReturn - rightReturn >= -1:
            return True
        else:
            return False
        

    def isBalancedHelper(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return 1
        
        leftReturn = self.isBalancedHelper(root.left)
        rightReturn = self.isBalancedHelper(root.right)

        if leftReturn == -1:
            return -1
        
        if rightReturn == -1:
            return -1

        if leftReturn - rightReturn <= 1 and leftReturn - rightReturn >= -1:
            return max(leftReturn, rightReturn) + 1
        else:
            print(root.val)
            return -1
