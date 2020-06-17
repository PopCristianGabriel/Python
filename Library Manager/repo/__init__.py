from _tracemalloc import start
class create_repository():
    def __init__(self):
        self.objectList = []
        
    
    def add_object_to_list(self,object):
        self.objectList.append(object)
    
    def remove_object_by_index(self,index):
        del self.objectList[index]
        
    def update_an_object_by_index(self,index,newobject):
        self.objectList[index] = newobject
    
    
    def find_a_client_by_name(self,searchedName,start):
        i = start
        while(i < len(self.objectList)):
            if(searchedName in  self.objectList[i].client_get_name()):
                return i
            else:
                i+=1
        return -1
    
    
    def find_an_object_by_id(self,searchedId,start):
        i = start
        while(i < len(self.objectList)):
            if(self.objectList[i].get_id_function() == searchedId):
                return i
            i += 1
        return -1
    
    def find_an_object_by_name(self,searchedName,start):
        i = start
        while(i < len(self.objectList)):
            if(self.objectList[i].get_name() == searchedName):
                return i
            i += 1
        return -1
    
    def find_an_object_by_author(self,searchedAuthor,start):
        i = start
        while(i < len(self.objectList)):
            if(self.objectList[i].book_get_author().find(searchedAuthor) != -1):
                return i
            i += 1
        return -1
    
    def find_an_object_by_description(self,searchedDescription,start):
        i = start
        while(i < len(self.objectList)):
            if(self.objectList[i].book_get_description().find(searchedDescription)!= -1):
                return i
            i += 1
        return -1    

    def find_an_object_by_title(self,searchedTitle,start):
        i = start
        while(i < len(self.objectList)):
            if(self.objectList[i].book_get_title().find(searchedTitle) != -1):
                return i
            i += 1
        return -1    