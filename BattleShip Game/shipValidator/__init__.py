from ship import *


def in_grid(ship,lengths):
    
    directions = [1,2,3,4]
    if(ship.ship_get_x() > "H" or ship.ship_get_x() <"A"):
        raise ValueError("incorrect horizontal input")
    checkY = int(ship.ship_get_y())
    if(checkY < 1 or checkY > 8):
        raise ValueError("incorrect vertical input")
    length = int(ship.ship_get_length())
    direction = int(ship.ship_get_direction())
    
    
    if length not in lengths.values():
        raise ValueError("incorrect length")
    if(direction not in directions):
        raise ValueError("incorrect direction")
    
    
    if(direction == 2 and chr(ord(ship.ship_get_x()) + int(ship.ship_get_length()) - 1) > "H"):
        raise ValueError("out of the grid")
    if(direction == 4 and chr(ord(ship.ship_get_x()) - int(ship.ship_get_length()) + 1) < "A"):
        raise ValueError("out of the grid")
    if(direction == 1 and int(ship.ship_get_y()) - int(ship.ship_get_length()) + 1 < 1):
        raise ValueError("out of the grid")
    if(direction == 3 and int(ship.ship_get_y()) + int(ship.ship_get_length())  - 1> 8):
        raise ValueError("out of the grid")
   
    


def overlap(ship,shipRepo):
    for anotherShip in shipRepo.objectList:
        if(ship == anotherShip):
            return True
        return False


def transform(ship):
    xTranslate = {"A" : 1, "B" : 2, "C" : 3, "D" : 4, "E" : 5 , "F" : 6 , "G" : 7, "H" : 8}
    ship.ship_set_direction(int(ship.direction))
    ship.ship_set_y(int(ship.y))
    ship.ship_set_x(xTranslate[ship.ship_get_x()])
    ship.ship_set_length(int(ship.length))
    return ship


def validate(ship,shipRepo,lengths,computer = False):
    
    try:
        in_grid(ship,lengths)
    except ValueError as ve:
        if (computer == False): 
            print(ve)
        return False
    ship = transform(ship)
    
    if(overlap(ship,shipRepo) == True):
        
        if(computer == False):
            print("overlapping ships")
        return False
    lengths.pop(ship.ship_get_length())
    
    return True



    