'''
Created on Oct 21, 2018

@author: student
'''
from console_ui import *
from functions_lists import *
from tkinter.constants import INSERT
from cmath import sqrt
import math




   
    


def run():
    complexList = [[2,3],[4,5],[-1,-2],[-7,0],[-23,266],[3,4],[-456,0],[254,-11],[100,101],[-555,-777]]
    history = []
    history.append(0)
    history[0] = complexList.copy()
    #complexList[0] = 1
    print("what interface do you want to have?")
    print("type -command-" " for a command based interface")
    print("type -menu- for a menu based interface")
    selectMenu = input()
    if(selectMenu.find("menu") != -1):
        
    
        while(True):
            print("your usable commands are : add /// insert /// remove /// replace /// filter /// list /// sum /// product /// undo /// exit")
            user_command = input("enter a command:")
            
            
            
            if(user_command.find("add") != -1):
                user_command = input("enter a number:")
                complexNumber = read_a_complex_number(user_command)
                insert_element_at_the_end_of_the_list(complexList,complexNumber)
                update_history(history,complexList)
    
                
                
                
                
            elif(user_command.find("insert") != -1):
                number = input("what number do you want to add?")
                number = number + " "
                location = input("give me the position where you want to add")
                user_command = number + location
                complexNumber = read_a_complex_number(user_command,2)
                position = find_the_position_for_insertion(user_command)
                if(position != -1):
                    insert_element_to_list(complexList,complexNumber,position)
                    update_history(history,complexList)
    
    
    
    
    
            elif(user_command.find("remove") != -1):
                user_command = input("what element do you want to remove?")
                question = input("do you want to remove a list? y/n")
                if(question =="y"):
                    index2 = input("what's the last element you want to remove?")
                    user_command = user_command + "to"
                    user_command = user_command + index2
                    remove_element_from_a_list_by_index(user_command,complexList)
                else:
                    remove_a_sequence_of_elements(complexList, int(user_command), int(user_command))
                update_history(history,complexList)
    
    
    
    
    
    
            elif(user_command.find("replace")  != -1):
                user_command = input("what element do you want to replace?")
                user_command = user_command + "with"
                replacer = input("with what element do you want that number to be replaced with?")
                user_command = user_command + replacer
                replace_an_element_with_another(complexList,user_command)
                update_history(history,complexList)
                
                
                
                
                
            elif(user_command.find("filter")!= -1):
                user_command = input("what do you want to filter? real/ modoulous <x  modoulous > x")  
                if(user_command.find("real") != -1):
                    keep_only_the_real_numbers(complexList)
                    update_history(history,complexList)
                else: 
                    compareTo = find_the_real_part(user_command, len(user_command)-1)
                    filter_in_respect_to_modulo(complexList,user_command,compareTo)
                    update_history(history,complexList)
            
            
            
                
            elif(user_command == "list"):
                question = input("what do you want to print? simple - the whole list, modulous >x, = x, <x , real - print only real numbers\n")
                user_command += question 
                if(user_command.find("real") != -1):
                    start = input("where do you wanna start?")
                    end = input("where do you wanna end?")
                    user_command = user_command + start + "to" + end
                    print_real_only(complexList,user_command)
                elif(user_command.find("<") != -1 or user_command.find("=") != -1 or user_command.find(">") != -1):
                    print_numbers_with_modulous_properties(complexList,user_command)
                else:
                    print_list(complexList)
                
                
                
           
            elif(user_command.find("sum") != -1):
                start = input("where do you wanna start?")
                end = input("where do you wanna end?")
                user_command = user_command + start + " " + end
                print_a_complex_number(sum_of_complex_numbers(complexList,user_command))
                
                
                
                
                
            elif(user_command.find("product") != -1):
                start = input("where do you wanna start?")
                end = input("where do you wanna end?")
                user_command = user_command + start + " " + end
                print_a_complex_number(product_of_complex_numbers(complexList,user_command))
                
                
                
                
                
            elif(user_command.find("undo") != -1):
                complexList = undo_the_last_operation(history,complexList)
    
    
    
            elif(user_command == "exit"):
                return
   
    
    
    else:
         while(True):    
            user_command = input("enter a command:")
            
            
            
            if(user_command.find("add") != -1):
                
                complexNumber = read_a_complex_number(user_command)
                insert_element_at_the_end_of_the_list(complexList,complexNumber)
                update_history(history,complexList)
    
                
                
                
                
            elif(user_command == "list"):
                print_list(complexList)
                
                
                
                
            elif(user_command.find("insert") != -1):
                complexNumber = read_a_complex_number(user_command,2)
                position = find_the_position_for_insertion(user_command)
                if(position != -1):
                    insert_element_to_list(complexList,complexNumber,position)
                    update_history(history,complexList)
    
    
            elif(user_command.find("remove") != -1):
                remove_element_from_a_list_by_index(user_command,complexList)
                update_history(history,complexList)
    
            elif(user_command.find("replace")  != -1):
                replace_an_element_with_another(complexList,user_command)
                update_history(history,complexList)
                
                
            elif(user_command.find("filter real") != -1):
                keep_only_the_real_numbers(complexList)
                update_history(history,complexList)
                
                
                
            elif(user_command.find("filter") != -1):
                compareTo = find_the_real_part(user_command, len(user_command)-1)
                filter_in_respect_to_modulo(complexList,user_command,compareTo)
                update_history(history,complexList)
                
                
            elif(user_command.find("<") != -1 or user_command.find("=") != -1 or user_command.find(">") != -1):
                print_numbers_with_modulous_properties(complexList,user_command)
                
            elif(user_command.find("list") != -1):
                print_real_only(complexList,user_command)
            elif(user_command.find("sum") != -1):
                print_a_complex_number(sum_of_complex_numbers(complexList,user_command))
            elif(user_command.find("product") != -1):
                print_a_complex_number(product_of_complex_numbers(complexList,user_command))
            elif(user_command.find("undo") != -1):
                complexList = undo_the_last_operation(history,complexList)
    
            elif(user_command == "exit"):
                return
            

run()

