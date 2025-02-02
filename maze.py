import sys

class Node():
    def __init__ (self,state,parent):
        self.state = state
        self.parent = parent

class StackFrontier():
    def __init__(self):
        self.nodeList = []

    def add(self,node):
        self.nodeList.append(node)
        
    def remove(self):
        node = self.nodeList[-1]
        del self.nodeList[-1]
        return node

    def empty(self):
        if len(self.nodeList) == 0:
            return True
        else:
            return False  

    def checkForState(self,state):
        for i in self.nodeList:
            if i.state == state:
                return True
                 
        return False
class Maze():
    
    def __init__(self,fileName):
        
        with open(fileName,'r') as f:
            self.maze1 = f.read()
            maze = self.maze1.splitlines()
            # print(maze)

            self.height = len(maze)
            self.width = len(maze[0])

            self.walls = []
            for i in range(self.height):
                rawWall = []
                for j in range(self.width):
                    
                    if maze[i][j] == 'A':
                        self.startPoint = (i,j)
                        
                        rawWall.append(False)
                    elif maze[i][j] == 'B':
                        self.goal = (i,j)
                        
                        rawWall.append(False)
                    elif maze[i][j] == ' ':
                        rawWall.append(False)
                    else:
                        rawWall.append(True)
                self.walls.append(rawWall)

              
    def neighbors(self,state):
        (raw,colum) = state

        possibleActions = [
            ("up",raw-1,colum),
            ("down",raw+1,colum),
            ("left",raw,colum-1),
            ("right",raw,colum+1)
        ]

        actionsList = []
        for action,r,c in possibleActions:
            if (0<= r <self.height) and (0<= c <self.width):
                if not self.walls[r][c]:
                    actionsList.append((r,c))
        return actionsList

    def solve(self):
        
        visitedNodes = []
        frontier = StackFrontier()    
        startPoint = Node(self.startPoint,None)
        frontier.add(node=startPoint)

        while True:
            if frontier.empty():
                return 
            
            nodeRemoveFromFrontier = frontier.remove()
            visitedNodes.append(nodeRemoveFromFrontier.state)

            possibleActions = self.neighbors(nodeRemoveFromFrontier.state)

            for i in possibleActions:
                # print("first" ,i)
                # print("visited nodes",frontier.checkForState(i))
                if i not in visitedNodes and (not frontier.checkForState(i)):
                    # print("I are",i)
                    if (i == self.goal):
                        # print("goal is",self.goal)
                        print("Here is the maze")
                        self.print(nodeRemoveFromFrontier,0)
                        print("Starting Point",self.startPoint)
                        print("Goal",self.goal,)
                        print("Here is the path")
                        self.print(nodeRemoveFromFrontier,1)
                        return
                    newNode = Node(i,nodeRemoveFromFrontier)  #given the node as the parent
                    frontier.add(newNode)

    def print(self,node,var):
        # print(self.maze1)
        # print(node.state)

        path = []
        path.append(node.state)
        parent = node.parent
        while parent != None:
            path.append(parent.state)
            parent = parent.parent

        # print(path)    

        maze2 = self.maze1.splitlines()
        c = -1
        r = -1
        for i in maze2:
            c += 1

            for j in i:
                r += 1
                # print(c,r)
                if j == '#':
                    print("█", end="")
                elif j=='A':
                    print("A",end="")    
                elif j=='B':
                    print("B",end="")
                elif j==" " and (c,r) in path and var==1:
                    print("*",end="")

                else:
                    print(" ",end="")  
            print("",sep="/n")
            r = -1                  

        
        
m = Maze(sys.argv[1]) #take the system inputs
m.solve()      