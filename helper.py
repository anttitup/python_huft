
class Leaf(Tree) 
    def __init__(self,charechter,freq):
        Tree.__init__(freq)
        self.charecter = charechter
        Tree.__init__(freq)

class Node(Tree)
    def __init__(self,left=None,right=None):

        if(left and right):
            self.left = left
            self.right = right
            Tree.__init__(left.freq+right.freq)

        else if(left):
            self.left = left
            Tree.__init__(left.freq)
        else if(right)
            self.left = left
            Tree.__init__(left.freq)

class Tree
    def __init__(self,freq = 0):
        self.freq = freq

    def __sub__(self,other):
       return self.freq - other.freq



class Heap
    
    def __init__(self,numberOfMarks):
        self.heap = [0] * len(numberOfMarks)

    def push(self, node):
        if(!self.heap):
            heap.append(node)
        else if(len(self.heap)<2):
            if(node.freq>heap[len(heap)-1].freq):
                heap.append(node)
            else:
                heap.insert(0,node)

            else:
                heap.append(node)
                i = len(heap)-1
                parent=1 * i/2

                while(i>0 and node.freq<heap[parent].freq):
                    swap(i,parent)
                    i = 1 * i/2
                    parent = 1 * parent/2

    def heapify(i)
        if(!keko):
            return None
        left = 2*i +1
        right = 2*i+2

        if(left <= len(self.heap)-1 and self.heap[left].freq < self.heap[i].freq:
            smallest  = left
         else :
            smallest = i

         if(right<=len(self.heap-1) and self.heap[right].freq<self.heap[smallest].freq):
         smallest = right
         if(smallest!=i):
            swap(i,smallest)
            heapify(smallest)

    def swap(self,a,b):
        helpNode =self.heap[a]
        self.heap[a] = self.heap[b]
        self.heap[b] = a

     def pop:
        if(!keko):
            return None

        else if(len(self.heap<3):
           return self.heap.pop(0)
        else:
            minN = self.heap[0]
            swap(0,len(self.heap)-1)
            del self.heap[len(self.heap-1)]
            heapify(0)
            return minN
            



