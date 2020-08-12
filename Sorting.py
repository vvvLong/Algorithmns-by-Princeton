#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 20:48:25 2019

@author: victor
"""

#%% create random list

import random

list = random.sample(range(1000),100)

list2 = random.sample(range(1000),10)

list3 = random.sample(range(1000),20)

list5 = random.sample(range(1000),10)


#%% Elementary sort 


def selection_sort(list):
    '''
    First, find the smallest item in the array and exchange it with the first 
    entry (itself if the first entry is already the smallest). Then, find the 
    next smallest item and exchange it with the second entry. Continue in this 
    way until the entire array is sorted.
    
    complexity n^2/2
    '''
    for i in range(len(list)):
        min = i
        for j in range(i+1,len(list)):
            if list[min] > list[j]:
                min = j
        list[i], list[min] = list[min], list[i] # exchange elements
    


def insertion_sort(list):
    '''
    only comparing each element to it's previous elemnts(left) and insert it 
    into the correct position,  which means the elements considered will keep 
    sorted. It is not difficult to speed up insertion sort substantially, by 
    shortening its inner loop to move the larger entries to the right one 
    position rather than doing full exchanges (thus cutting the number of 
    array accesses in half ). 
    
    when the number of inversions is low, insertion sort is likely to be faster 
    than any sorting method that we consider in this chapter.
    
    max complexity n^2/4
    '''
    for i in range(1,len(list)):
        key = list[i]
        j = i - 1 
        while j >= 0 and key < list[j]:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = key # be very careful here, not forget to add 1 back
    


def shell_sort(list):
    '''
    In shellSort, we make the array h-sorted for a large value of h. We keep 
    reducing the value of h until it becomes 1. An array is said to be h-sorted 
    if all sublists of every h\’th element is sorted. We implement insertion 
    sort multiple times until h become 1.
    
    Shellsort gains efficiency by making a tradeoff between size and partial 
    order in the subsequences. At the beginning, the subsequences are short; 
    later in the sort, the subsequences are partially sorted.
    '''
    n = len(list)
    h = n//2
    while h > 0:
        for i in range(h,n):
            key = list[i]
            j = i - h
            while j>=0 and list[j]>key:
                list[j+h] = list[j]
                j -= h
            list[j+h] = key
        h //= 2
    


#selection_sort(list)
#insertion_sort(list)
shell_sort(list)


#%% Mergesort

def merge(list,low,mid,high):
    '''
    a method that merges two disjoint ordered arrays into a third array. This 
    strategy is easy to implement: create an output array of the requisite 
    size and then choose successively the smallest 
    remaining item from the two input arrays to be the next item added to the 
    output array.
    low is the starting point of the list
    mid the last point of the first half
    high is the last point of the list
    '''
    # copy the list
    aux = list[:]
        
    i = low
    j = mid+1    
    for k in range(low,high+1):
        if i>mid:
            list[k] = aux[j]
            j += 1
        elif j>high:
            list[k] = aux[i]
            i += 1
        elif aux[i]<aux[j]:
            list[k] = aux[i]
            i += 1
        else:
            list[k] = aux[j]
            j += 1    
   
   
    
def topdown_mergesort(list,low,high):
    '''
    a recursive mergesort implementation based on this abstract in- place 
    merge. It is one of the best-known examples of the utility of the 
    divide-and-conquer paradigm for efficient algorithm design. This recursive 
    code is the basis for an inductive proof that the algorithm sorts the 
    array: if it sorts the two subarrays, it sorts the whole array, by merging 
    together the subarrays
    
    top-down mergesort use at most 6NlgN array accesses
    
    Switching to insertion sort for small subarrays (length 15 or less)
    '''
    if high <= low:
        return
    
    mid = low + (high-low)//2
    
    topdown_mergesort(list,low,mid)
    topdown_mergesort(list,mid+1,high)
    
    # additional test to save time if left and right is already in order
    if list[mid] > list[mid+1]:
        merge(list,low,mid,high)            
            
    
 
def bottomup_mergesort(list):
    '''
    We start by doing a pass of 1-by-1 merges (considering individual items 
    as subarrays of size 1), then a pass of 2-by-2 merges (merge subarrays of 
    size 2 to make subarrays of size 4), then 4-by-4 merges, and so forth.
    '''
    n = len(list)
    size = 1
    while size < n:
        low = 0
        while low < n-size:
            merge(list,low,low+size-1,min(n-1,low+2*size-1))
            low += 2*size
        size = size*2




# connect them into 1 list
list4 = shell_sort(list3) + shell_sort(list2)

merge(list4,6,9,14)  
    
topdown_mergesort(list,0,len(list)-1)          
        
bottomup_mergesort(list)

    
#%% Quicksort
    
def partitioning(list,low,high):
    '''
    a method that makes sure the left of the partitioning point (the first 
    point after shuffling the original list) smaller than it and the right 
    larger than the point
    '''
    partition = list[low]
    i = low+1
    j = high
    
    while i<j:
        
        while list[i] <= partition and i < high:
            i += 1
            
        while list[j] >= partition and j > low:
            j -= 1
        # be very cafeful not forget to test i<j     
        if i < j:
            list[i], list[j] = list[j], list[i]
               
    list[low], list[j] = list[j], list[low]
    
    return j



def quicksort(list,low,high):
    '''
    do partitioning recursively
    Quicksort uses ~ 2NlnN compares (and one-sixth that many exchanges) 
    on the average to sort an array of length N with distinct keys.
    '''
    if low < high:
        j = partitioning(list,low,high)
        quicksort(list,low,j-1) # be careful here is j-1
        quicksort(list,j+1,high)



#partitioning(list5,0,9)        
    
quicksort(list,0,len(list)-1)
    
    
    
#%% Priority Queues & Heapsort   
    
class SimplePriorityQueue(object):
    '''
    simple priority queue
    insert without order
    delete max
    '''
    def __init__(self):
        self.queue = []
        
    def __str__(self): 
        return ' '.join([str(i) for i in self.queue])
    
    def isempty(self):
        return len(self.queue) == 0
    
    def insert(self,x):
        self.queue.append(x)
        
    def delete(self):
        if not self.isempty():
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max]:
                    max = i
            deleted = self.queue[max]
            del self.queue[max]
            return deleted
        else:
            return ('empty queue')

    
myQueue = SimplePriorityQueue() 
myQueue.insert(12) 
myQueue.insert(1) 
myQueue.insert(14) 
myQueue.insert(7) 
print(myQueue)             
while not myQueue.isempty(): 
    print(myQueue.delete())                   
myQueue.delete()


###########################################################################

def swim(list,n):
    '''
    make the nth element swim up to correct node if it's larger than its 
    parent.
    binary heap that the index represent node already, no need for explicit 
    link.
    ignore the first position 0
    '''
    while n > 1 and list[n] > list[n//2]:
        list[n], list[n//2] = list[n//2], list[n]
        n = n//2
 

       
list6 = [[],10,9,8,7,6,5,11]     
swim(list6,7)     
        
        
def sink(list,k,n):
    '''
    opposite to swim, remove down the element to correct place 
    child is 2n or 2n + 1
    '''
    while 2*k <= n:
        j = 2*k
        if j<n and list[j] < list[j+1]:
            j += 1
        if list[k] < list[j]:
            list[k], list[j] = list[j], list[k]
            k = j
        else:
            return


list6 = [[],10,1,8,7,6,5,4,3,2]     
sink(list6,2,9)   



class HeapPriorityQueue(object):
    '''
    max oriented
    delete max
    ignore first item
    '''
    def __init__(self):
        self.queue = []  
        
    def __str__(self): 
        return ' '.join([str(i) for i in self.queue])
        
    def isempty(self):
        return len(self.queue) == 0
    
    def insert(self,x):
        '''
        no more than 1 + lg N compares 
        '''
        self.queue.append(x)
        swim(self.queue,len(self.queue)-1)
        
    def delete(self):
        '''
        at most 2lgN compares
        '''
        if len(self.queue) >= 2:
            n = len(self.queue) - 1
            deleted = self.queue[1]
            self.queue[1], self.queue[n] = self.queue[n], self.queue[1]
            del self.queue[n]
            sink(self.queue,1,n-1)
            return deleted
        elif len(self.queue) == 1:
            deleted = self.queue[0]
            del self.queue[0]
            return deleted
        else:
            return('empty queue')
            
            
myQueue = HeapPriorityQueue()
myQueue.insert([]) 
myQueue.insert(8) 
myQueue.insert(4) 
myQueue.insert(9) 
myQueue.insert(6)
myQueue.insert(7)
myQueue.insert(5)
myQueue.insert(10) 
print(myQueue)             
while not myQueue.isempty(): 
    print(myQueue.delete())                   
myQueue.delete()



def heapsort(list):
    '''
    Heapsort breaks into two phases: heap construction, where we reorganize 
    the original array into a heap, and the sortdown, where we pull the items 
    out of the heap in decreasing order to build the sorted result.
    Sink-based heap construction uses fewer than 2N compares and fewer than N 
    exchanges to construct a heap from N items
    
    this sort ignores first item
    '''
    n = len(list) - 1
    k = n//2 # heapify start from the second last level
    
    # heapify the array
    # we do not use swim (insert) because sink can start from half way
    while k >= 1:
        sink(list,k,n)
        k -= 1
    
    # take the largest value and heapify the rest by sink
    while n > 1:
        list[1], list[n] = list[n], list[1]
        n -= 1
        sink(list,1,n)
        
        
heapsort(list)
    
    
    
