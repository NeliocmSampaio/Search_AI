import sys

from List import *
from PIL import Image
import numpy as np


class Graph:
    def __init__(self, v, lines, collumns):
        self.v = v
        self.lines = lines
        self.collumns = collumns
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

    #DFS Iterativo
    def idfs( self, start, destiny, limit ):
        visitados   = [ 0 for i in range(self.v) ]
        parent      = [ -1 for i in range(self.v) ]
        level       = [ -1 for i in range(self.v) ]
        openList    = List()
        #closedList  = List()
        path        = List()
        minLevel = limit

        cost = -1

        lv = limit
        #Empilhando o vértice inicial e o custo até ele (0)
        visitados[start]    = 1
        level[start]        = 0
        openList.pushB( [start, 0, lv] )

        while openList.elements > 0:
            u = openList.popL()
            vertice = u[0]
            custo = u[1]
            lv = u[2]

            if(minLevel>lv):
                minLevel = lv

            if u[0] == destiny and (cost==-1 or cost >u[1]):
                path.list.clear()
                i = u[0]
                path.pushB( (i, custo) )
                while i!=start:
                    path.pushB( parent[i] )
                    i = parent[i][0]
                cost = u[1]

            if lv==0:
                continue

            for i in self.adj[ vertice ]:
                if level[i[0]]==-1 or level[i[0]]<lv:
                    visitados[ i[0] ] = 1
                    parent [i[0]] = (u[0], custo)
                    # u[1]: Custo empilhado até vértice u[0].
                    # i[1]: Custo do vértice u[0] para i[0]
                    # u[2]: level do nó u
                    level[i[0]] = lv-1
                    openList.pushB( [i[0], custo+i[1], lv-1 ] )
        
        if(cost==-1):
            return -1, None, minLevel
        else:
            return cost, path, minLevel

    # Busca de custo uniforme
    def bcu( self, start, destiny ):
        visitados   = [ 0 for i in range(self.v) ]
        parent      = [ -1 for i in range(self.v) ]
        level       = [ -1 for i in range(self.v) ]
        Custo       = [ 80000000000 for i in range(self.v) ]
        openList    = List()
        closedList  = List()
        path        = List()
        cost = -1

        #Empilhando o vértice inicial e o custo até ele (0)
        visitados[start]    = 1
        level[start]        = 0
        Custo[start]        = 0
        openList.insertPriority( [start, 0], 0 )

        while openList.elements > 0:
            
            u = openList.popL()
            vertice = u[0][0]
            custo = u[1]

            if u[0][0] == destiny:
                path.list.clear()
                i = u[0][0]

                path.pushB( (i, custo) )
                while i!=start:
                    path.pushB( (parent[i][0][0], custo) )
                    i = parent[i][0][0]
                return u[1], path, openList, closedList

            closedList.pushB( vertice )
            visitados [ vertice ] = 2

            for i in self.adj[ vertice ]: 
                if visitados[i[0]]== 1 and Custo[i[0]]>custo+i[1]:
                    Custo[i[0]] = custo+i[1]
                    openList.insertPriority( [i[0], custo+i[1] ], custo+i[1] )
                else:
                    if visitados[i[0]]==0:
                        visitados[ i[0] ] = 1
                        parent[i[0]] = (u[0], custo)
                        Custo[i[0]] = custo+i[1]
                        openList.insertPriority( [i[0], custo+i[1] ], custo+i[1] )

                    # u[1]: Custo empilhado até vértice u[0].
                    # i[1]: Custo do vértice u[0] para i[0]
                    # u[2]: level do nó u
        
        if(cost==-1):
            return -1, None, None, None
        else:
            return cost, path, openList, closedList

    # Busca gulosa
    def bfs( self, start, destiny ):
        visitados   = [ 0 for i in range(self.v) ]
        parent      = [ -1 for i in range(self.v) ]
        level       = [ -1 for i in range(self.v) ]
        Custo       = [ 80000000000 for i in range(self.v) ]
        openList    = List()
        closedList  = List()
        path        = List()
        cost = -1

        goalx = int (destiny/self.lines)
        goaly = int ( destiny - goalx*self.lines )

        #Empilhando o vértice inicial e o custo até ele (0)
        visitados[start]    = 1
        level[start]        = 0
        Custo[start]        = 0
        openList.insertPriority( [start, 0], 0 )

        while openList.elements > 0:
            
            u = openList.popL()
            vertice = u[0][0]
            custo = u[0][1]

            if u[0][0] == destiny:
                path.list.clear()
                i = u[0][0]

                path.pushB( (i, custo) )
                while i!=start:
                    path.pushB( (parent[i][0][0], custo) )
                    i = parent[i][0][0]
                return u[0][1], path, openList, closedList

            closedList.pushB( vertice )
            visitados [ vertice ] = 2

            for i in self.adj[ vertice ]: 

                x = int ( i[0] /self.lines)
                y = int ( i[0] - x*self.lines )

                dx = abs( x - goalx )
                dy = abs( y - goaly )

                h = dx + dy

                if visitados[i[0]]== 1 and Custo[i[0]]>custo+i[1]:
                    Custo[i[0]] = custo+i[1]
                    openList.insertPriority( [i[0], custo+i[1] ], h )
                else:
                    if visitados[i[0]]==0:
                        visitados[ i[0] ] = 1
                        parent[i[0]] = (u[0], custo)
                        Custo[i[0]] = custo+i[1]
                        openList.insertPriority( [i[0], custo+i[1] ], h )

                    # u[1]: Custo empilhado até vértice u[0].
                    # i[1]: Custo do vértice u[0] para i[0]
                    # u[2]: level do nó u
        
        if(cost==-1):
            return -1, None, None, None
        else:
            return cost, path, openList, closedList

