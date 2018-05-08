import sys
from List import *

class Graph:
    def __init__(self, v):
        self.v = v
        self.adj = [  ]
        for i in range(v):
            self.adj.append([])

    def add(self, a, b, p):
        self.adj[a].append( (b, p) )

    def print(self):
        for index, l in enumerate(self.adj):
            print(index, ": ", end="")
            for i in l:
                print (i, " ", end="")
            print()

    def idfs( self, start, destiny ):
        visitados = [ 0 for i in range(self.v) ]
        openList = List()
        closedList = List()

        #Empilhando o vértice inicial e o custo até ele (0)
        openList.pushB( [start, 0] )

        while openList.elements > 0:
            u = openList.popL()

            if u[0] == destiny:
                return u[1]

            for i in self.adj[ u[0] ]:
                if(visitados[i]==0):
                    visitados[ i[0] ] = 1
                    # u[1]: Custo empilhado até vértice u[0].
                    # i[1]: Custo do vértice u[0] para i[0]
                    openList.pushB( [i, u[1]+i[1] ] )

    def vldfs(self, u, destiny, visitados, custo, l ):
        visitados[u] = 1

        if u==destiny:
            return custo
        if l==0:
            visitados[u] = 0
            return -1

        for i in self.adj[u]:
            if visitados[i[0]]==0:
                r = self.vldfs(i[0], destiny, visitados, custo+i[1], l-1 )

                if r!=-1:
                    return r

        visitados[u] = 0
        return -1

    def ldfs(self, start, destiny, l):
        visitados = [ 0 for i in range(self.v) ]

        return self.vldfs( start, destiny, visitados, 0, l )

    def IDS( self, start, destiny ):
        i=0
        r = -1
        while True:
            r = self.ldfs( start, destiny, i )
            print("called l= ", i, ", r= ", r)
            if r != -1:
                print( "custo= ", r )
                return True
            i+=1

class Map:
    def __init__(self, lines, columns, mapType, name, map):
        self.graph      = Graph( lines*columns )
        self.mapHeight  = lines
        self.mapWidth   = columns
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
    
    def printGraph(self):
        self.graph.print()
    
    def printSpec(self):
        print("\nDados do Mapa:")
        print("Type: ", self.mapType)
        print("Height: ", self.mapHeight)
        print("Width: ", self.mapWidth)
        print("Name: ", self.name)

    def mapping(self, cel):

        x = cel[0]  #Linha
        y = cel[1]  #Coluna
        #print(" ", (x*self.mapWidth) + y, " ", end="" )
        #aux = input()

        '''
            Células de cima, de baixo, esquerda e direita
        '''
        # UP
        #Célula não possui obstáculo e não foi visitada
        if self.map[x-1][y]==0:
            self.graph.add( ( x*self.mapWidth)+y , ((x-1)*self.mapWidth)+y, 1 )

        # DOWN
        #Célula não possui obstáculo e não foi visitada
        if self.map[x+1][y]==0:
            self.graph.add( ( x*self.mapWidth)+y , ((x+1)*self.mapWidth)+y, 1 )

        # LEFT
        #Célula não possui obstáculo e não foi visitada
        if self.map[x][y-1]==0:
            self.graph.add( ( x*self.mapWidth)+y , ((x)*self.mapWidth)+(y-1), 1 )

        # RIGHT
        #Célula não possui obstáculo e não foi visitada
        if self.map[x][y+1]==0:
            self.graph.add( ( x*self.mapWidth)+y , ((x)*self.mapWidth)+(y+1), 1 )

        '''
            Células das diagonais, cima-esquerda, cima-direita, baixo-direita 
            e baixo esquerda
        '''
        # UP-LEFT
        #Célula não possui obstáculo e não foi visitada
        if self.map[x-1][y-1]==0 and self.map[x-1][y]==0 and self.map[x][y-1]==0:
            self.graph.add( ( x*self.mapWidth)+y , ((x-1)*self.mapWidth)+(y-1), 1.5 )

        # UP-RIGHT
        #Célula não possui obstáculo e não foi visitada
        if self.map[x-1][y+1]==0 and self.map[x-1][y]==0 and self.map[x][y+1]==0:
            self.graph.add( ( x*self.mapWidth)+y , ((x-1)*self.mapWidth)+(y+1), 1.5 )

        # DOWN-RIGHT
        #Célula não possui obstáculo e não foi visitada
        if self.map[x+1][y+1]==0 and self.map[x+1][y]==0 and self.map[x][y+1]==0:
            self.graph.add( ( x*self.mapWidth)+y , ((x+1)*self.mapWidth)+(y+1), 1.5 )

        # DOWN-LEFT
        #Célula não possui obstáculo e não foi visitada
        if self.map[x+1][y-1]==0 and self.map[x+1][y]==0 and self.map[x][y-1]==0:
            self.graph.add( ( x*self.mapWidth)+y , ((x+1)*self.mapWidth)+(y-1), 1.5 )


    def readGraph(self):
        m = [ [ 0 for j in range(self.mapWidth) ] for i in range(self.mapHeight) ]

        for i in range(self.mapHeight):
            for j in range(self.mapWidth):
                #print("i, j, map[i][j]: ", i, j, self.map[i][j] )
                if(self.map[i][j] == 0):
                    if(m[i][j]==0):
                        m[i][j] = 1
                        self.mapping( (i, j) )

        #self.graph.print()

    def ids(self, start, destiny ):
        self.graph.IDS(start, destiny )

def readMap(file):
    f = open(file, 'r')
    lines = f.readlines()

    mapType     = ( str( lines[0] ).split(' ')[1] ).split('\n')[0]
    mapHeight   = int ( str( lines[1] ).split(' ')[1] )
    mapWidth    = int ( str( lines[2] ).split(' ')[1] )
    mapName     = ( str( lines[3] ) ).split('\n')[0]

    m = [ [ [] for j in range(mapWidth) ] for i in range(mapHeight) ]

    for i, l in enumerate( lines[4:] ):
        for j, e in enumerate(l):
            if i<mapHeight and j<mapWidth:
                if(e=='@'):
                    m[i][j] = 1
                else:
                    m[i][j] = 0

    map = Map( mapHeight, mapWidth, mapType, mapName, m )
    map.readGraph()

    return map

'''
map = readMap(sys.argv[1])
map.printSpec()
map.printMap()
map.printGraph()
'''