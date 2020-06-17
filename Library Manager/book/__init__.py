from repo import *
from UI import single_book_print
import unittest
from command import create_command
from iterable import filter_contains, shellSort
class create_book:
    def __init__(self,bookId,bookTitle,bookDescription,bookAuthor,ra,rs):
        self.bookId = bookId
        self.bookTitle = bookTitle
        self.bookDescription = bookDescription
        self.bookAuthor = bookAuthor
        self.nrOfTimeRented = ra
        self.NrOfDaysRented = rs
        
    def book_get_times_rented(self):
        return self.nrOfTimeRented 
    def book_get_days_rented(self):
        return self.NrOfDaysRented
    def get_id_function(self):
        return self.bookId
    def book_get_title(self):
        return self.bookTitle
    def book_get_description(self):
        return self.bookDescription
    def book_get_author(self):
        return self.bookAuthor
    
    
  
    def book_set_times_rented(self,v):
            self.nrOfTimeRented = v
    def book_set_days_rented(self,v):
            self.NrOfDaysRented = v
    def book_set_id(self,update):
        self.bookId = update
    def book_set_title(self,update):
        self.bookTitle = update
    def book_set_description(self,update):
        self.bookDescription = update
    def book_set_author(self,update):
        self.bookAuthor = update
        


        
        
        
        
    def __eq__(self,newBook):
        return self.book_get_author() == newBook.book_get_author() and self.book_get_description() == newBook.book_get_description() and self.book_get_title() == newBook.book_get_title()
        
'''this function adds a book to a book list'''
def book_add__book_to_a_list(bookList,book): 
    bookList.add_object_to_list(book)
    
    


def book_filter(bookList,searchCriteria,whatToSearch):
    if(filter_contains(bookList,whatToSearch) == True):
        print(whatToSearch)
        
def book_sort(bookList):
    return shellSort(bookList)


'this function removes a book from a bookList by its id and prints an error message if the id is incorrect'        
def book_remove_a_book_from_the_list(bookList,bookId,commandList,toAdd):
    bookIndex = bookList.find_an_object_by_id(bookId,0)
    if(bookIndex == -1):
        print("book id hasn't been found")
        return
    if(toAdd == 1):
        arguments = []
        arguments.append(bookList.objectList[bookIndex])
        command = create_command("remove book",arguments)
        commandList.add_object_to_list(command)
    bookList.remove_object_by_index(bookIndex)
'this function edits a book by its id, giving it a new title,author,description'
def book_edit_a_book(bookList,bookId,newBook,commandList,toAdd):
    bookIndex = bookList.find_an_object_by_id(bookId,0)
    if(bookIndex == -1):
        print("book id hasn't been found")
        return
    if(toAdd == 1):
        arguments = []
        arguments.append(bookList.objectList[bookId])
        arguments.append(newBook)
        command = create_command("update book",arguments)
        commandList.add_object_to_list(command)
    bookList.update_an_object_by_index(bookIndex,newBook)
    
'this function filters the book list by a criteria : title, author,id, description'
def book_filter_books(bookList,searchCriteria,whatToSearch):
    start = 0
    while(start != -1):
        if(searchCriteria == "title"):
            start = bookList.find_an_object_by_title(whatToSearch,start)
            if(start != -1):
                single_book_print(bookList.objectList[start])
                start += 1
        elif(searchCriteria == "author"):
            start = bookList.find_an_object_by_author(whatToSearch,start)
            if(start != -1):
                single_book_print(bookList.objectList[start])
                start += 1
        elif(searchCriteria == "id"):
            start = create_repository.find_an_object_by_id(bookList,int(whatToSearch),start)
            if(start != -1):
                single_book_print(bookList.objectList[start])
                start += 1
        elif(searchCriteria == "description"):
            start = bookList.find_an_object_by_description(whatToSearch,start)
            if(start != -1):
                single_book_print(bookList.objectList[start])
                start += 1
                
class BookClassTest(unittest.TestCase):

    """
        This function is called before any test cases.
        We can add initialization code common to all methods here 
            (e.g. reading an input file)
    """
    def setUp(self):
        self.repo = create_repository()
        self.book1 = create_book(1,"Test Title","Test Description","Test Author",0,0)
        self.book2 = create_book(2,"Test Title","Test Description","Test Author",0,0)
        self.book3 = create_book(3,"Test Title","Test Description","Test Author",0,0)

    """
        This function is called after all test function are executed
        It's like the opposite of setUp, here you dismantle the test scaffolding
    """
    def tearDown(self):
        unittest.TestCase.tearDown(self)
    
    def testAddBookToList(self):
        book_add__book_to_a_list(self.repo,self.book1)
        assert self.repo.objectList[0] == self.book1,1
        book_add__book_to_a_list(self.repo,self.book2)
        assert self.repo.objectList[1] == self.book2,55
        book_add__book_to_a_list(self.repo,self.book3)
        assert self.repo.objectList[2] == self.book3,3
    
    def testUpdateBook(self):
        book_add__book_to_a_list(self.repo,self.book1)
        assert self.repo.objectList[0] == self.book1,1
        newBook = create_book(4,"Test Title2","Test Description2","Test Author2",0,0)
        book_edit_a_book(self.repo,1,newBook)
        assert self.repo.objectList[0] == newBook,4
        
    def testRemoveBook(self):
        book_add__book_to_a_list(self.repo,self.book1)
        assert self.repo.objectList[0] == self.book1,1
        book_remove_a_book_from_the_list(self.repo, 1)
        assert len(self.repo.objectList) == 0,5


    
    