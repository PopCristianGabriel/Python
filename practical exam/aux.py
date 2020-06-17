from repo import *
from bus import *

"""
a function that finds the index of a route in a repository
"""
def findRoute(routeRepo,route):
     for i in range(len(routeRepo.objects)):
            if(int(routeRepo.objects[i].routeCode) == route):
                return i
     return -1

'''
a function that given a route repository, it reads from a file the given routes and appends them into the repository
'''
def readBussRoutes(routeRepo):
    f = open("busRoutesFile","r")
    line = f.readline()  #read a line
    while(len(line) != 0):
        line = line.split(",")
        newRoute = create_route(line[0],line[1]) #create the route
        routeRepo.add_obj_to_repo(newRoute) # add the route to the repo
        line = f.readline()


'''
a function that given a route repository and buss repository, it reads from a file the given busses and appends them into the repository
'''

def readBusses(routeRepo,bussRepo):
    f = open("busesFile","r")
    line = f.readline()
    while(len(line) != 0):
        line = line.split(",") # read the line
        route = routeRepo.objects[findRoute(routeRepo,int(line[1]))] # compute the route
        newBuss = create_buss(line[0],route,line[2],line[3]) # create the buss
        bussRepo.add_obj_to_repo(newBuss) #add the buss to the repo
        line = f.readline()