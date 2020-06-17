from client import *
from book import *
import random
''' this is an auxiliary function to the filter function, which returns the search criteria through "whatToSearch'''
def find_what_to_search(command):
    i = 3
    whatToSearch = ""
    while(i < len(command)):
        whatToSearch += command[i]
        if(i != len(command) - 1):
            whatToSearch += " "
        i += 1
    return whatToSearch

'''this function creates 100 clients and adds them to the list'''
def create_ten_clients(clientList,name_list_1,name_list_2):
    for i in range (100):
        newClient = create_client(i,pick_a_random_name(name_list_1, name_list_2))
        client_add_client_to_a_list(clientList, newClient)


def pick_a_random_name(name_list_1,name_list_2):
    name = ""
    index = random.randint(0,len(name_list_1)) - 1
    name += name_list_1[index]
    name += " "
    index = random.randint(0,len(name_list_2)) - 1
    name += name_list_2[index]
    return name
    
def pick_a_random_description(description):
    return description[random.randint(0,len(description))-1]
    
def pick_a_random_title(title1,title2):
    return pick_a_random_name(title1,title2)


'''this function creates 100 books and adds them to the list '''
def create_ten_books(bookList,title1,title2,description,name_list_1,name_list_2):
    for i in range (100):
        newBook = create_book(i,pick_a_random_title(title1, title2),pick_a_random_description(description),pick_a_random_name(name_list_1, name_list_2),0,0)
        book_add__book_to_a_list(bookList, newBook)
        
def read_a_string_input(message):
    return input(message)
def read_an_int_input(message):
    return int(input(message))