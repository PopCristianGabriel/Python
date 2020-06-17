from repo import *
from dates import *
from UI import *
from statistics import *
from mySetup import *
import datetime



class create_rent():
    def __init__(self,clientId,bookId,rentDate,dueDate):
        self.clientId = clientId
        self.bookId = bookId
        self.rentDate = rentDate
        self.dueDate = dueDate
        
    
    def get_id_function(self):
        return self.bookId
    def rent_get_client_id(self):
        return self.clientId
    def rent_get_rent_date(self):
        return self.rentDate
    def rent_get_due_date(self):
        return self.dueDate
    
    
    'this function adds a rental object to the list and adds the book in question in the rented books list'
def rental_add_rental_to_the_list(rentList,rent,rentedBooks,book):
    rentList.add_object_to_list(rent)
    rentedBooks.add_object_to_list(book)
    ''' his function returns a book to the booklist and updates nr of times the book was rented, nr of days the book was rented
       and nr of days a person rented a book'''
    
def rental_return_a_book(bookList,rentedBooks,returnedBookId,cameBackDate,rentList,clientList,commandList,toAdd):
    index = 0
    while(index < len(rentList.objectList) and rentList.objectList[index].get_id_function() != returnedBookId):
        index += 1
    if(index >= len(rentList.objectList)):
        print("incorrect id")
        return -1
    else:
        days = create_date.date_days_between_two_dates(rentList.objectList[index].rent_get_rent_date(),cameBackDate)
        if(days == -1):
            days = create_date.date_days_between_two_dates(cameBackDate,rentList.objectList[index].rent_get_rent_date()) 
        clientList.objectList[rentList.objectList[index].rent_get_client_id()].client_set_days_rented(clientList.objectList[rentList.objectList[index].rent_get_client_id()].client_get_days_rented() + days)
        book = rentedBooks.objectList[index]
        rentedBooks.remove_object_by_index(index)
        rentList.remove_object_by_index(index)
        book_add__book_to_a_list(bookList, book)
        if(toAdd == 1):
            arguments = []
            arguments.append(book)
            command = create_command("return",arguments)
            commandList.add_object_to_list(command)
    return days

'''this function checks wether or not a book is late '''

def book_is_late(date):
    now = datetime.datetime.now()
    if(now.year > date.date_get_year()):
        return True
    elif(now.year < date.date_get_year()):
        return False
    
    if(now.month > date.date_get_month()):
        return True
    if(now.month < date.date_get_month()):
        return False
    if(now.day > date.date_get_day()):
        return True
    if(now.day < date.date_get_day()):
        return False
    return False


'''this function adds a late book to the late books list '''
def add_late_books(rentals,lateBooks):
    for rental in rentals.objectList:
        if(book_is_late(rental.rent_get_due_date())):
            lateBooks.add_object_to_list(rental)
            
            

class BookClassTest(unittest.TestCase):

    """
        This function is called before any test cases.
        We can add initialization code common to all methods here 
            (e.g. reading an input file)
    """
    def setUp(self):
        self.repo = create_repository()
        self.lateBooks = create_repository()
        self.rent1 = create_rent(1,1,create_date(1,1,1990),create_date(1,10,1990))
        self.rent2 = create_rent(1,1,create_date(25,11,2018),create_date(5,12,2018))

    """
        This function is called after all test function are executed
        It's like the opposite of setUp, here you dismantle the test scaffolding
    """
    def tearDown(self):
        unittest.TestCase.tearDown(self)
    
    def testbook_is_late(self):
        assert book_is_late(self.rent2.rent_get_due_date()) == False
        assert book_is_late(self.rent1.rent_get_due_date()) == True
    
    def testadd_late_bookst(self):
        self.repo.add_object_to_list(self.rent1)
        self.repo.add_object_to_list(self.rent2)
        add_late_books(self.repo,self.lateBooks)
        assert len(self.lateBooks.objectList) == 1
        
   

        