from route import *
from bus import *

class create_repository():
    def __init__(self):
        self.objects = []
        
    def add_obj_to_repo(self,object):
        self.objects.append(object)
        
    def getElementById(self,id):
        for i in range(len(self.objects)):
            if(self.objects[i].get_route_code == id):
                return i
        return -1