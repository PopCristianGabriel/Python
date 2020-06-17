'''
Created on Jan 9, 2019

@author: student
'''
import random 
from shipValidator import validate,in_grid
from ship import create_ship
from shipValidator import transform
from gameLogics import check_hit
from gameLogics import add_dead_ship


def computer_create_a_ship(lengths):
    shipX = chr(random.randint(65,72))
    shipY = random.randint(1,8)
    ok = False
    while(ok == False):
        ok = True
        shipLength = random.randint(2,4)
        if(shipLength not in lengths.values()):
            ok = False
    shipDirection = random.randint(1,4)
    return create_ship(shipX,shipY,shipLength,shipDirection)
    
    
    
    



def computer_choose_ships(computerRepo,howMany,lengths):
    for i in range (howMany):
        ok = False
        while(ok == False):
            ok = True
            newShip = computer_create_a_ship(lengths)
            if(validate(newShip,computerRepo,lengths,True) == False):
                ok = False
        computerRepo.add_object(newShip)
            
                
def computer_choose_a_random_target():
    shipX = random.randint(1,8)
    shipY = random.randint(1,8)
    return create_ship(shipX,shipY,1,1)


def computer_choose_a_target(computerHits,computerMisses,playerDeadShips):
    ok = False
    target = 1
    while(ok == False):
        ok = True
        target = computer_choose_a_random_target()
        #target = transform(target)
        x = target.ship_get_x()
        y = target.ship_get_y()
        if([x,y] in computerHits.objectList or [x,y] in computerMisses.objectList or [x,y] in playerDeadShips.objectList):
            ok = False
    #return create_ship(1,2,1,1)
    return target

def computer_analize_hit(target,result,playerRepo,computerHits,computerMisses,playerDeadShips):
    if(type(result) == type("A") and result == "Body"):
        print("the computer has hit one of your ships!")
        computerHits.add_object([target.ship_get_x(),target.ship_get_y()])
    elif(type(result) != type("No")):
        print("the computer has destroyed a ship!")
        add_dead_ship(playerDeadShips,result)
        playerRepo.remove_ship(result)
        i = 0
        while(i < len(computerHits.objectList)):
            if computerHits.objectList[i] in playerDeadShips.objectList:
                del computerHits.objectList[i]
            else:
                i += 1
    else:
        print("the computer has missed!")
        computerMisses.add_object([target.ship_get_x(),target.ship_get_y()])


def computer_hit_2(computerHits,computerMisses,playerDeadShips):
    letters = {0:"a",1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H",9:"J"}
    choises = [[-1,0],[1,0],[0,1],[0,-1]]
    increment = choises[random.randint(0,3)]
    newX = computerHits.objectList[len(computerHits.objectList)-1][0] + increment[0]
    newY = computerHits.objectList[len(computerHits.objectList)-1][1] + increment[1]
    if(newX == 0 or newX == 9 or newY >8 or newY < 1):
        return computer_hit_2(computerHits,computerMisses,playerDeadShips)
    newTarget = create_ship(letters[newX],newY,1,1)
    if (in_grid(newTarget,{1:1}) == False or ([newX,newY] in computerMisses.objectList == True) or ([newX,newY] in playerDeadShips.objectList == True) or ([newX,newY] in computerHits.objectList) == True):
        return computer_hit_2(computerHits,computerMisses,playerDeadShips)
    newTarget = transform(newTarget)
    return newTarget
    

def computer_hit(playerRepo,computerRepo,computerHits,computerMisses,computerDeadShips,playerDeadShips):
    
    
    
    if(len(computerHits.objectList) == 0):
        
        target = computer_choose_a_target(computerHits,computerMisses,playerDeadShips)
        result = check_hit(target,playerRepo.objectList)
        computer_analize_hit(target, result, playerRepo, computerHits, computerMisses, playerDeadShips)
    else:
        ok = False
        while(ok == False):
            ok = True
            target = computer_hit_2(computerHits,computerMisses,playerDeadShips)
            result = check_hit(target,playerRepo.objectList)
            computer_analize_hit(target, result, computerRepo, computerHits, computerMisses, playerDeadShips)
                                    
        
            
        
        
    





















