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
    def __init__(self, lines, columns, mapType, name, map):
        self.graph      = Graph( lines*columns )
        self.mapHeight  = lines
        self.mapWidth  = columns
        self.mapType    = mapType
        self.name       = name
        self.map        = map

    def printMap(self):
        for i in range(self.mapHeight):
            for j in range(self.mapWidth):
                if self.map[i][j] == 1:
                    print("@", end="")
                else:
                    print( " ", end="" )
            print()
    
    def printSpec(self):
        print("\nDados do Mapa:")
        print("Type: ", self.mapType)
        print("Height: ", self.mapHeight)
        print("Width: ", self.mapWidth)
        print("Name: ", self.name)

    def dfsMap(self, visited, cel):

        x = cel[0]  #Linha
        y = cel[1]  #Coluna
        print(" ", (x*self.mapWidth) + y, " ", end="" )
        aux = input()
        '''
            Células de cima, de baixo, esquerda e direita
        '''
        # UP
        #Célula não possui obstáculo e não foi visitada
        if self.map[x-1][y]==0:
            if  visited[x-1][y]==0:
                visited[x-1][y] = 1
                self.dfsMap(visited, (x-1, y))

        # DOWN
        #Célula não possui obstáculo e não foi visitada
        if self.map[x+1][y]==0:
            if visited[x+1][y]==0:
                visited[x+1][y] = 1
                self.dfsMap(visited, (x+1, y))

        # LEFT
        #Célula não possui obstáculo e não foi visitada
        if self.map[x][y-1]==0:
            if visited[x][y-1]==0:
                visited[x][y-1] = 1
                self.dfsMap(visited, (x, y-1))

        # RIGHT
        #Célula não possui obstáculo e não foi visitada
        if self.map[x][y+1]==0:
            if visited[x][y+1]==0:
                visited[x][y+1] = 1
                self.dfsMap(visited, (x, y+1))

        '''
            Células das diagonais, cima-esquerda, cima-direita, baixo-direita 
            e baixo esquerda
        '''
        # UP-LEFT
        #Célula não possui obstáculo e não foi visitada
        if self.map[x-1][y-1]==0:
            if visited[x-1][y-1]==0:
                visited[x-1][y-1] = 1
                self.dfsMap(visited, (x-1, y-1))

        # UP-RIGHT
        #Célula não possui obstáculo e não foi visitada
        if self.map[x-1][y+1]==0:
            if visited[x-1][y+1]==0:
                visited[x-1][y+1] = 1
                self.dfsMap(visited, (x-1, y+1))

        # DOWN-RIGHT
        #Célula não possui obstáculo e não foi visitada
        if self.map[x+1][y+1]==0:
            if visited[x+1][y+1]==0:
                visited[x+1][y+1] = 1
                self.dfsMap(visited, (x+1, y+1))

        # DOWN-LEFT
        #Célula não possui obstáculo e não foi visitada
        if self.map[x+1][y-1]==0:
            if visited[x+1][y-1]==0:
                visited[x+1][y-1] = 1
                self.dfsMap(visited, (x+1, y-1))

    def readGraph(self):
        m = [ [ 0 for j in range(self.mapWidth) ] for i in range(self.mapHeight) ]

        for i in range(self.mapHeight):
            for j in range(self.mapWidth):
                print("i, j, map[i][j]: ", i, j, self.map[i][j] )
                if(self.map[i][j] == 0):
                    if(m[i][j]==0):
                        m[i][j] = 1
                        self.dfsMap( m, (i, j) )

def readMap(file, map):
    f = open(file, 'r')
    lines = f.readlines()

    mapType     = ( str( lines[0] ).split(' ')[1] ).split('\n')[0]
    mapHeight   = int ( str( lines[1] ).split(' ')[1] )
    mapWidth    = int ( str( lines[2] ).split(' ')[1] )
    mapName     = ( str( lines[3] ).split(' ')[1] ).split('\n')[0]

    m = [ [ [] for j in range(mapWidth) ] for i in range(mapHeight) ]

    for i, l in enumerate( lines[4:] ):
        for j, e in enumerate(l):
            if i<mapHeight and j<mapWidth:
                if(e=='@'):
                    m[i][j] = 1
                    #m[index].append(1)
                else:
                    m[i][j] = 0
                    #m[index].append(0)

    map = Map( mapHeight, mapWidth, mapType, mapName, m )
    map.printMap()

    map.readGraph()

    map.printSpec()

readMap(sys.argv[1], map)