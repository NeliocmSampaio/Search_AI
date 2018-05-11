def vldfs( self, u, destiny, visitados, custo, l ):
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

from PIL import Image
import numpy as np

array = np.zeros([255, 255, 3], dtype=np.uint8)
array[:,:] = [255, 128, 0]
image = Image.fromarray( array, 'RGB' )
image.save("teste.png")