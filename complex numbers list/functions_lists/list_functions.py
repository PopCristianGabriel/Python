
from console_ui import *




def insert_element_at_the_end_of_the_list(list,number):
    list.append(number)


def insert_element_to_list(list,number,index):
    if(len(list) == 0):
        insert_element_at_the_end_of_the_list(list,number)
    else:
        list.insert(index,number)


def print_list(complexList):
    for number in complexList:
        print_a_complex_number(number)


def remove_element_from_a_list(list,replaced):
    list.remove(replaced)
    
    
def remove_a_sequence_of_elements(list,index1,index2):
    if(index1 == index2):
        list.pop(index1)
    else: 
        del list[index1:index2+1]