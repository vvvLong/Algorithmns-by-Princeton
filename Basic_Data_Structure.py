#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 21:23:19 2019

@author: victor
"""

#%% Node

class Node(object):
    '''
    a simple node with only item and next
    '''
    def __init__(self, item = None):
        self.item = item
        self.next = None
        
'''        
a = Node()
a.item = 'ok'

b = Node('not ok')

a.next = b

a.next.item

a.next.next
'''



#%% Stack (LIFO)

class Stack(object):
    '''
    push-down stack 
    linked list implementation
    '''
    def __init__(self, N = 0):
        self.first = None
        self.N = N
        
    def __iter__(self):
        node = self.first
        while node:
            yield node.item
            node = node.next

    def isEmpty(self):
        return self.N == 0
    
    def size(self):
        return self.N
    
    def push(self, item):
        oldfirst = self.first
        self.first = Node()
        self.first.item = item
        self.first.next = oldfirst
        self.N += 1
        
    def pop(self):
        item = self.first.item
        self.first = self.first.next
        self.N -= 1
        return item


'''
s = Stack()
test_str = 'EASYQUESTION'
for element in test_str:
    s.push(element)       

s.isEmpty()

while s.N > 0:  
    print(s.pop())
    
s.isEmpty()
'''





#%% Queue (FIFO)

class Queue(object):
    '''
    LIFO queue
    linked-list implementation
    '''
    def __init__(self, N = 0):
        self.first = None
        self.last = None
        self.N = N
        
    def __iter__(self):
        node = self.first
        while node:
            yield node.item
            node = node.next
        
    def isEmpty(self):
        return self.first == None
    
    def size(self):
        return self.N
    
    def enqueue(self, item):
        oldlast = self.last
        self.last = Node()
        self.last.item = item
        self.last.next = None
        if self.isEmpty():
            self.first = self.last
        else:
            oldlast.next = self.last
        self.N += 1
        
    def dequeue(self):
        if not self.isEmpty():        
            item = self.first.item
            self.first = self.first.next
            if self.isEmpty():
                self.last = None
            self.N -= 1
            return item
        else:
            print ('Queue is already empty')
            
            
            
'''
q = Queue()
test_str = 'EASYQUESTION'
for element in test_str:
    q.enqueue(element)       

q.isEmpty()

while q.N > 0:  
    print(q.dequeue())
    
q.isEmpty()

q.dequeue()
'''






#%% Bag

class Bag(object):
    '''
    A bag is a collection where removing items is not supported
    '''
    def __init__(self, first = None, N = 0):
        self.first = first
        self.N = N
        
    def __iter__(self):
        node = self.first
        while node:
            yield node.item
            node = node.next
        
    def add(self, item):
        oldfirst = self.first
        self.first = Node()
        self.first.item = item
        self.first.next = oldfirst
        self.N += 1
     
    
    
    
'''    
b = Bag()
test_str = 'EASYQUESTION'
for element in test_str:
    b.add(element)     
    
    
ite = b.__iter__()   
    
for i in ite:
    print (i)
'''


