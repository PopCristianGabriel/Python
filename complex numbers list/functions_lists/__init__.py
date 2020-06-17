from auxiliaries import *
from console_ui import read_a_complex_number


def insert_element_at_the_end_of_the_list(list,number):
    list.append(number)


def insert_element_to_list(list,number,index):
    if(len(list) == 0):
        insert_element_at_the_end_of_the_list(list,number)
    else:
        list.insert(index,number)
        
def remove_element_from_a_list(list,replaced):
    list.remove(replaced)
    
    
def find_the_replaced(list,replaced):
    i = 0
    while(i < len(list)):
        if(get_real(list[i]) == get_real(replaced) and get_imag(list[i]) == get_imag(replaced)):
            return i
        i += 1
    print("The number hasn't been found")
    return -1

        
def replace_an_element_with_another(list,string):
        replacer = read_a_complex_number(string,2)
        replaced = read_a_complex_number(string)
        position = find_the_replaced(list,replaced)
        if(position != -1): 
            remove_element_from_a_list(list,replaced)
            insert_element_to_list(list, replacer, position)
        

def find_the_position_for_insertion(inputString):
    index = inputString.find("at ")
    while(is_a_digit(inputString[index]) == False):
        index += 1
    pos = int(inputString[index])
    if(pos < 0):
        print("invalid position")
        return -1
    return pos
        
def remove_a_sequence_of_elements(list,index1,index2):
    if(index1 == index2):
        list.pop(index1)
    else: 
        del list[index1:index2+1]
        
def remove_element_from_a_list_by_index(string,list):
    i = 0
    index1 = get_the_first_number(string)
    if(index1 >= len(list)):
        print("i can't remove from there")
        return
    if(index1 != -1 and string.find("to") != -1):
        index2 = get_the_last_number(string)
    else:
        index2 = index1
    remove_a_sequence_of_elements(list,index1,index2)
    
    
def sum_of_complex_numbers(list,inputString):
    startingIndex = (int(inputString[get_the_starting_index(inputString)]))
    stoppingIndex = (int(inputString[get_the_stopping_index(inputString)]))
    sum = [0,0]
    while(startingIndex <= stoppingIndex):
        sum = sum_of_two_complex_numbers(sum,list[startingIndex])
        startingIndex += 1
    return sum
        
        
def product_of_complex_numbers(list,inputString):
    startingIndex = (int(inputString[get_the_starting_index(inputString)]))
    stoppingIndex = (int(inputString[get_the_stopping_index(inputString)]))
    product = [1,0]
    while(startingIndex <= stoppingIndex):
        product = product_of_two_complex_numbers(product,list[startingIndex])
        startingIndex += 1
    return product


def keep_only_the_real_numbers(list):
    index = 0
    while(index < len(list)):
        if(get_imag(list[index]) != 0):
            remove_a_sequence_of_elements(list, index, index)
        else:
            index += 1


    
def delete_numbers_less_than(list,compareTo):
    index = 0
    while(index < len(list)):
        if(calculate_modulous(list[index]) >= compareTo):
            remove_a_sequence_of_elements(list, index, index)
        else:
            index += 1
            
            

            
def delete_numbers_greater_than(list,compareTo):
    index = 0
    while(index < len(list)):
        if(calculate_modulous(list[index]) <= compareTo):
            remove_a_sequence_of_elements(list, index, index)
        else:
            index += 1           


def filter_in_respect_to_modulo(list,string,compareTo):
    if(string.find("<") != -1):
        delete_numbers_less_than(list,compareTo)
    else:
        delete_numbers_greater_than(list,compareTo)
        
def undo_the_last_operation(history,list):
    newList = history[len(history) - 1].copy()
    if(len(history ) > 1):
        del history[-1]
        newList = history[len(history) - 1].copy()
    else:
        print("we arrived at the beginning")
    return newList
    