# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.result = None
        self.k = k
        self.attachPosLeft(root, 0)

        return self.result.val

    def attachPosLeft(self, root: Optional[TreeNode], count):
        if root is None:
            return 0
        
        left = self.attachPosLeft(root.left, count)
        right = self.attachPosLeft(root.right, count + left + 1)

        if left + count + 1 == self.k:
            self.result = root
            

        return left + right + 1



    # def attachSizing(self, root: Optional[TreeNode], dictionary: dict):
    #     if root is None:
    #         return 0
    #     left_count = self.attachSizing(root.left, dictionary)
    #     right_count = self.attachSizing(root.right, dictionary)

    #     my_count = left_count + right_count + 1
    #     dictionary[root.val] = my_count

    #     return my_count 
