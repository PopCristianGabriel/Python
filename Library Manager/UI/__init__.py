def single_book_print(book):
        toPrint = ""
        toPrint += "book Title: " + book.book_get_title() + "\nbook's author: "+book.book_get_author() + "\nbook's id: " + str(book.get_id_function()) + "\nbook's description: " + book.book_get_description() + "\ndays rented: "+str(book.book_get_days_rented()) + "\ntimes rented: "+str(book.book_get_times_rented())+"\n\n"              
        print(toPrint)
        
        
def ui_print_a_book_list(bookList):
    for i in range(len(bookList)):
        single_book_print(bookList[i])
        
        
def ui_print_a_book_list_by_indexes(bookList,orderedList):
    for searchedBook in orderedList:
        searchedBookId = searchedBook.get_id_function()
        for book in bookList.objectList:
            if(searchedBookId == book.get_id_function()):
                single_book_print(book)
                break
            
            

def ui_print_a_dictionary_element(key,value):
    print("author ",key," has been rented; ",value," times")
    
def ui_print_a_dictionary(dictionary):
    for key, value in dictionary.items():
        ui_print_a_dictionary_element(key, value)
        print("\n")
        

def single_client_print(client):
        print("client's id is:",client.get_id_function())
        print("client's name is:",client.client_get_name())
        print("total days rented:",client.client_get_days_rented())
        print("\n")
        
def ui_print_a_client_list(clientList):
    for i in range(len(clientList)):
        single_client_print(clientList[i])
        
        