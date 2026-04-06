# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

    def dfs_srlz(self, root):
        if root is None:
            return "nnnnnn"
        
        left_index = self.dfs_srlz(root.left)
        right_index = self.dfs_srlz(root.right)

        my_index = len(self.running_str) * 18

        self.running_str.append(f"{root.val:06}{left_index:06}{right_index:06}")

        return my_index

    def dfs_desert(self, string, index):
        me = TreeNode(int(string[index:index+6]))
        if string[index+6:index+12] != "nnnnnn":
            left = self.dfs_desert(string, int(string[index+6:index+12]))
        else:
            left = None
        if string[index+12:index+18] != "nnnnnn":
            right = self.dfs_desert(string, int(string[index+12:index+18]))
        else:
            right = None
        
        me.left = left
        me.right = right

        return me

    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.running_str = []
        self.dfs_srlz(root)

        print(self.running_str)

        self.real_str = "".join(self.running_str)

        print(self.real_str)

        return self.real_str

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if len(data) == 0:
            return None
        
        return self.dfs_desert(data, len(data) - 18)
        
        
