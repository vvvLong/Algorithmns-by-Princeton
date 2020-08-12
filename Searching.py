#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 21:15:36 2019

@author: victor
"""

#%% Linked list and sequential search

class snode(object):
    '''
    sequential search node
    '''
    def __init__(self, key=None, value=None, next_node=None):
        self.key = key
        self.value = value
        self.next = next_node
 

'''       
x = snode()
x.next
x = snode('a',1)
y = snode('b',2)
x.key
x.next = y
x.next
x.next.key
'''

class sequential_search(object):
    '''
    sequential search with linked list
    '''
    def __init__(self):
        self.first = None
    
    # public insert     
    def put(self, key, value):
        x = self.first
        while x is not None:
            if x.key ==  key:
                x.value = value
                return
            x = x.next
        self.first = snode(key, value, self.first)

    # public search
    def get(self, key):
        x = self.first
        while x is not None:
            if x.key == key:
                return x.value
            x = x.next
        return 'Not in the list'



ss = sequential_search()
test_str = 'EASYQUESTION'
for (index, element) in enumerate(test_str):
    ss.put(element, index)       
  

ss.get('A')      
ss.get('E') 
ss.get('Z')
ss.first.key





#%% Binary Search







#%% Binary search tree

class btnode(object):
    '''
    binary tree node
    '''
    def __init__(self, key = None, val = None, n = 0):
        self.key = key
        self.value = val
        self.N = n
        self.left = None
        self.right = None 
    
    # public function for getting size
    def size(self):
        return self.N

'''    
x = btnodenode(1,'a',1)
x.left = 2
x.left     
x.key
x.value
x.N
x.right

y = btnodenode(10,'B',2)
y.right = x
y.right
x
y
'''

class binary_search_tree(object):
    '''
    binary searh tree
    '''
    def __init__(self):
        self.root = None
    
    # function for node size    
    def node_size(self, btnode):
        if btnode == None:
            return 0
        else:
            return btnode.N
        
    # function for tree size    
    def size(self):
        if self.root == None:
            return 0
        else:
            return self.root.N
    
    # public function for searching value
    def get(self, key):
        return self._get(self.root, key)
    
    # private search function, recursive 
    def _get(self, cur_node, key):
        if cur_node == None:
            return 'Empty'
        if key > cur_node.key:
            self._get(cur_node.right, key)
        elif key < cur_node.key:
            self._get(cur_node.left, key)
        else:
            return cur_node.value
       
    # public function for inserting value
    def put(self, key, value):
        if self.root == None:
            self.root = btnode(key,value,1)
        else:
            self._put(self.root, key, value)
    
    # private function for inserting, recursive
    def _put(self, cur_node, key, value):               
        if key > cur_node.key:
            if cur_node.right == None:  
                cur_node.right = btnode(key, value, 1) 
            else:
                self._put(cur_node.right, key, value)
        elif key < cur_node.key:
            if cur_node.left == None:  
                cur_node.left = btnode(key, value, 1) 
            else:
                self._put(cur_node.left, key, value)
        else:            
            cur_node.value = value
        # calculate size recursively        
        cur_node.N = self.node_size(cur_node.left) + \
                     self.node_size(cur_node.right) + 1
    
    '''
    # public function for inserting value
    def put(self, key, value):
        self._put(self.root, key, value)
    
    # private function for inserting, recursive
    def _put(self, cur_node, key, value):
        if cur_node == None:
            cur_node = btnode(key, value, 1) # seems like this line doesn't work         
        elif key > cur_node.key:
            self._put(cur_node.right, key, value)
        elif key < cur_node.key:
            self._put(cur_node.left, key, value)
        else:            
            cur_node.value = value
        # calculate size recursively        
        cur_node.N = self.node_size(cur_node.left) + \
                     self.node_size(cur_node.right) + 1
    '''
    
    # print tree                 
    def print_tree(self):
        if self.root!=None:
            self._print_tree(self.root)
            
    def _print_tree(self,cur_node):
        if cur_node!= None:
            self._print_tree(cur_node.left)
            print (str(cur_node.key))
            self._print_tree(cur_node.right)
            
    # public find min
    def min(self):
        return self._min(self.root)

    # private find min, recursive
    def _min(self, cur_node):
        if cur_node == None:
            return 'Empty'
        if cur_node.left == None:
            return cur_node
        else:
            return self._min(cur_node.left)
                    
    # public find max
    def max(self):
        return self._max(self.root)
    
    # private max, recursive
    def _max(self, cur_node):
        if cur_node == None:
            return 'Empty'
        if cur_node.right == None:
            return cur_node
        else:
            return self._max(cur_node.right)
        
    # public floor (largest value <= key)
    def floor(self, key):
        return self._floor(self.root, key)
    
    # private floor, recursive
    def _floor(self, cur_node, key):
        if cur_node == None:
            return None
        if cur_node.key == key:
            return cur_node.key
        elif cur_node.key > key:
            return self._floor(cur_node.left, key)
        else:
            x = self._floor(cur_node.right, key)
            if  x == None:
                return cur_node.key
            else:
                return x
    
    # public ceiling (smallest >= key)
    def ceiling(self, key):
        return self._ceiling(self.root, key)
    
    # private ceiling, recursive
    def _ceiling(self, cur_node, key):
        if cur_node == None:
            return None
        if key == cur_node.key:
            return cur_node.key
        elif key > cur_node.key:
            return self._ceiling(cur_node.right, key)
        else:
            x = self._ceiling(cur_node.left, key)
            if x == None:
                return cur_node.key
            else:
                return x
    
    # public select (find the key that has k keys smaller than it)
    def select(self, k):
        return self._select(self.root, k)
    
    # private select, recursive
    def _select(self, cur_node, k):
        if cur_node == None:
            return None
        t = self.node_size(cur_node.left)
        if k == t:
            return cur_node.key
        elif k < t:
            return self._select(cur_node.left, k)
        else:
            return self._select(cur_node.right,k-t-1)
    
    # public function rank
    def rank(self, key):
        return self._rank(self.root, key)
    
    # private rank, recursive
    def _rank(self, cur_node, key):
        if cur_node == None:
            return 0
        if key == cur_node.key:
            return self.node_size(cur_node.left)
        elif key < cur_node.key:
            return self._rank(cur_node.left, key)
        else:
            return self.node_size(cur_node.left) + 1 + \
                   self._rank(cur_node.right, key)
    
    # public fucntion for delete min
    def deleteMin(self):
        self.root = self._deleteMin(self.root)
        
    # private function deleteMin
    def _deleteMin(self, cur_node):
        if cur_node.left == None:
            return cur_node.right
        cur_node.left = self._deleteMin(cur_node.left)
        cur_node.N = self.node_size(cur_node.left) + \
                        self.node_size(cur_node.right) + 1
        return cur_node
    
    # public function for delete
    def delete(self, key):
        self.root == self._delete(self.root, key)
        
    # private function delete
    def _delete(self, cur_node, key):
        if cur_node == None:
            return None
        if key > cur_node.key:
            cur_node.right = self._delete(cur_node.right, key)
        elif key < cur_node.key:
            cur_node.left = self._delete(cur_node.left, key)
        else:
            if cur_node.left == None:
                return cur_node.right
            if cur_node.right == None:
                return cur_node.left
            t = cur_node
            cur_node = self._min(t.right)
            cur_node.right = self._deleteMin(t.right)
            cur_node.left = t.left
        
        cur_node.N = self.node_size(cur_node.left) + \
                     self.node_size(cur_node.right) + 1
        return cur_node
    
    
    
    
    
        
bst = binary_search_tree()

'''
bst.put('element', 'index') 
bst.root == None   
bst.root
'''


test_str = 'EASYQUESTION'
for (index, element) in enumerate(test_str):
    bst.put(element, index)       
        
bst.get('E')          
        
bst.size() 
bst.root.N            
bst.print_tree()        
      


bst.min().key
bst.min().value

bst.max().key
bst.max().value


bst.floor('M')

bst.ceiling('Z')

bst.select(6)

bst.rank('M')

bst.deleteMin()


bst.delete('Y')



#%% Red-Black Balanced Search Trees

class rbnode(object):
    '''
    node for Red-Black tree
    same as node for BST except for color
    red = 1
    black = 0
    '''
    def __init__(self, key = None, value = None, color = 1, N = 0):
        self.key = key
        self.value = value
        self.N = N
        self.left = None
        self.right = None
        self.color = color
        

x = rbnode()
x.N
x.color = 0
x.color


class red_black_tree(object):
    '''
    Left leaning Red-Black balanced search tree
    similar to BST
    insert is more complicated
    '''
    def __init__(self):
        self.root = None
    
    # function for node size    
    def node_size(self, node):
        if node == None:
            return 0
        else:
            return node.N
        
    # function for tree size    
    def size(self):
        if self.root == None:
            return 0
        else:
            return self.root.N
    
    # if the node is red    
    def isRed(self, cur_node):
        if cur_node == None:
            return False
        return cur_node.color == 1
    
    # rotate left
    def rotateLeft(self, cur_node):
        x = cur_node.right
        cur_node.right = x.left
        x.left = cur_node
        x.color = cur_node.color
        cur_node.color = 1
        return x
    
     # rotate right
    def rotateRight(self, cur_node):
        x = cur_node.left
        cur_node.left = x.right
        x.right = cur_node
        x.color = cur_node.color
        cur_node.color = 1
        return x
     
    # flip color
    def flipColor(self, cur_node):
        cur_node.left.color = 0
        cur_node.right.color = 0
        cur_node.color = 1
        
    # insert, public
    def put(self, key, value):
        if self.root == None:
            self.root = rbnode(key, value, color = 0, N = 1)
        else:
            self._put(self.root, key, value)
    
    # insert, private    
    def _put(self, cur_node, key, value):
        # same process as BST
        if key > cur_node.key:
            if cur_node.right == None:  
                cur_node.right = rbnode(key, value, N = 1) 
            else:
                self._put(cur_node.right, key, value)
        elif key < cur_node.key:
            if cur_node.left == None:  
                cur_node.left = rbnode(key, value, N = 1) 
            else:
                self._put(cur_node.left, key, value)
        else:            
            cur_node.value = value
            
        # rotate and reorganise color    
        if self.isRed(cur_node.right) and not self.isRed(cur_node.left):
            cur_node = self.rotateLeft(cur_node)
            
        if self.isRed(cur_node.left) and cur_node.left.left \
        and self.isRed(cur_node.left.left):
            cur_node = self.rotateRight(cur_node)
            
        if self.isRed(cur_node.right) and self.isRed(cur_node.left):
            self.flipColor(cur_node)
        
        # calculate size recursively        
        cur_node.N = self.node_size(cur_node.left) + \
                     self.node_size(cur_node.right) + 1
    
    # public function for searching value
    def get(self, key):
        return self._get(self.root, key)
    
    # private search function, recursive 
    def _get(self, cur_node, key):
        if cur_node == None:
            return 'Empty'
        if key > cur_node.key:
            self._get(cur_node.right, key)
        elif key < cur_node.key:
            self._get(cur_node.left, key)
        else:
            return cur_node.value
    
 
    
    
    
rbt = red_black_tree()
  
test_str = 'EASYQUESTION'
for (index, element) in enumerate(test_str):
    rbt.put(element, index)       
        
rbt.get('E')  



    
    
#%% Hash table: separate chaining
                     
class separate_chaining_ht(object):
    '''
    separate chaining hash table
    form a list of sequential search object
    '''
    def __init__(self, n=0, m=997):
        self.n = n # number of nodes
        self.m = m # number of chains/hash table size
        self.st = [sequential_search()] * m # ss chain
        
    def _hash(self, key):
        return hash(key) & 0x7fffffff % self.m

    def put(self, key, value):
        self.st[self._hash(key)].put(key, value)
        
    def get(self, key):
        return self.st[self._hash(key)].get(key)
    
    
    
scht = separate_chaining_ht()
  
test_str = 'EASYQUESTION'
for (index, element) in enumerate(test_str):
    scht.put(element, index)       
        
scht.get('E')     
    
scht.m    
    



    
#%% Hash table: linear probing

    
class linear_probing_ht(object):
    '''
    Hash table with linear-probing strategy
    making sure that 1/2 of the list is empty
    '''
    def __init__(self, m=16):
        self.n = 0
        self.m = m
        self.keys = [None]*m
        self.values = [None]*m
    
    # private hash function   
    def _hash(self, key):
        return hash(key) & 0x7fffffff % self.m
    
    # private doubling the size    
    def _resize(self, size):
        tmp = linear_probing_ht(m=size)
        for i in range(self.m):
            if self.keys[i] is not None:
                tmp.put(self.keys[i], self.values[i])
        self.m = tmp.m
        self.keys = tmp.keys
        self.values = tmp.values
    
    # public insert    
    def put(self, key, value):
        if self.n >= self.m/2:
            self._resize(self.m*2)
        i = self._hash(key)
        while self.keys[i] is not None:
            if self.keys[i] == key:
                self.values[i] = value
                return 
            i = (i+1) % self.m
        self.keys[i] = key
        self.values[i] = value
        self.n += 1
     
    # public search    
    def get(self, key):
        i = self._hash(key)
        while self.keys[i] is not None:
            if self.keys[i] == key:
                return self.values[i]
            i = (i+1) % self.m
        return 'Key is not in the table'
    
    # private check if contain the key
    def _contain(self, key):
        i = self._hash(key)
        while self.keys[i] is not None:
            if self.keys[i] == key:
                return True
            i = (i+1) % self.m
        return False  

    # public delete
    def delete(self, key):
        if not self._contain(key):
            return 'key do not exist'
        # delete key and value
        i = self._hash(key)
        while self.keys[i] != key:
            i = (i+1) % self.m
        self.keys[i] = None
        self.values[i] = None
        self.n -= 1
        # reorder the rest of the cluster
        i = (i+1) % self.m
        while self.keys[i] is not None:
            k, v = self.keys[i], self.values[i]
            self.keys[i] = None
            self.values[i] = None
            self.n -= 1
            self.put(k, v)
            i = (i+1) % self.m
        # shrink size if n = m/8
        if self.n>0 and self.n == self.m / 8:
            self._resize(self.m / 2)
        
        
  
      

lpht = linear_probing_ht(4)
  
test_str = 'EASYQUESTION'
for (index, element) in enumerate(test_str):
    lpht.put(element, index)       
    
lpht.m  
lpht.n

lpht.get('a')
lpht.get('A')
lpht.get('E')

lpht.keys

lpht.delete('S')
lpht.keys


hash('S')%32
hash('Y')%32

