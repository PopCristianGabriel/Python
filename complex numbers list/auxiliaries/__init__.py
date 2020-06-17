
import math

def get_real(number):
    return number[0]
                         
def get_imag(number):
    return number[1]


def set_real(number,data):
    number[0] = data


def set_imag(number,data):
    number[1] = data
    

def is_a_digit(character):
    digits = ['0','1','2','3','4','5','6','7','8','9']
    for digit in digits:
        if(digit == character):
            return True
    return False

def get_the_starting_index(string):
    i = 0
    index = 0
    while(i < len(string)):
        if(is_a_digit(string[i]) == True):
            index = i
            break
        i += 1
    if(i >= len(string)):
        print("i haven't found the index")
        return -1
    return i

def get_the_stopping_index(string):
    
    i = len(string) - 1
    while(i >= 0):
        if(is_a_digit(string[i])):
            index2 = i
            break
        i -= 1
    if(i < 0):
        print("i haven't found the index")
        return -1
    return i

def get_the_first_number(string):
    i = 0
    index = 0
    number = 0
    while(i < len(string) and is_a_digit(string[i]) == False):
        i += 1
    while(i < len(string)  and  is_a_digit(string[i]) == True):
        number = number * 10 +int(string[i])
        i += 1
    if(i > len(string)):
        print("i haven't found the index")
        return -1
    return number

def get_the_last_number(string):
    number = 0
    power = 1
    i = len(string) - 1
    while(i >= 0 and is_a_digit(string[i]) == False):
        i -= 1
    while(i >= 0 and is_a_digit(string[i]) == True):
        number = number + power * int(string[i])
        power *= 10
        i -= 1
    if(i < 0):
        print("i haven't found the index")
        return -1
    return number




def sum_of_two_complex_numbers(complex1 , complex2):
    result = []
    result.append(get_real(complex1) + get_real(complex2))
    result.append(get_imag(complex1) + get_imag(complex2))
    return result


def product_of_two_complex_numbers(complex1,complex2):
    result = []
    result.append(get_real(complex1) * get_real(complex2))
    result.append(get_real(complex1) * get_imag(complex2))
    set_real(result, get_real(result) + get_imag(complex1) * get_imag(complex2) * (-1))
    set_imag(result,get_imag(result) + get_imag(complex1) * get_real(complex2))
    return result


def calculate_modulous(number):
    return (math.sqrt(get_real(number) * get_real(number) + get_imag(number) * get_imag(number)))
    
def update_history(history,list):
    history.append(0)
    history[len(history) - 1] = list.copy()