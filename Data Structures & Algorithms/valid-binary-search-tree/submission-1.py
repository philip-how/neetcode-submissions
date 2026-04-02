# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.BSTHelper(root, -1001, 1001)
        
    def BSTHelper(self, root, left_cap, right_cap):
        if root is None:
            return True
        if root.val <= left_cap or root.val >= right_cap:
            return False
        
        return self.BSTHelper(root.left, left_cap, min(right_cap, root.val)) and self.BSTHelper(root.right, max(left_cap, root.val), right_cap)