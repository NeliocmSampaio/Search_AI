import sys
from Map import *

map = readMap(sys.argv[1])
map.printSpec()
map.printMap()
map.dfs(0, 62730)