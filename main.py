# -*- coding: utf-8 -*-
from helper import *

def openAndCount(name):
    numberOfCharechters = [0]*256
    with open(name,"r") as mainFile:
        while(mark):
            mark = mainFile.read()
            if(not mark): 
		break
            else: 
		numberOfCharechters[mark]=+1
	numberOfCharecters[255]=+1 #eof
	return numberOfCharecters

def generateTree(numberOfCharechters):
	heap = Heap()
	for i in range(len(numberOfCharechters)):
		if i!=0:
			leaf = Leaf(i,numberOfCharechters[i])
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
	
	for char in range(table):
		if node !=0:
			encFile.write(char+" "+table[char])
		
	for char in mainFile.read(1):
		writeInBits(encFile,table[char])
	
	writeInBits(encFile,table[255])

num = openAndCount("test.txt")		
heap = generateTree(num)
tree = makeOneTree(heap)	
table=makePrefix(tree,prefix=[])	
writeEncode("test.txt",table,tree,len(table))
