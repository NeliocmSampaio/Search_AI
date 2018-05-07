

class Queue:
    def __init__(self):
        self.elements   = 0
        self.list       = []

    def insertPriority(self, element, key):
        e = (element, key)

        if self.elements == 0:
            self.list.append(e)
            self.elements += 1
            return

        #print("for")
        for i in range( len( self.list ) ):
            #print("comparing: ", key, self.list[i][1])
            if self.list[i][1] > key:
                self.list.insert( i, e )
                self.elements += 1
                return
        
        self.list.append(e)
        self.elements += 1

    def insertGreater(self, element, key):
        e = (element, key)

        if self.elements == 0:
            self.list.append(e)
            self.elements += 1
            return

        #print("for")
        for i in range( len( self.list ) ):
            #print("comparing: ", key, self.list[i][1])
            if self.list[i][1] < key:
                self.list.insert( i, e )
                self.elements += 1
                return
        
        self.list.append(e)
        self.elements += 1