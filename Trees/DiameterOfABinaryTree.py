# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: [TreeNode]) -> int:
        self.res=0
        def dfs(root):
            if not root:
                return 0
            height_left=dfs(root.left)
            height_right=dfs(root.right)
            self.res=max(self.res,height_left+height_right)
            return 1+max(height_right,height_left)
        dfs(root)
        return self.res
