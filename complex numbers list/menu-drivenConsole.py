from cmath import sqrt
from _operator import index
from tkinter.constants import CURRENT
from _tracemalloc import start





def add_element_to_list(list,complex):
    list.append(complex)





def read_complex_number():
    Real = int(input("enter the real part of the number:"))
    Imag = int(input("enter the imaginary part of the number:"))
    complex_number = []
    add_element_to_list(complex_number,Real)
    add_element_to_list(complex_number,Imag)
    return complex_number







def print_a_complex_number(real,imag):
    if(real == 0 and imag == 0):
        print("0")
    if(real != 0): 
        print(real)
    if(imag != 0):  
        if(imag > 0):
            print("+")
        print(imag,"i")
        print("   ")





def print_list(list):
    
        i = 0
        while(i < len(list["Re"])):
            real = list["Re"][i]
            imag = list["Im"][i]
            print_a_complex_number(real,imag)
            i += 1
        
        
        
        
        
        
def calculate_modulus(complex_number):
    return complex_number[0] * complex_number[0] + complex_number[1] * complex_number[1]




def print_sequence_in_list(list,index1,index2):
    while(index1 <= index2):
        print_a_complex_number(list[index1][0],list[index1][1])
        index1 += 1
        
        
        
        
def find_the_indexes_of_the_list_with_ascending_moduluses(list):
    index1 = 0
    index2 = 0
    start = 0
    mod1 = calculate_modulus(list[0])
    currentSequence = 1
    imInSequence = False
    i = 1
    longestSequence = 1
    while(i < len(list) and len(list) - index2  > longestSequence):
        mod2 = calculate_modulus(list[i])
        if(mod2 > mod1):
            if(imInSequence == False):
                imInSequence = True
                start = i - 1
                currentSequence += 1
            else:
                currentSequence += 1
        if((mod2 <= mod1 and imInSequence == True) or i + 1 == len(list)):
            
            imInSequence = False
            if(currentSequence > longestSequence):
                longestSequence = currentSequence
                index1 = start
                index2 = i
            currentSequence = 1
        mod1 = mod2
        i += 1
    indexes = []
    add_element_to_list(indexes, index1)
    add_element_to_list(indexes, index2)
    return indexes
    





def print_sequence_with_ascending_moduluses(complex_list):
    listRe = complex_list["Re"]
    listIm = complex_list["Im"]
    i = 0
    list = []
    
    while(i < len(listRe)):
        complex_number = []
        add_element_to_list(complex_number, listRe[i])
        add_element_to_list(complex_number, listIm[i])
        add_element_to_list(list,complex_number)
        i += 1
    indexes = find_the_indexes_of_the_list_with_ascending_moduluses(list)
    print_sequence_in_list(list,indexes[0],indexes[1])    
    




def find_indexes_of_the_sequence_with_the_sum_of_moduluses10(list):
    
    index1 = -1
    index2 = -1
    sumRe = 0
    sumIm = 0
    i = 0
    longestSequence = 0
    start = 0
    while(start + longestSequence < len(list)):
        while((sumRe < 10 or sumIm < 10) and i < len(list)):
           sumRe += list[i][0]
           sumIm += list[i][1]
           i += 1
        if(sumRe == 10 and sumIm == 10 and i - start > longestSequence):
            index1 = start
            index2 = i - 1
            longestSequence = i - start
        sumRe = 0
        sumIm = 0
        start += 1
        i = start
    indexes  = []
    add_element_to_list(indexes,index1)
    add_element_to_list(indexes,index2)
    return indexes


def print_sequence_with_sum_of_moduluses10(complex_list):
    listRe = complex_list["Re"]
    listIm = complex_list["Im"]
    i = 0
    list = []
    
    while(i < len(listRe)):
        complex_number = []
        add_element_to_list(complex_number, listRe[i])
        add_element_to_list(complex_number, listIm[i])
        add_element_to_list(list,complex_number)
        i += 1
    
    
    indexes = []
    indexes = find_indexes_of_the_sequence_with_the_sum_of_moduluses10(list)
    if(indexes[0] == -1):
        print("there is no such sequence")
    else:
        print_sequence_in_list(list,indexes[0],indexes[1])  

def run():
    complex_list ={"Re":[],"Im":[]}
    while(True):
        console_input = input("enter a command:")
        if(console_input =="complex"):
            complex_number = read_complex_number()
            add_element_to_list(complex_list["Re"],complex_number[0])
            add_element_to_list(complex_list["Im"],complex_number[1])
        elif(console_input == "print"):
            print_list(complex_list)
        elif(console_input == "special1"):
            print_sequence_with_ascending_moduluses(complex_list)
        elif(console_input == "special2"):
            print_sequence_with_sum_of_moduluses10(complex_list)
        elif(console_input == "exit"):
            return
            

run()