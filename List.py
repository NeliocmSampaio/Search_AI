

class List:
    def __init__(self):
        self.elements   = 0
        self.list       = []

    def insertPriority(self, element, key):
        e = (element, key)

        if self.elements == 0:
            self.list.append(e)
            self.elements += 1
            return

        for i in range( len( self.list ) ):
            if self.list[i][1] > key:
                self.list.insert( i, e )
                self.elements += 1
                return
        
        self.list.append(e)
        self.elements += 1

    def popL( self ):
        if self.elements==0:
            return None
        self.elements -= 1
        return (self.list).pop(0)

    def insertGreater(self, element, key):
        e = (element, key)

        if self.elements == 0:
            self.list.append(e)
            self.elements += 1
            return

        for i in range( len( self.list ) ):
            if self.list[i][1] < key:
                self.list.insert( i, e )
                self.elements += 1
                return
        
        self.list.append(e)
        self.elements += 1

    def enqueue(self, element ):
        self.elements += 1
        self.list.append( element )

    def pushB( self, element ):
        self.elements += 1
        self.list.insert( 0, element )

'''
l = List()
l.pushB(2)
l.pushB(3)
l.pushB(8)
l.pushB(7)
print(l.list)
print( l.popL() )
print( l.popL() )
print( l.popL() )
print( l.popL() )
'''