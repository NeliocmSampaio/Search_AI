import sys

class Graph:
    def __init__(self, v):
        self.v = v
        self.adj = [  ]
        for i in range(v):
            self.adj.append([])

    def add(self, a, b):
        self.adj[a].append(b)

    def print(self):
        for index, l in enumerate(self.adj):
            print(index, ": ", end="")
            for i in l:
                print (i, " ", end="")
            print()

class Map:
    def __init__(self, lines, columns):
        self.graph = Graph( lines*columns )

def readMap(file, map):
    f = open(file, 'r')
    lines = f.readlines()

    mapType     = ( str( lines[0] ).split(' ')[1] ).split('\n')[0]
    mapHeight   = int ( str( lines[1] ).split(' ')[1] )
    mapWidth    = int ( str( lines[2] ).split(' ')[1] )
    mapName     = ( str( lines[3] ).split(' ')[1] ).split('\n')[0]

    m = [ [] for i in range(mapHeight) ]

    for index, l in enumerate( lines[4:] ):
        for i in l:
            i.append()
            if(i=='@'):
                i = 1
            else:
                i = 0

    for l in lines[4:]:
        for i in l:
            if()

    print("\nespec:")
    print(mapType)
    print(mapHeight)
    print(mapWidth)
    print(mapName)

readMap(sys.argv[1], map)
print("\nOut")

G = Graph(5)

G.add(1, 2)
G.add(1, 3)
G.add(2, 4)
G.add(4, 3)

G.print()