# A-star
    def aStar( self, start, destiny, heuristica ):
        visitados   = [ 0 for i in range(self.v) ]
        parent      = [ -1 for i in range(self.v) ]
        level       = [ -1 for i in range(self.v) ]
        Custo       = [ 80000000000 for i in range(self.v) ]
        openList    = List()
        closedList  = List()
        path        = List()
        cost = -1

        print(start, destiny)

        goalx = int (destiny/self.lines)
        goaly = int ( destiny - goalx*self.lines )

        #Empilhando o vértice inicial e o custo até ele (0)
        visitados[start]    = 1
        level[start]        = 0
        Custo[start]        = 0
        openList.insertPriority( [start, 0], 0 )

        while openList.elements > 0:
            
            u = openList.popL()
            vertice = u[0][0]
            custo = u[0][1]

            if u[0][0] == destiny:
                path.list.clear()
                i = u[0][0]

                path.pushB( (i, custo) )
                while i!=start:
                    path.pushB( (parent[i][0][0], custo) )
                    i = parent[i][0][0]
                return u[0][1], path, openList, closedList

            closedList.pushB( vertice )
            visitados [ vertice ] = 2

            for i in self.adj[ vertice ]: 

                x = int ( i[0] /self.lines)
                y = int ( i[0] - x*self.lines )

                dx = abs( x - goalx )
                dy = abs( y - goaly )

                h = dx + dy

                if visitados[i[0]]== 1 and Custo[i[0]]>custo+i[1]:
                    Custo[i[0]] = custo+i[1]
                    openList.insertPriority( [i[0], custo+i[1] ], custo+i[1]+h )
                else:
                    if visitados[i[0]]==0:
                        visitados[ i[0] ] = 1
                        parent[i[0]] = (u[0], custo)
                        Custo[i[0]] = custo+i[1]
                        openList.insertPriority( [i[0], custo+i[1] ], custo+i[1]+h )

                    # u[1]: Custo empilhado até vértice u[0].
                    # i[1]: Custo do vértice u[0] para i[0]
                    # u[2]: level do nó u
        
        if(cost==-1):
            return -1, None, None, None
        else:
            return cost, path, openList, closedList

class Map:
    def __init__(self, lines, collumns, mapType, name, map):
        self.graph      = Graph( lines*collumns, lines, collumns )
        self.mapHeight  = lines
        self.mapWidth   = collumns
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

    def ids(self, start, destiny ):
        custo = -1
        i=0
        minLevel = -1
        while custo==-1:
            custo, path, minLevel = map.graph.idfs( src, dst, i )
            if(custo==-1 and minLevel!=0):
                break
            i+=1
        return custo, path

    def bcu(self, start, destiny ):
        custo, path, openl, closedl = map.graph.bcu( src, dst )
        return custo, path, openl, closedl

    def bfs(self, start, destiny ):
        custo, path, openl, closedl = map.graph.bfs( src, dst )
        return custo, path, openl, closedl

    def aStar(self, start, destiny, heuristica ):
        custo, path, openl, closedl = map.graph.aStar( src, dst, heuristica )
        return custo, path, openl, closedl

    def printPath(self, path):
        celulas = []

        for i in path.list:
            celulas.append( i[0] )

        for i in range(self.mapHeight):
            for j in range(self.mapWidth):
                if celulas.__contains__( (i*self.mapWidth)+j ):
                    print("*", end="")
                else: 
                    if self.map[i][j] == 1:
                        print("@", end="")
                    else:
                        print( " ", end="" )
            print()

def printRoute(map, path, openL, closedL):
    m = [ [ 0 for j in range(map.mapWidth) ] for i in range(map.mapHeight) ]
    array = np.zeros([map.mapHeight, map.mapWidth, 3], dtype=np.uint8)

    O = []  #open transcription
    C = []  #closed Transcription
    P = []

    for i in openL.list:
        O.append( i[0][0] )

    for i in closedL.list:
        C.append( i )

    for i in path.list:
        P.append(i[0])

    for i in range(map.mapHeight):
        for j in range(map.mapWidth):
            if P.__contains__((i*map.mapWidth)+j):
                        array[i,j] = [0,0,0]
            else:
                if O.__contains__( (i*map.mapWidth)+j ):
                        #print("*", end="")
                    #m[i][j] = 50 #[50, 50, 50]
                    array[i, j] = [123,104,238]
                else:
                    if C.__contains__( (i*map.mapWidth)+j ):
                        #m[i][j] = [100, 100, 100, 100]
                        array[i, j] = [135,206,250]
                    else:
                        if map.map[i][j] == 1:
                            #m[i][j] = [150, 150, 150, 150]
                            array[i, j] = [105,105,105]
                        else:
                            #m[i][j] = [200, 200, 200]
                            array[i, j] = [220,220,220]
    
    #array = np.zeros([255, 255, 3], dtype=np.uint8)
    #array[:,:] = [255, 128, 0]

    #im = np.array( m )
    #t = np.array ( [ [ [255, 255, 255, 255] for j in range(255) ] for i in range(255) ] )
    img = Image.fromarray(array, 'RGB')
    img.show()
    img.save('imagem2.png')
'''
    for i in range(map.mapHeight):
        for j in range(map.mapWidth):
            print(m[i][j], " ", end='')
        print()
'''

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

map = readMap(sys.argv[1])
x = int( sys.argv[2] )
y = int( sys.argv[3] )
src = x*map.mapWidth+y
x = int( sys.argv[4] )
y = int( sys.argv[5] )
dst = x*map.mapWidth+y

custo, path, o, c = map.aStar(src, dst, 1)
print(custo)
if custo != -1:
    printRoute(map, path, o, c)
    #print(path.list)
    #map.printPath(path)
