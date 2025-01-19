class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.right=right
        self.left=left

def invertTree(root:[TreeNode]):
    if not root:
        return None
    tmp=root.left
    root.left=root.right
    root.right=tmp
    invertTree(root.left)
    invertTree(root.right)
    return root