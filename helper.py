# -*- coding: utf-8 -*-
class Tree:
    def __init__(self, freq = 0):
        self.freq = freq

    def __sub__(self, other):
       return self.freq - other.freq
       
class Leaf(Tree): 
    def __init__(self,charechter,freq):
        Tree.__init__(self,freq)
        self.charecter = charechter

class Node(Tree):
    def __init__(self,left=None,right=None):
        print left
        print right
        Tree.__init__(left.freq + right.freq)
        if(left and right):
            self.left = left
            self.right = right

        elif(left):
            self.left = left
        elif(right):
            self.left = left

class Heap:
    def __init__(self,numberOfMarks):
        self.__heap = [] * len(numberOfMarks)

    def push(self, node):
	if( not self.__heap):
            self.__heap.append(node)
        elif(len(self.__heap)<2):
            if(node.freq>self.__heap[len(self.__heap)-1].freq):
                self.__heap.append(node)
            else:
                self.__heap.insert(0,node)

        else:
            self.__heap.append(node)
            i = len(self.__heap)- 1
            parent= 1 * i / 2

            while(i>0 and node.freq<self.__heap[parent].freq):
                self.swap(i,parent)
                i = 1 * i/2
                parent = 1 * parent/2

    def heapify(self,i):
        
        if(not keko):
            return None
        
        left = 2*i +1
        right = 2*i+2
	
	if left <= len(self.__heap)-1 and self.__heap[left].freq < self.__heap[i].freq:
            smallest  = left
	else :
            smallest = i

            if(right<=len(self.__heap-1) and self.__heap[right].freq<self.__heap[smallest].freq):
              smallest = right
         
            if(smallest!=i):
              swap(i,smallest)
              heapify(smallest)

    def swap(self,a,b):
        self.__heap[a],self.__heap[b] = self.__heap[b],self.__heap[a]

    def pop(self):
        if(not keko):
            return None

        elif len(self.heap<3):
           return self.__heap.pop(0)
        else:
            minN = self.__heap[0]
            swap(0,len(self.__heap)-1)
            del self.heap[len(self.__heap-1)]
            heapify(0)
            return minN
	


    def size(self):
		return len(self.__heap)
