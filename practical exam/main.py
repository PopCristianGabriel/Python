from aux import *




def run():
    
    bussRepo = create_repository()
    routeRepo = create_repository()
    readBussRoutes(routeRepo)
    readBusses(routeRepo,bussRepo)
    
    
    while(True):
        userInput = input("give me a command:")
        if(userInput == '1'):
            routeCode = input("enter a route code:")
            for buss in bussRepo.objects:
                if(buss.get_buss_route().get_route_code() == int(routeCode)):
                    buss.list()
        if(userInput == "2"):
            for route in routeRepo.objects:
                print(route.get_route_code(), " ",route.get_route_len())
                
        if(userInput == "3"):
            bussId = int(input("enter a buss id:"))
            for buss in bussRepo.objects:
                if(buss.get_buss_id() == bussId):
                    print(buss.get_buss_times() * buss.get_buss_route().get_route_len())
                    buss.list()
                
            
        
run()