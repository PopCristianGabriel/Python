class create_route:
    def __init__(self,routeCode,routeLen):
        self.routeCode = routeCode
        self.routeLen = routeLen
        
    def get_route_code(self):
        return int(self.routeCode)
    
    def get_route_len(self):
        return int(self.routeLen)