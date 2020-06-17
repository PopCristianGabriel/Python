'''
Created on Jan 9, 2019

@author: student
'''


from ship import create_ship
from shipValidator import validate
from shipValidator import in_grid
from gameLogics import add_dead_ship


def read_a_ship(lengths,ask = True):
        
        shipX = input("give a letter : A-H: ")
        shipY = input("give a number : 1-8: ")
        if(ask == True):
            print("remaining lengths are:")
            print(lengths.keys())
            length = input("enter a length : 2 , 3 or 4: ")
            direction = input("enter a direction : 1(up), 2(right), 3(down), 4(left): ")
            return create_ship(shipX,shipY,length,direction)
        return create_ship(shipX,shipY,1,1)

def player_add_ships(playerRepo,lengths,howMany = 3):
    for i in range (howMany):
        ship = read_a_ship(lengths)
        while(validate(ship,playerRepo,lengths) == False):
            ship = read_a_ship(lengths)
        playerRepo.add_object(ship)
    




def player_choose_a_target(lengths):
    ok = False
    while(ok == False):
        
        print("enter a target")
        ok = True
      
        target = read_a_ship(lengths, False)
        try:
            in_grid(target,lengths)
        except ValueError as ve:
            
            print(ve)
            ok = False
    return target




def player_analize_hit(target,result,playerHits,computerDeadShips,playerMisses,computerRepo):
    if(type(result) == type("A") and result == "Body"):
        print("YOU'VE HIT!")
        playerHits.add_object([target.ship_get_x(),target.ship_get_y()])
    elif(type(result) != type("No")):
        print("YOU'VE DESTROYED A SHIP!")
        add_dead_ship(computerDeadShips,result)
        computerRepo.remove_ship(result)
    else:
        print("MISS!")
        playerMisses.add_object([target.ship_get_x(),target.ship_get_y()])
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        