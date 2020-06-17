from auxiliaries import *



def insert_element_at_the_end_of_the_list(list,number):
    list.append(number)

def delete_the_digit(string,digitIndex):
    string = list(string)
    del string[digitIndex]
    string = "".join(string)
    return string

def find_the_imaginary_part(string,digitIndex):
    number = 0
    negative = 1
    if(string[digitIndex - 1] =='-'):
        negative = -1
    while(digitIndex < len(string) and is_a_digit(string[digitIndex]) == True):
        number = number * 10 + int(string[digitIndex])
        delete_the_digit(string, digitIndex)
        digitIndex += 1
    return number * negative
    
    
def find_the_real_part(string,digitIndex):
    number = 0
    power = 1
    negative = 1
    while(digitIndex >= 0 and is_a_digit(string[digitIndex]) == True):
        number = number + power * int(string[digitIndex])
        power *= 10
        delete_the_digit(string, digitIndex)
        digitIndex -= 1
    if(string[digitIndex] == "-"):
        negative = -1
    return number * negative
    
    
def read_a_complex_number(inputString,whichOne = 1):
    number = []
    if(whichOne == 2):
        signIndex = inputString.rfind("i")
    else:
        signIndex = inputString.find("i")

    input_string = delete_the_digit(inputString, signIndex)
    while(inputString[signIndex] != "-" and inputString[signIndex] != "+"):
        signIndex -= 1
    imaginaryPart  = find_the_imaginary_part(inputString,signIndex + 1)
    realPart = find_the_real_part(inputString,signIndex - 1)
    insert_element_at_the_end_of_the_list(number,realPart) # add the real part
    insert_element_at_the_end_of_the_list(number,imaginaryPart) # add the imaginary part
    return number

    

def print_a_complex_number(number):
    real = get_real(number)
    imag = get_imag(number)
    numberToPrint =''
    if(real == 0 and imag == 0):
        numberToPrint =  numberToPrint +'0'
    if(real != 0): 
        numberToPrint = numberToPrint + (str(real))
    if(imag != 0):  
        if(imag > 0): 
           numberToPrint =  numberToPrint+'+'
        numberToPrint = numberToPrint+(str(imag)) +'i'
    print(numberToPrint)

def print_list(complexList):
    for number in complexList:
        print_a_complex_number(number)
        

def print_real_only(list,string):
    index1 = find_the_imaginary_part(string,get_the_starting_index(string))
    if(index1 != -1 and string.find("to") != -1):
         index2 = find_the_real_part(string,get_the_stopping_index(string))
    while(index1 <= index2 and index1 < len(list)):  
        if(get_imag(list[index1]) == 0):
             print_a_complex_number(list[index1])
        index1 += 1





def print_numbers_less_than(list,compareTo):
    for number in list:
        if(calculate_modulous(number) < compareTo):
            print_a_complex_number(number)
            
            
def print_numbers_equal_to(list,compareTo):
    for number in list:
        if(calculate_modulous(number) == compareTo):
            print_a_complex_number(number)
            
def print_numbers_bigger_than(list,compareTo):
    for number in list:
        if(calculate_modulous(number) > compareTo):
            print_a_complex_number(number)            


def print_numbers_with_modulous_properties(list,string):
    digitIndex =get_the_stopping_index(string)
    compareTo = find_the_real_part(string, digitIndex)
    if(string.find("<") != -1):
        print_numbers_less_than(list,compareTo)
    elif(string.find("=")!= -1):
        print_numbers_equal_to(list,compareTo)
    else:
        print_numbers_bigger_than(list,compareTo)