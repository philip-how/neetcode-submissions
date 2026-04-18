# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traverse(self, root: Optional[TreeNode], ls):
        if root is None:
            return
        self.traverse(root.left, ls)
        ls.append(root.val)
        self.traverse(root.right, ls)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ls = []

        self.traverse(root, ls)

        return ls