import sys

from List import *
from Map import *

#Nome do arquivo
fileName = sys.argv[1]

map = readMap( fileName )

#Pontos inicial e final
x = int( sys.argv[2] )
y = int( sys.argv[3] )
inicial = ( x*map.mapWidth+y )

x = int( sys.argv[4] )
y = int( sys.argv[5] )
final = ( x*map.mapWidth+y )

custo, path = map.ids(inicial, final)
#print(custo)
if custo != -1:
	#print( path.list )
	imprimeCaminho( path.list, map.mapWidth, map.mapHeight)
	#map.printPath( path )