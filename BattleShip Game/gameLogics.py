'''
Created on Jan 9, 2019

@author: student
'''
def draw_enemy_grid(playerHits,playerMisses,computerDeadShips):
    letter = ['A','B','C','D','E','F','G','H','q']
    i = 0
    j = 0
    while(j <= 8):
        i = 0
        while(i <= 8):
            if(j == 0):
                print(letter[i-1],'',end ="")
                if(letter[i-1] =="q"):
                    print(" ",end = "")
            if(i == 0 and j != 0):
                print(j,' ',end ='')
            if ([i,j] in playerHits.objectList and [i,j] not in computerDeadShips.objectList):
                print("X ",end = "")
            elif([i,j] in computerDeadShips.objectList):
                print("D ",end = "")
            elif([i,j] in playerMisses.objectList):
                print("M ",end = "")
            elif(j != 0 and i != 0):
                print("O ",end = "")
            i += 1
        print(" ")
        j += 1
    print("")
    print("")

def draw_my_grid(myShips,playerDeadShips,computerHits,computerMisses):
    print("Your grid is:")
    i = 1
    j = 1
    while(j <= 8):
        i = 1
        while(i <= 8):
            if([i,j] in computerHits.objectList):
                print("x ",end = "")
            elif([i,j] in playerDeadShips.objectList):
                print("D ",end = "")
            elif([i,j] in myShips.objectList):
                print("S ",end = "")
            
            elif([i,j] in computerMisses.objectList):
                print("x ",end = "")
            else:
                print("O ",end = "")
            i += 1
        print(" ")
        j += 1
    print("")
    print("")
    print("")
    print("Enemy grid is:")  




def check_hit(target,shipList):
    for i in range(len(shipList)):
        if(target.ship_get_x() == shipList[i].ship_get_x() and target.ship_get_y() == shipList[i].ship_get_y()):
            return shipList[i]
        elif(shipList[i] == target):
            return "Body"
    return "No"


def add_dead_ship(hits,ship):
    increment = ship.get_increment()
    currentX = ship.ship_get_x()
    currentY = ship.ship_get_y()
    for i in range(ship.ship_get_length()):
        hits.add_object([currentX,currentY])
        currentX += increment["x"]
        currentY += increment["y"]

def check_end_game(playerRepo,computerRepo):
    if(len(playerRepo.objectList) != 0 and len(computerRepo.objectList) != 0):
        return 0
    if(len(playerRepo.objectList) == 0):
        print("you've lost")
        return 1
    else:
        print("you've won")
        return 2

