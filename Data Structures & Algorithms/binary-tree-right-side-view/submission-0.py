# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        fringe = [root]
        output = []
        while fringe:
            output.append(fringe[-1].val)

            new_fringe = []

            for node in fringe:
                if node.left is not None:
                    new_fringe.append(node.left)
                if node.right is not None:
                    new_fringe.append(node.right)
            
            fringe = new_fringe
        
        return output