'''
Created on Oct 25, 2018

@author: student
'''
from list_functions import *




def is_a_digit(character):
    digits = ['0','1','2','3','4','5','6','7','8','9']
    for digit in digits:
        if(digit == character):
            return True
    return False

def delete_the_digit(string,digitIndex):
    string = list(string)
    del string[digitIndex]
    string = "".join(string)
    return string

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


def find_the_imaginary_part(string,digitIndex):
    number = 0
    neg = 1
    if(string[digitIndex - 1] =='-'):
        neg = -1
    while(digitIndex < len(string) and is_a_digit(string[digitIndex]) == True):
        number = number * 10 + int(string[digitIndex])
        delete_the_digit(string, digitIndex)
        digitIndex += 1
    return number * neg
    
    
def find_the_real_part(string,digitIndex):
    number = 0
    power = 1
    neg = 1
    while(digitIndex >= 0 and is_a_digit(string[digitIndex]) == True):
        number = number + power * int(string[digitIndex])
        power *= 10
        delete_the_digit(string, digitIndex)
        digitIndex -= 1
    if(string[digitIndex] == "-"):
        neg = -1
    return number * neg


def get_real(number):
    return number[0]
                         
def get_imag(number):
    return number[1]


def print_a_complex_number(number):
    real = get_real(number)
    imag = get_imag(number)
    if(real == 0 and imag == 0):
        print("0")
    if(real != 0): 
        print(real)
    if(imag != 0):  
        if(imag > 0):
            print("+")
        print(imag,"i")
        print("   ")

