#!/usr/bin/env python
# coding: utf-8

# In[19]:


from collections import defaultdict 
import sys

class Graph: 
  
    def __init__(self,vertices): 
        self.V= vertices
        self.graph = []
    def addEdge(self,u,v,w): 
        self.graph.append([u, v, w]) 

    def printDist(self, dist): 
        for i in range(self.V):
            if dist[i]!=float("inf"):
                print("%d %d" % (i, dist[i]))
            else:
                print("%d inf" % i)

    def BellmanFord(self, src): 
        previous=[False] * self.V 
        dist = [float("Inf")] * self.V 
        dist[src] = 0 
 
        for i in range(self.V - 1): 
            change = False
            for u, v, w in self.graph: 
                if dist[u] != float("Inf") and dist[u] + w < dist[v]: 
                        dist[v] = dist[u] + w
                        change = True
            if not(change):
                self.printDist(dist)
                return
                        
  
        for u, v, w in self.graph: 
                if dist[u] != float("Inf") and dist[u] + w < dist[v]: 
                        print ("NEGATIVE WEIGHT CYCLE")
                        return

lines = sys.stdin.readlines()
line = lines[0]
n=int(line.split()[0])
m=int(line.split()[1])
s=int(line.split()[2])
G=Graph(n)

for i in range(m):
    line=lines[i+1]
    u=int(line.split()[0])
    v=int(line.split()[1])
    w=float(line.split()[2])
    G.addEdge(u,v,w)
G.BellmanFord(s)
# ## 

# # 
