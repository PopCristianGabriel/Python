class create_repository():
    def __init__(self):
        self.objectList = []
        
    def get_obects(self):
        return self.objectList
    
    
    def add_object(self,object):
        self.objectList.append(object)
        
    def remove_ship(self,ship2):
        i = 0 
        while(i < len(self.objectList)):
            if(ship2.is_the_same(self.objectList[i]) == True):
                del self.objectList[i]
                return 
            else:
                i += 1
        
