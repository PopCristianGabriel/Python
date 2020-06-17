from test.support import swap_attr
import operator



def nr_of_times_rented(book1,book2):
    return (book1.book_get_times_rented() < book2.book_get_times_rented())

def nr_of_days_rented(book1,book2):
    return (book1.book_get_days_rented() < book2.book_get_days_rented())

def client_nr_of_days_rented(client1,client2):
    return client1.client_get_days_rented() < client2.client_get_days_rented()

                            
def order_a_dictionary(dictionary):
    return sorted(dictionary.items(), key=operator.itemgetter(0),reverse=True)
               
                                        
def order_a_list_by_due_date(rentals,criteria): 
    ListImage = rentals.objectList.copy()
    ok = False
    while(ok == False):
        ok = True
        for i in range(len(ListImage) - 1):
            if(criteria(ListImage[i].rent_get_due_date(),ListImage[i].rent_get_rent_date()) < criteria(ListImage[i+1].rent_get_due_date(),ListImage[i+1].rent_get_rent_date())):
                aux = ListImage[i]
                ListImage[i] = ListImage[i+1]
                ListImage[i+1] = aux
                ok = False
    return ListImage  
                           
def orderAList(List,criteria):
    ListImage = List.objectList.copy()
    ok = False
    while(ok == False):
        ok = True
        for i in range(len(ListImage) - 1):
            if(criteria(ListImage[i],ListImage[i+1]) == True):
                aux = ListImage[i]
                ListImage[i] = ListImage[i+1]
                ListImage[i+1] = aux
                ok = False
    return ListImage
    