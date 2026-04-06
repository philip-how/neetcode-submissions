# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def search(self, root: Optional[TreeNode]):
        """
        Returns:
        (one sided best, overall best)
        """
        if root is None:
            return float("-inf"),float("-inf")
        
        left_best, left_overall = self.search(root.left)
        right_best, right_overall = self.search(root.right)

        left_best = max(0, left_best)
        right_best = max(0, right_best)

        best_no_turn = max(left_best, right_best) + root.val
        best_overall = max(left_best + right_best + root.val, left_overall, right_overall)

        return best_no_turn, best_overall

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        return self.search(root)[1]
        