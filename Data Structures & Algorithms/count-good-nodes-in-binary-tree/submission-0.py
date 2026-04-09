# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodesHelper(self, root: TreeNode, current_branch_max):
        if root is None:
            return 0

        good_nodes = 0
        
        if root.val >= current_branch_max:
            good_nodes += 1
            current_branch_max = root.val
        
        good_nodes += self.goodNodesHelper(root.left, current_branch_max)
        good_nodes += self.goodNodesHelper(root.right, current_branch_max)

        return good_nodes

    def goodNodes(self, root: TreeNode) -> int:
        return 1 + self.goodNodesHelper(root.left, root.val) + self.goodNodesHelper(root.right, root.val)
        