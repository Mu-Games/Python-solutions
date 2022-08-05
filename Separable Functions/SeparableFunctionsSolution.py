import sys # Not necessary in Domjudge.
import os # Not necessary in Domjudge.


# Code to mimic the Domjudge input.
input_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),'Testsets' ))
testset_numer = 1
sys.stdin = open(os.path.join(input_dir, f'Testset0{testset_numer}.txt'),'r')


# Code to read the Domjudge input.
n = int( sys.stdin.readline() )
k = int( sys.stdin.readline() ) 

a1=[]
a2=[]
i1=[]
i2=[]

for i in range(k):
    a,b,c,d = map(int,sys.stdin.readline().split(' '))

    a1.append(int(a))
    a2.append(int(b))
    i1.append(int(c))
    i2.append(int(d))
    
 
# A recursive function to prDFS starting from v
def BFSUtil(adj, v, visited):

    # Create a queue for BFS
    queue = []

 
    # Mark the current node as visited
    # and enqueue it
    visited[v] = True
    queue.append(v)

 
    # 'i' will be used to get all adjacent
    # vertices of a vertex
    while (len(queue) > 0):
         
        # Dequeue a vertex from queue
        v = queue.pop(0)

        # Get all adjacent vertices of the
        # dequeued vertex s. If a adjacent
        # has not been visited, then mark it
        # visited and enqueue it
        for i in adj[v]:
            if (visited[i] == False):
                visited[i] = True
                queue.append(i)
                 
    return visited
 

def getTranspose(adj, V):
     
    g = [[] for i in range(V)]
 
    for v in range(V):
        for i in adj[v]:
            g[i].append(v)
 
    return g
 
def addEdge(adj, v, w):
     
    # Add w to vs list.
    adj[v].append(w)
    return adj
 
# The main function that returns True if graph
# is strongly connected
def isSC(adj, V):
     
    # St1p 1: Mark all the vertices as not
    # visited (For first BFS)
    visited = [False]*V
 
    # Step 2: Do BFS traversal starting
    # from first vertex.
    visited = BFSUtil(adj, 0, visited)
 
    # If BFS traversal doesnt visit all
    # vertices, then return false.
    for i in range(V):
        if (visited[i] == False):
              return False
 
    # Step 3: Create a reversed graph
    adj = getTranspose(adj, V)
 
    # Step 4: Mark all the vertices as not
    # visited (For second BFS)
    for i in range(V):
        visited[i] = False
 
    # Step 5: Do BFS for reversed graph
    # starting from first vertex.
    # Starting Vertex must be same starting
    # point of first DFS
    visited = BFSUtil(adj, 0, visited)
 
    # If all vertices are not visited in
    # second DFS, then return false
    for i in range(V):
        if (visited[i] == False):
              return False
 
    return True


g = [[] for i in range(2*n)]
for j in range(k):
        
        v1 = n+i1[j] if a1[j]==1 else   i1[j]
        w1=    i2[j] if a2[j]==1 else n+i2[j]
        v2 = n+i2[j] if a2[j]==1 else   i2[j]
        w2 =   i1[j] if a1[j]==1 else n+i1[j]
        
        g = addEdge( g, v1-1, w1-1 )
        g = addEdge( g, v2-1, w2-1 )

print('1' if isSC(g, 2*n) else '0')