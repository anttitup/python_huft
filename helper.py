
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
        
        heap =  * len(numberOfMarks)
