# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lesser = min(p.val, q.val)
        maxer = max(p.val, q.val)

        print(root.val)
        
        if root.val >= lesser and root.val <= maxer:
            return root
        elif root.val <= lesser and root.val <= maxer:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return self.lowestCommonAncestor(root.left, p, q)

        