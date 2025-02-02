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
        del self.nodeList[-1]

    def empty(self):
        if len(self.nodeList) == 0:
            return True
        else:
            return False  


class Maze():
    
    def __init__(self,fileName):
        
        with open(fileName,'r') as f:
            maze = f.read()
            maze = maze.splitlines()
            print(maze)

            height = len(maze)
            width = len(maze[0])

            walls = []
            for i in range(height):
                rawWall = []
                for j in range(width):
                    
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
                walls.append(rawWall)

            frontier = StackFrontier()    
            startPoint = Node(self.startPoint,None)
            frontier.add(node=startPoint)    
          
              
        
m = Maze(sys.argv[1])        