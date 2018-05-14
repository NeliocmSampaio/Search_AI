import sys

x = int( sys.argv[1] )
y = int( sys.argv[2] )
inicial = ( x, y )

x = int( sys.argv[3] )
y = int( sys.argv[4] )
final = ( x, y )

print(inicial)
print(final)

'''
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
'''