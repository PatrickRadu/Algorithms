# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    # def levelOrder(self, root: [TreeNode]):
    #     res=[]
    #     q=collections.deque()
    #     q.append(root)
    #     while q:
    #         qLen=len(q)
    #         level=[]
    #         for i in range(qLen):
    #             node=q.popleft()
    #             if node:
    #                 level.append(node.val)
    #                 q.append(node.left)
    #                 q.append(node.right)
    #         if level:
    #             res.append(level)
    #     return res

    def levelOrder(self,root:[TreeNode]):
        res=[]
        def dfs(root,depth):
            if root is None:
                return None
            if len(res) == depth:
                res.append([])
            res[depth].append(root.val)
            dfs(root.left,depth+1)
            dfs(root.right,depth+1)
        dfs(root,0)
        return res


