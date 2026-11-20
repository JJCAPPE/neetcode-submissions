# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxdiam = 0

    
        def dfs_depth(root: Optional[TreeNode]) -> int:
            nonlocal maxdiam
            if not root:
                return 0
            
            left = dfs_depth(root.left)
            right = dfs_depth(root.right)

            maxdiam = max(maxdiam, left+right)
            
            return 1+max(left, right)

        dfs_depth(root)
        return(maxdiam)