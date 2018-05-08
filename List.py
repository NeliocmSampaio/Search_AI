

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

    def pushL(self, element ):
        self.list.append( element )