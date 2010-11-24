from help.py import *

def openAndCount(name):
    numberOfCharechters = [0]*256
    with open(name,r) as mainFile:
        while(i):
            mark = mainFile.read()
            if(not mark): 
				break
            else: 
				numberOfCharechters[mark]=+1
   
   numberOfCharecters[255]=+1 #eof
   return numberOfCharecters

def generateTree(numberOfCharechters):
    heap = Heap()
	for(char,node in range(numberOfCharecters) if node!=0):
		leaf = Leaf(index,freq)
		heap.push(leaf)
	return heap

def makeOneTree(heap):
	if(heap.size==1):
		return heap.pop
	else:
		while(heap.size>1):
			a = heap.pop
			b = heap.pop
			heap.push(Node(a,b))
		return heap.pop

def makePrefix(tree,prefix,table=[]*256):
	if(puu is Leaf):
		taulu[puu.charechter]=prefix
	else:
		makeprefix(tree.left,prefix+"0",table)
		makeprefix(tree.right,prefix+"1",table)
	return table

def writeEncode(filename,table,tree,heapSize):
	mainFile=open(fileName,"r")
	encFile= open(fileName+".enc","w+")
	
	encFile.write(heapSize)
	
	for(char,freq in range(table) if node !=0):
		encFile.write(char+" "+freq)
		
	for(char in mainFile.read(1)):
		writeInBits(encFile,table[char])
	
	writeInBits(encFile,table[255])

		
	
	
