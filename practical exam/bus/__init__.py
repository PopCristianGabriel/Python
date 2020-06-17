import unittest
class create_buss:
    def __init__(self,bussId,bussRoute,bussModel,bussTimes):
        self.bussId = bussId
        self.bussRoute = bussRoute
        self.bussModel = bussModel
        self.bussTimes = bussTimes
        
        
    def get_buss_id(self):
        return int(self.bussId)
    def get_buss_route(self):
        return self.bussRoute
    def get_buss_model(self):
        return self.bussModel
    def get_buss_times(self):
        return int(self.bussTimes)
    
    
    """
    function that prints a buss
    """
    def list(self):
        print(self.get_buss_id(), " ",self.get_buss_route().get_route_code()," ",self.bussModel," ",self.bussTimes)
        

