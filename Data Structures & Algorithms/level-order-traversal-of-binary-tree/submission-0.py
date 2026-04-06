# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        prev_row = [root]
        output = [[root.val]]
        while True:
            new_row = []
            for node in prev_row:
                if node.left is not None:
                    new_row.append(node.left)
                if node.right is not None:
                    new_row.append(node.right)

            if len(new_row) == 0:
                return output

            output.append([])
            
            for node in new_row:
                output[-1].append(node.val)
            
            prev_row = new_row


