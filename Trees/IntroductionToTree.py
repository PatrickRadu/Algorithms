from collections import deque
class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

firstNode = Node(2)
secondNode = Node(3)
thirdNode = Node(4)
fourthNode = Node(5)
firstNode.left = secondNode
firstNode.right = thirdNode
secondNode.left = fourthNode


def in_order_dfs(node):
    if node is None:
        return
    in_order_dfs(node.left)
    print(node.data,end=' ')
    in_order_dfs(node.right)

def pre_order_dfs(node):
    if node is None:
        return
    print(node.data,end=' ')
    pre_order_dfs(node.left)
    pre_order_dfs(node.right)

def post_order_dfs(node):
    if node is None:
        return
    post_order_dfs(node.left)
    post_order_dfs(node.right)
    print(node.data,end=' ')
root = Node(2)
root.left = Node(3)
root.right = Node(4)
root.left.left = Node(5)

print("In-order DFS: ", end='')
in_order_dfs(root)
print("Pre-order DFS: ",end='')
pre_order_dfs(root)
print("Post-order DFS: ",end='')
post_order_dfs(root)

def insert(root,key):
    if root is None:
        return Node(key)
    queue=deque([root])
    while queue:
        temp=queue.popleft()
        if temp.left is None:
            temp.left=Node(key)
            break
        else:
            queue.append(temp.left)
        if temp.right is None:
            temp.right=Node(key)
            break
        else:
            queue.append(temp.right)
    return root

def searchDFS(root,value):
    if root is None:
        return False
    if root==value:
        return True
    search_left=searchDFS(root.left)
    search_right=searchDFS(root.right)
    return search_left or search_right