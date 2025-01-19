# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: [TreeNode], q: [TreeNode]) -> bool:
        if not p and not q:
            return True
        if p and q and p.val==q.val:
            left_dfs=self.isSameTree(p.left,q.left)
            right_dfs=self.isSameTree(p.right,q.right)
            return left_dfs and right_dfs
        else:
            return False

