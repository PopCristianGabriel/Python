'''
Created on Nov 7, 2018

@author: student
'''

from rentals import *
import random
from Crypto.Cipher.DES import DESCipher
from statistics import nr_of_days_rented
from UI import ui_print_a_book_list
from iterable import *

def undo(commandList,commandListIndex,bookList,clientList):
    if(commandListIndex == -1):
        print("you are at the begging")
    else:
        
        if(commandList.objectList[commandListIndex].command_get_name() == "add book"):
            bookIndex = commandList.objectList[commandListIndex].command_get_arguments()[0].get_id_function()
            book_remove_a_book_from_the_list(bookList, bookIndex, commandList, 0)
            
        elif(commandList.objectList[commandListIndex].command_get_name() == "remove book"):
            book_add__book_to_a_list(bookList, commandList.objectList[commandListIndex].arguments[0])
        
        elif(commandList.objectList[commandListIndex].command_get_name() == "update book"):
            book_edit_a_book(bookList, commandList.objectList[commandListIndex].arguments[1].get_id_function(), commandList.objectList[commandListIndex].arguments[0], commandList, 0)
        
        elif(commandList.objectList[commandListIndex].command_get_name() == "add client"):
            clientIndex = commandList.objectList[commandListIndex].command_get_arguments()[0].get_id_function()
            client_remove_a_client_from_the_list(clientList, clientIndex, commandList, 0)
            
        elif(commandList.objectList[commandListIndex].command_get_name() == "remove client"):
            client_add_client_to_a_list(clientList, commandList.objectList[commandListIndex].arguments[0])
            
        elif(commandList.objectList[commandListIndex].command_get_name() == "update client"):
            client_edit_a_client(clientList, commandList.objectList[commandListIndex].arguments[1].get_id_function(), commandList.objectList[commandListIndex].arguments[0], commandList, 0)
        commandListIndex -= 1
        
            
            
    return commandListIndex


def redo(commandList,commandListIndex,bookList,clientList):
    if(commandListIndex == len(commandList.objectList ) - 1):
        print("you are at the end")
    else:
        commandListIndex += 1
        if(commandList.objectList[commandListIndex].command_get_name() == "remove book"):
            bookIndex = commandList.objectList[commandListIndex].command_get_arguments()[0].get_id_function()
            book_remove_a_book_from_the_list(bookList, bookIndex, commandList, 0)
            
        elif(commandList.objectList[commandListIndex].command_get_name() == "add book"):
            book_add__book_to_a_list(bookList, commandList.objectList[commandListIndex].arguments[0])
        
        elif(commandList.objectList[commandListIndex].command_get_name() == "update book"):
            book_edit_a_book(bookList, commandList.objectList[commandListIndex].arguments[0].get_id_function(), commandList.objectList[commandListIndex].arguments[1], commandList, 0)
        
        elif(commandList.objectList[commandListIndex].command_get_name() == "remove client"):
            clientIndex = commandList.objectList[commandListIndex].command_get_arguments()[0].get_id_function()
            client_remove_a_client_from_the_list(clientList, clientIndex, commandList, 0)
            
        elif(commandList.objectList[commandListIndex].command_get_name() == "add client"):
            client_add_client_to_a_list(clientList, commandList.objectList[commandListIndex].arguments[0])
            
        elif(commandList.objectList[commandListIndex].command_get_name() == "update client"):
            client_edit_a_client(clientList, commandList.objectList[commandListIndex].arguments[0].get_id_function(), commandList.objectList[commandListIndex].arguments[1], commandList, 0)
    return commandListIndex
        

def print_menu():
    
    print("you can type:")
    print("print books")
    print("add book")
    print("remove book")
    print("update book")
    print("print clients")
    print("add client")
    print("remove client")
    print("update client")
    print("print rentals")
    print("rent")
    print("search book")
    print("search client")
    print("undo")
    print("redo")
    print("statistic")
