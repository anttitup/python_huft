

def openAndCount(name):
    numberOfCharechters = [0]*256
    with open(name,r) as mainFile:
        while(i):
            mark = mainFile.read()
            if(not mark): break
            numberOfCharechters[mark]=+1
   
   numberOfCharecters[255]=+1 #eof
   return numberOfCharecters

def generateTree(numberOfCharechters):
    heap = heap()
