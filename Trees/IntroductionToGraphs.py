from collections import deque
class Node:
    def __init__(self,data):
        self.data=data
        self.children=[]
#Adjency matrix
def add_matrix_edge(mat,i,j):
    mat[i][j]=1
    mat[j][i]=1

def display_matrix(mat):
    for row in mat:
        print(" ".join(map(str,row)))

mat=[[0]*4 for _ in range(4)]
add_matrix_edge(mat, 0, 1)
add_matrix_edge(mat, 0, 2)
add_matrix_edge(mat, 1, 2)
add_matrix_edge(mat, 2, 3)
print("Adjacency Matrix:")
# display_matrix(mat)
#Adjency list
def add_edge(adj, i, j):
    adj[i].append(j)
    adj[j].append(i)
def display_list(adj):
    for i in range(len(adj)):
        print(f"{i}: ",end="")
        for j in adj[i]:
            print(j,end=" ")
        print()
adj=[[] for _ in range(4)]
add_edge(adj,0,1)
add_edge(adj, 0, 2)
add_edge(adj, 1, 2)
add_edge(adj, 2, 3)
print("Adjacency List Representation:")
# display_list(adj)

#DFS_REC
def dfs_rec(adj,visited,s):
    visited[s]=True
    print(s,end=" ")
    for i in adj[s]:
        if not visited[i]:
            dfs_rec(adj,visited,i)

#dfs de la o sursa stiute
def dfs(adj,s):
    visited=[False]*len(adj)
    dfs_rec(adj,visited,s)

def all_dfs(adj):
    visited=[False]*len(adj)
    for i in range(len(adj)):
        if not visited[i]:
            dfs_rec(adj,visited,i)

V = 5

    # Create an adjacency list for the graph
adj = [[] for _ in range(V)]

    # Define the edges of the graph
edges = [[1, 2], [1, 0], [2, 0], [2, 3], [2, 4]]

    # Populate the adjacency list with edges
for e in edges:
    add_edge(adj, e[0], e[1])
display_list(adj)
source=1
dfs(adj,source)
print()
print("Complete DFS of the graph:")
all_dfs(adj)

