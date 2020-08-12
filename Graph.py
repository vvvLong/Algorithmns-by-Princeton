#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 21:11:49 2019

@author: victor
"""

#%% import lib

from Basic_Data_Structure import Bag, Queue, Stack


#%% Undirected Graph
###############################################################################
###############################################################################

#%% Graph

class Graph(object):
    '''
    graph object
    '''
    def __init__(self): 
        self.adj = {}
        self.V = 0
        self.E = 0
        
    def vertices_size(self):
        return self.V
    
    def edges_size(self):
        return self.E
    
    def has_edge(self, v, w):
        if v not in self.adj or w not in self.adj:
            return False
        return next((True for i in self.adj[v] if i == w), False)
         
    def add_edge(self, v, w):
        if v==w or self.has_edge(v,w): # no self cycle or parallel edges
            return
        if v not in self.adj:
            self.adj[v] = Bag() # initialize as bag
        if w not in self.adj:
            self.adj[w] = Bag() # initialize as bag
        self.adj[v].add(w)
        self.adj[w].add(v)
        self.E += 1
        self.V = len(self.adj.keys()) # update number of vertices
        
    def __repr__(self):
        g = 'Graph: '+str(self.V)+' vertices, '+str(self.E)+' edges'+'\n'+  \
            '-'*50+'\n'
        for v in self.adj:
            edge = str(v)+': '
            for w in self.adj[v]:
                edge += str(w)+', '
            edge = edge[:-2] + '\n' 
            g += edge      
        return g 



'''

g = Graph()

test_data = [(0, 5), (4, 3), (0, 1), (9, 12), (6, 4), (5, 4), (0, 2),  
             (11, 12), (9, 10), (0, 6), (7, 8), (9, 11), (5, 3), 
             (3, 5), (0, 3)]

for a, b in test_data:
    g.add_edge(a, b)

g.vertices_size()
g.edges_size()

g

'''



#%% Depth-first search

class DepthFirstPaths(object):
    '''
    using depth-first search to find all paths of the source in the graph
    '''
    def __init__(self, graph, source):
        self.marked = {}
        self.edgeTo = {}
        self.source = source
        self._dfs(graph, source)
        
    def _dfs(self, graph, v):
        self.marked[v] = True
        for w in graph.adj[v]:
            if w not in self.marked:
                self.edgeTo[w] = v
                self._dfs(graph, w)
        
    def hasPathTo(self, v):
        return v in self.marked
    
    def pathTo(self, v):
        if not self.hasPathTo(v):
            return None
        path = Stack()
        tmp = v
        while tmp != self.source:
            path.push(tmp)
            tmp = self.edgeTo[tmp]
        path.push(self.source)
        return path
        
   
    
    
'''  
      
g = Graph()        
test_data = [(0, 5), (2, 4), (2, 3), (1, 2), (0, 1), (3, 4), (3, 5), (0, 2)]        
for a, b in test_data:
    g.add_edge(a, b)        
g        
        
dfp = DepthFirstPaths(g,0)        
        
dfp.marked        
        
dfp.edgeTo        
        
dfp.hasPathTo(2)        
 
path = ''       
for i in dfp.pathTo(4):
    path += str(i) + ' -> '
print (path[:-4])   
  
'''        
        
        
        
#%% Breadth-first search

class BreadthFirstPaths(object):
    '''
    using breadth-first search to find all paths of the source in the graph        
    '''
    def __init__(self, graph, source):
        self.source = source
        self.edgeTo = {}
        self.marked = {}
        self.distance = {self.source:0}
        self._bfs(graph, source)
        
    def _bfs(self, graph, source):
        q = Queue()
        self.marked[source] = True
        q.enqueue(source)
        while not q.isEmpty():
            v = q.dequeue()
            dist = self.distance[v]
            for w in graph.adj[v]:
                if w not in self.marked:
                    q.enqueue(w)
                    self.marked[w] = True
                    self.edgeTo[w] = v
                    self.distance[w] = dist + 1
                    
    def hasPathTo(self, v):
        return v in self.marked
    
    def pathTo(self, v):
        if not self.hasPathTo(v):
            return None
        path = Stack()
        tmp = v
        while tmp != self.source:
            path.push(tmp)
            tmp = self.edgeTo[tmp]
        path.push(self.source)
        return path
        
    def distanceTo(self, v):
        if not self.hasPathTo(v):
            return None
        return self.distance[v]
        
    def maxDistance(self):
        return max(self.distance.values())





'''  
      
g = Graph()        
test_data = [(0, 5), (2, 4), (2, 3), (1, 2), (0, 1), (3, 4), (3, 5), (0, 2)]        
for a, b in test_data:
    g.add_edge(a, b)        
g        
        
bfp = BreadthFirstPaths(g,0)        
        
bfp.marked        
        
bfp.edgeTo        
        
bfp.hasPathTo(2)        
 
path = ''       
for i in bfp.pathTo(4):
    path += str(i) + ' -> '
print (path[:-4])   
  
bfp.distanceTo(4)

bfp.maxDistance()

bfp.distance

'''    



#%% Connected componets

class ConnectedComponents(object):
    '''
    using depth-first search to find all connected clusters
    '''
    def __init__(self, graph):
        self.marked = {}       
        self.id = {}
        self.count = 0
        
        for v in graph.adj.keys():
            if v not in self.marked:                
                self._dfs(graph, v)
                self.count += 1
                
    def _dfs(self, graph, v):
        self.marked[v] = True        
        self.id[v] = self.count
        for w in graph.adj[v]:
            if w not in self.marked:
                self._dfs(graph, w)
                
    def connected(self, v, w):
        return self.id[v] == self.id[w]
    
    def vertexId(self, v):
        return self.id[v]
    
    def count(self):
        return self.count
    
    
'''    
    
g = Graph()
test_data = [(0, 5), (4, 3), (0, 1), (9, 12), (6, 4), (5, 4), (0, 2),  
             (11, 12), (9, 10), (0, 6), (7, 8), (9, 11), (5, 3), 
             (3, 5), (0, 3)]
for a, b in test_data:
    g.add_edge(a, b) 
 
g
    
cc = ConnectedComponents(g)    

cc.count
    
cc.id    

cc.vertexId(2)

cc.connected(1,11)    

'''



#%% Cycle

class Cycle(object):
    '''
    using DFS to check if there is cycle in the graph
    '''
    def __init__(self, graph):
        self._marked = {}
        self._hasCycle = False
        
        for v in graph.adj.keys():
            if v not in self._marked:
                self._dfs(graph, v, v)
            
    def _dfs(self, graph, v, u):
        self._marked[v] = True
        for w in graph.adj[v]:
            if w not in self._marked:
                self._dfs(graph, w, v) # be very careful
            else:
                # always exist a cycle if next vertice is marked
                if w != u: # check no self loop (previous vertex not equal to the next)
                    self._hasCycle = True

    def hasCycle(self):
        return self._hasCycle



'''

g1 = Graph()
g2 = Graph()
test_data = [(0, 1), (0, 2), (0, 6), (0, 5), (3, 5), (6, 4)]
test_data2 = [(0, 1), (0, 2), (0, 6), (0, 5), (3, 5), (6, 4), (3, 4)]
for a, b in test_data:
    g1.add_edge(a, b)
for a, b in test_data2:
    g2.add_edge(a, b)

g1
g2

cycle = Cycle(g1)
cycle.hasCycle()

cycle = Cycle(g2)
cycle.hasCycle()

'''




#%% Two color (Bipartite)

class TwoColor(object):
    '''
    using DFS to check if every edge of the graph linked by two vertices that 
    belong to two different colors (e.g. black and red)?
    '''
    def __init__(self, graph):
        self._marked = {}
        self._color = {}
        self._bipartite = True
        
        for v in graph.adj.keys():
            if v not in self._marked: 
                self._color[v] = True
                self._dfs(graph, v)

    def _dfs(self, graph, v):
        self._marked[v] = True    
        for w in graph.adj[v]:
            if w not in self._marked:
                self._color[w] = not self._color[v]
                self._dfs(graph, w)
            else:
                if self._color[v] == self._color[w]:
                    self._bipartite = False 

    def isBipartite(self):
        return self._bipartite
    
  

'''
    
g = Graph()
test_data = [(0, 5), (2, 4), (2, 3), (1, 2), (0, 1), (3, 4), (3, 5), (0, 2)]       
for a, b in test_data:
    g.add_edge(a, b)        
        
g    
    
tc = TwoColor(g)

tc.isBipartite()

tc._color

'''





#%% Directed Graph
###############################################################################
###############################################################################

#%% Digraph

class Digraph(object):
    '''
    directed graph
    every edge has direction
    very similar to undirected graph
    adding attribute 'vertices' as set, previous dictionary key didn't work
    '''
    def __init__(self): 
        self._adj = {}
        self._V = 0
        self._E = 0
        self._vertices = set()
        
    def __repr__(self):
        g = 'Graph: '+str(self._V)+' vertices, '+str(self._E)+' edges'+'\n'+  \
            '-'*50+'\n'
        for v in self._adj:
            edge = str(v)+': '
            for w in self._adj[v]:
                edge += str(w)+', '
            edge = edge[:-2] + '\n' 
            g += edge      
        return g 
        
    def vertices_size(self):
        return self._V
    
    def edges_size(self):
        return self._E
    
    def has_edge(self, start, end):
        '''
        the two inputs have order now
        '''
        if start not in self._adj:
            return False
        return next((True for i in self._adj[start] if i == end), False)
         
    def add_edge(self, start, end):
        if start==end or self.has_edge(start,end): # no self cycle or parallel edges
            return
        if start not in self._adj:
            self._adj[start] = Bag() # initialize as bag
        self._adj[start].add(end)
        self._vertices.add(start)
        self._vertices.add(end)
        self._E += 1
        self._V = len(self._vertices) # update number of vertices
        
    def reverse(self):
        g = Digraph()
        for v in self._adj.keys():
            for w in self._adj[v]:
                g.add_edge(w,v)
        return g
    
    def vertices(self):
        return self._vertices


        
'''

dg = Digraph()
test_data = [(4, 2), (2, 3), (3, 2), (6, 0), (0, 1), (2, 0),
             (11, 12), (12, 9), (9, 10), (9, 11), (8, 9), (10, 12),
             (11, 4), (4, 3), (3, 5), (7, 8), (8, 7), (5, 4), (0, 5),
             (6, 4), (6, 9), (7, 6)]      
for a, b in test_data:
    dg.add_edge(a, b)        
        
dg  

dg.reverse()

'''



#%% Directed DFS

class DirectedDFS(object):
    def __init__(self, dgraph, *sources):
        self._marked = {v:False for v in dgraph.vertices()}      
        for s in sources:
            assert(s in dgraph.vertices()), f'source {s} is not in the graph'
            if not self._marked[s]:
                self._dfs(dgraph, s)
                
    def _dfs(self, dgraph, v):
        self._marked[v] = True
        if v in dgraph._adj.keys(): # check if vertex has nodes linked to it
            for w in dgraph._adj[v]:
                if not self._marked[w]:
                    self._dfs(dgraph, w)
                
    def marked(self, v):
        return self._marked[v]


'''

dg = Digraph()
test_data = [(4, 2), (2, 3), (3, 2), (6, 0), (0, 1), (2, 0),
             (11, 12), (12, 9), (9, 10), (9, 11), (8, 9), (10, 12),
             (11, 4), (4, 3), (3, 5), (7, 8), (8, 7), (5, 4), (0, 5),
             (6, 4), (6, 9), (7, 6)]      
for a, b in test_data:
    dg.add_edge(a, b)        
        
dg  

dfs = DirectedDFS(dg, 1,2,6)
[i for i in dg.vertices() if dfs.marked(i)]

'''



#%% Directed Cycle 

class DirectedCycle(object):
    '''
    using DFS to find if the Digraph has cycle
    and 
    return the first cycle found
    using stack to store cycle
    and _onStack to check if vertex on current adj
    '''
    def __init__(self, dgraph):
        self._marked = {v:False for v in dgraph.vertices()}
        self._onStack = {v:False for v in dgraph.vertices()}
        self._cycle = Stack()
        self._edgeTo = {}
        
        for v in dgraph.vertices():
            if not self._marked[v]:
                self._dfs(dgraph, v)
                
    def _dfs(self, dgraph, v):
        self._marked[v] = True
        self._onStack[v] = True
        if v in dgraph._adj.keys(): # check if vertex has nodes linked to it
            for w in dgraph._adj[v]:
                if self.hasCycle():
                    return
                elif not self._marked[w]:
                    self._edgeTo[w] = v # be careful about the order of the two lines
                    self._dfs(dgraph, w)
                elif self._onStack[w]:
                    x = v
                    while x != w:
                        self._cycle.push(x)
                        x = self._edgeTo[x]   
                    self._cycle.push(w)
                    self._cycle.push(v)
        self._onStack[v] = False
        
    def hasCycle(self):
        return not self._cycle.isEmpty()

    def cycle(self):
        if self.hasCycle():    
            return self._cycle
        else:
            return None


'''

dg = Digraph()
test_data = [(4, 2), (2, 3), (3, 2), (6, 0), (0, 1), (2, 0),
             (11, 12), (12, 9), (9, 10), (9, 11), (8, 9), (10, 12),
             (11, 4), (4, 3), (3, 5), (7, 8), (8, 7), (5, 4), (0, 5),
             (6, 4), (6, 9), (7, 6)]      
for a, b in test_data:
    dg.add_edge(a, b)        
        
dg  

dc = DirectedCycle(dg)
        
dc.hasCycle()        

[i for i in dc.cycle()]        
        
'''



#%% Depth-first search order & Topological sorting

class DepthFirstOrder(object):
    '''
    using depth-first search to go through the directed graph;
    preorder is order of dfs() calls
    postorder is order in which vertices are done
    reversePost order is the reversed postorder, and it's the topological order
    '''
    def __init__(self, dgraph):
        self._marked = {v:False for v in dgraph.vertices()}
        self._pre = Queue()
        self._post = Queue()
        self._reversePost = Stack()
        
        for v in dgraph.vertices():
            if not self._marked[v]:
                self._dfs(dgraph,v)
                
    def _dfs(self, dgraph, v):
        self._marked[v] = True
        self._pre.enqueue(v)
        if v in dgraph._adj.keys():
            for w in dgraph._adj[v]:
                if not self._marked[w]:
                    self._dfs(dgraph, w)
        self._post.enqueue(v) # very smart design
        self._reversePost.push(v)
        
    def preOrder(self):
        return self._pre
    
    def postOrder(self):
        return self._post
    
    def reversePostOrder(self):
        return self._reversePost
    
    
    
class TopologicalSort(object):
    '''
    Topological order is the order such that all edges point upwards
    A digraph has a topological order if and only if it is a DAG
    (Directed acyclic graph)
    '''
    def __init__(self, dgraph):
        if not DirectedCycle(dgraph).hasCycle():
            self._order = DepthFirstOrder(dgraph).reversePostOrder()
        else:
            self._order = None
            
    def order(self):
        return self._order
    
    def isDAG(self):
        return self._order is not None
    
    
    
    
'''    
    
dg = Digraph()
test_data = [(2, 3), (0, 6), (0, 1), (2, 0), (11, 12),
             (9, 12), (9, 10), (9, 11), (3, 5), (8, 7),
             (5, 4), (0, 5), (6, 4), (6, 9), (7, 6)]      
for a, b in test_data:
    dg.add_edge(a, b)        
        
dg  

tp = TopologicalSort(dg)   
    
tp.isDAG()    
    
[i for i in tp.order()]    
    
'''    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    






        
        