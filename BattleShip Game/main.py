from Repository import create_repository
from shipValidator import *
import random
from playerFunctions import *
from computerFunctions import *
from gameLogics import *
from _tkinter import create




def print_ships(list):
    for ship in list.objectList:
        print(ship)


def game():
    playerRepo = create_repository()
    computerRepo = create_repository()
    
    playerDeadShips = create_repository()
    computerDeadShips = create_repository()
    
    playerHits = create_repository()
    computerHits = create_repository()
    
    playerMisses = create_repository()
    computerMisses = create_repository()
    
    myShips = create_repository()
   
   
    lengths = {2:2,3:3,4:4}
    turn = 0
    player_add_ships(playerRepo,lengths)
    #playerRepo.add_object(create_ship(1,1,4,3))
    #playerRepo.add_object(create_ship(2,1,3,3))
    #playerRepo.add_object(create_ship(3,1,2,3))
    lengths = {2:2,3:3,4:4}
    

    lengths = {2:2,3:3,4:4}
    computer_choose_ships(computerRepo,3,lengths)
    
    lengths = {1:1} 
    
    for ship in playerRepo.objectList:
        add_dead_ship(myShips,ship)
        
    
    while(check_end_game(playerRepo,computerRepo) == 0):
        if(turn % 2 == 0):
            
            
            draw_my_grid(myShips,playerDeadShips,computerHits,computerMisses)
            
            
            
            draw_enemy_grid(playerHits,playerMisses,computerDeadShips)
            
           
            target  = player_choose_a_target(lengths)    
            
            target = transform(target)
            
            result = check_hit(target,computerRepo.objectList)
            
            print("")
            print("")
            print("")
            player_analize_hit(target,result,playerHits,computerDeadShips,playerMisses,computerRepo)
            
            print("")
            print("")
            print("")
        else:
            
            computer_choose_a_target(computerHits, computerMisses, playerDeadShips)
            computer_hit(playerRepo, computerRepo, computerHits, computerMisses, computerDeadShips, playerDeadShips)
            
        turn += 1
        
            
       
    print("this is the end")  
    print("hold your breath and count to 10")   
    

            
            
        
game()