def run():
    name_list_1 = ["Pop ","Ileana","Dragus","Jurca","Sofrac","Leterna","Mermezan","Cioanca","Pitea","Trascaian"]
    name_list_2 = ["Andrei","Marcel","Cristi","Maria","Alex","Nicolae","Razvan","Darius","Robert","Carla","Denisa","Andreea","Mihai"]
    
    title1 = ["The adventure of" , "The return of", "The revenge of"]
    title2 = ["the four fantastics", "batman", " he great unknown", "politics"]
    
    description = ["this is an amazing book", "this book is rather dissapointing", "pls buy this book", "i was drunk when i wrote this", "10/10 best book"]
    
    commandList = create_repository()
    commandListIndex = -1
    
    bookId = 100
    clientId = 100
    rentalId = 1
    bookList = create_repository()
    clientList = create_repository()
    rentedBooks = create_repository()
    rentals = create_repository()
    create_ten_clients(clientList,name_list_1,name_list_2)
    create_ten_books(bookList,title1,title2,description,name_list_1,name_list_2)
    
    authorList = {}
    
    while(True):
        
        print_menu()
        userCommand = input("what do you wanna do:")
        
        
        if(userCommand.find("print books") != -1):
            ui_print_a_book_list(bookList.objectList)
            
            
        
            
        elif(userCommand.find("add book") != -1):
            bookTitle = read_a_string_input("enter the book's title:")
            bookAuthor = read_a_string_input("enter the book's author:")
            bookDescription = read_a_string_input("enter the book's description:")
            newBook = create_book(bookId,bookTitle,bookDescription,bookAuthor,0,0)
            bookId += 1
            book_add__book_to_a_list(bookList, newBook)
            if(commandListIndex <len(commandList.objectList) - 1):
                del commandList.objectList[commandListIndex + 1 :]
            arguments = []
            arguments.append(newBook)
            newCommand = create_command("add book",arguments)
            commandList.add_object_to_list(newCommand)
           
            commandListIndex += 1
            
            
        elif(userCommand.find("remove book") != -1):
            bookRemoveId = read_an_int_input("enter the book's id you wanna remove:")
            if(commandListIndex <len(commandList.objectList) - 1):
                del commandList.objectList[commandListIndex + 1 :]
            book_remove_a_book_from_the_list(bookList, bookRemoveId,commandList,1)
            commandListIndex += 1
            
        elif(userCommand.find("update book") != -1):
            editId = read_an_int_input("what book do you want to update?:")
            bookTitle = read_a_string_input("enter the book's title:")
            bookAuthor = read_a_string_input("enter the book's author:")
            bookDescription = read_a_string_input("enter the book's description:")
            newBook = create_book(editId,bookTitle,bookDescription,bookAuthor,0,0)
            if(commandListIndex <len(commandList.objectList) - 1):
                del commandList.objectList[commandListIndex + 1 :]
            book_edit_a_book(bookList, editId, newBook,commandList,1)
            commandListIndex += 1
            
        elif(userCommand.find("print clients") != -1):
            ui_print_a_client_list(clientList.objectList)
            
            
        elif(userCommand.find("add client") != -1):
            clientName = read_a_string_input("enter the new client's name:")
            newClient = create_client(clientId,clientName)
            client_add_client_to_a_list(clientList, newClient)
            if(commandListIndex <len(commandList.objectList) - 1):
                del commandList.objectList[commandListIndex + 1 :]
            arguments = []
            arguments.append(newClient)
            command = create_command("add client",arguments)
            commandList.add_object_to_list(command)
            clientId += 1
            commandListIndex += 1
            
        elif(userCommand.find("remove client") != -1):
            clientRemoveId = read_an_int_input("what client do you wanna remove?:")
            if(commandListIndex <len(commandList.objectList) - 1):
                del commandList.objectList[commandListIndex + 1 :]
            client_remove_a_client_from_the_list(clientList, clientRemoveId,commandList,1)
            commandListIndex += 1
            
        elif(userCommand.find("print rentals") != -1):
            ui_print_a_book_list(rentedBooks.objectList) 
            
        elif(userCommand.find("update client") != -1):
            clientUpdateIndex = read_an_int_input("what client do you want to update?:")
            clientName = read_a_string_input("enter the new client's name:")
            if(commandListIndex <len(commandList.objectList) - 1):
                del commandList.objectList[commandListIndex + 1 :]
            newClient = create_client(clientUpdateIndex,clientName)
            client_edit_a_client(clientList, clientUpdateIndex, newClient,commandList,1)
            commandListIndex += 1
            
        elif(userCommand.find("rent") != -1):
            renterId = read_an_int_input("which client wants to rent a book?:")
            index = clientList.find_an_object_by_id(renterId,0)
            if(index == -1):
                print("client not found")
            else:
                rentedBookId = read_an_int_input("enter the id of the book the client wants to rent:")
                rentDate = read_a_string_input("input the rent date:")
                rentDate = rentDate.split("/")
                rentDate = create_date(rentDate[0],rentDate[1],rentDate[2])
                dueDate = rentDate.set_due_date()
                rentedBookIndex = bookList.find_an_object_by_id(rentedBookId, 0)
                if(rentedBookIndex != -1):
                    bookList.objectList[rentedBookIndex].book_set_times_rented(bookList.objectList[rentedBookIndex].book_get_times_rented() + 1)
                    rentedBook = bookList.objectList[rentedBookIndex]
                    rentedBookAuthor = rentedBook.book_get_author()
                    if(rentedBookAuthor in authorList.keys()):
                        authorList[rentedBookAuthor] += 1  
                    else:
                        authorList[rentedBookAuthor] = 1
                    rental = create_rent(renterId,rentedBookId,rentDate,dueDate)
                    rental_add_rental_to_the_list(rentals,rental,rentedBooks,rentedBook)
                    book_remove_a_book_from_the_list(bookList, rentedBookId,clientList,1)
                else:
                    print("incorrect book id")
        elif(userCommand.find("return") != -1):
            returnedBookId = read_an_int_input("which book is coming back?:")
            returnedBookReturnDate = read_a_string_input("when is it comming back?")
            returnedBookReturnDate = returnedBookReturnDate.split("/")
            returnedBookReturnDate = create_date(returnedBookReturnDate[0],returnedBookReturnDate[1],returnedBookReturnDate[2])
            daysRented = rental_return_a_book(bookList,rentedBooks,returnedBookId,returnedBookReturnDate,rentals,clientList,commandList,0)
            bookList.objectList[len(bookList.objectList) - 1].book_set_days_rented(bookList.objectList[len(bookList.objectList) - 1].book_get_days_rented()+daysRented)
            
            
            
        elif(userCommand.find("search book") != -1):
            userCommand = userCommand.split()
            searchCriteria = userCommand[2]
            whatToSearch = find_what_to_search(userCommand)   
            book_filter_books(bookList,searchCriteria,whatToSearch) 
        elif(userCommand.find("search client") != -1):
            userCommand = userCommand.split()
            searchCriteria = userCommand[2]
            whatToSearch = find_what_to_search(userCommand)
            client_filter_clients(clientList, searchCriteria, whatToSearch)
            
        elif(userCommand.find("statistic") != -1):
            if(userCommand.find("books") != -1):
                if(userCommand.find("number") != -1):
                    booksOrderedByNrOfTimesRented = orderAList(bookList,nr_of_times_rented)
                    ui_print_a_book_list(booksOrderedByNrOfTimesRented)
                else:
                    booksOrderedByDaysRented = orderAList(bookList,nr_of_days_rented)
                    ui_print_a_book_list(booksOrderedByDaysRented)
            elif(userCommand.find("client") != -1):
                    clientsORderedByNrOfDaysRented = orderAList(clientList,client_nr_of_days_rented)
                    ui_print_a_client_list(clientsORderedByNrOfDaysRented)
            elif(userCommand.find("author") != -1):
                    order_a_dictionary(authorList)
                    ui_print_a_dictionary(authorList)
            elif(userCommand.find("late") != -1):
                lateBooks = create_repository()
                add_late_books(rentals,lateBooks)
                orderedList = order_a_list_by_due_date(lateBooks, create_date.date_days_between_two_dates)
                ui_print_a_book_list_by_indexes(rentedBooks,orderedList)
        
        elif(userCommand.find("undo") != -1):
            commandListIndex = undo(commandList, commandListIndex, bookList,clientList)        
        
        elif(userCommand.find("redo") != -1):
            commandListIndex = redo(commandList, commandListIndex, bookList,clientList)         
        
        elif(userCommand.find("exit") != -1):
            return
        
        
        else:
            print("invalid command")
        
    
run()