from repo import *
import unittest
from command import create_command
from UI import single_client_print

class create_client():
    def __init__(self,clientId,clientName):
        self.clientId = clientId
        self.clientName = clientName
        self.daysRented = 0
        
    def get_id_function(self):
        return self.clientId
    def client_get_name(self):
        return self.clientName
    def client_get_days_rented(self):
        return self.daysRented
    
    
    
    def client_set_days_rented(self,v):
        self.daysRented = v
  
    
    def client_set_id(self,update):
        self.clientId = update
    def client_set_name(self,update):
        self.clientName = update
        
    
        
    def __eq__(self,newClient):
        return self.client_get_name() == newClient.client_get_name()

        

def client_add_client_to_a_list(clientList,client):
    clientList.add_object_to_list(client)
    
    
    
def client_filter_clients(clientList,searchCriteria,whatToSearch):
    start = 0
    while(start != -1):
        if(searchCriteria == "name"):
            start = clientList.find_a_client_by_name(whatToSearch,start)
            if(start != -1):
                single_client_print(clientList.objectList[start])
                start += 1
        elif(searchCriteria == "id"):
            start = clientList.find_an_object_by_id(int(whatToSearch),start)
            if(start != -1):
                single_client_print(clientList.objectList[start])
                start += 1

        
def client_remove_a_client_from_the_list(clientList,clientId,commandList,toAdd):
    
    clientIndex = clientList.find_an_object_by_id(clientId,0)
    if(clientIndex == -1):
        
        print("client id hasn't been found")
        return
    if(toAdd == 1):
        arguments = []
        arguments.append(clientList.objectList[clientIndex])
        command = create_command("remove client",arguments)
        commandList.add_object_to_list(command)
    clientList.remove_object_by_index(clientIndex)

def client_edit_a_client(clientList,clientId,newClient,commandList,toAdd):
    clientIndex = clientList.find_an_object_by_id(clientId,0)
    if(clientIndex == -1):
        
        print("client id hasn't been found")
        return
    if(toAdd == 1):
        arguments = []
        arguments.append(clientList.objectList[clientIndex])
        arguments.append(newClient)
        command = create_command("update client",arguments)
        commandList.add_object_to_list(command)
    clientList.update_an_object_by_index(clientIndex,newClient)
    
    
    
class BookClassTest(unittest.TestCase):

    """
        This function is called before any test cases.
        We can add initialization code common to all methods here 
            (e.g. reading an input file)
    """
    def setUp(self):
        self.repo = create_repository()
        self.client1 = create_client(1,"Tudor")
        self.client2 = create_client(2,"Alex")
        self.client3 = create_client(3,"Andrei")

    """
        This function is called after all test function are executed
        It's like the opposite of setUp, here you dismantle the test scaffolding
    """
    def tearDown(self):
        unittest.TestCase.tearDown(self)
    
    def testAddClientkToList(self):
        client_add_client_to_a_list(self.repo,self.client1)
        assert self.repo.objectList[0] == self.client1,1
        client_add_client_to_a_list(self.repo,self.client2)
        assert self.repo.objectList[1] == self.client2,55
        client_add_client_to_a_list(self.repo,self.client3)
        assert self.repo.objectList[2] == self.client3,3
    
    def testUpdateClient(self):
        client_add_client_to_a_list(self.repo,self.client1)
        assert self.repo.objectList[0] == self.client1,22
        newClient = create_client(4,"Marius")
        client_edit_a_client(self.repo,1,newClient)
        assert self.repo.objectList[0] == newClient,4
        
    def testRemoveBook(self):
        client_add_client_to_a_list(self.repo,self.client1)
        assert self.repo.objectList[0] == self.client1,22
        client_remove_a_client_from_the_list(self.repo, 1)
        assert len(self.repo.objectList) == 0,5

        