import unittest
from Repository import create_repository


class create_ship():
    def __init__(self,x,y,length,direction):
        self.x = x 
        self.y = y
        self.length = length
        self.direction = direction
        
        
    def ship_get_x(self):
        return self.x
    def ship_get_y(self):
        return self.y
    def ship_get_length(self):
        return self.length
    def ship_get_direction(self):
        return self.direction
    def ship_set_x(self,newX):
        self.x = newX
    def ship_set_y(self,newY):
        self.y = newY
    def ship_set_length(self,newX):
        self.length = newX
    def ship_set_direction(self,newY):
        self.direction = newY
        
        
    
    
    def get_increment(self):
        incrementX = 0
        incrementY = -1
        if(self.ship_get_direction() == 1):
            incrementX = 0
            incrementY = -1
        elif(self.ship_get_direction() == 2):
            incrementX = 1
            incrementY = 0
        elif(self.ship_get_direction() == 3):
            incrementX = 0
            incrementY = 1
        elif(self.ship_get_direction() == 4):
            incrementX = -1
            incrementY = 0
        return {"x" : incrementX,"y" : incrementY}
        
    
        
    
    def __str__(self):
        return str("x = " +str( self.ship_get_x()) + " y = " + str(self.ship_get_y()) + " length = " + str(self.ship_get_length()) + " direction = " + str(self.ship_get_direction()))
        
        
        
        
        
    def __eq__(self,another):
        currentX = self.ship_get_x()
        currentY = int(self.ship_get_y())
        for i in range (int(self.ship_get_length())):
            anotherX = another.ship_get_x()
            anotherY = int(another.ship_get_y())
            for j in range (int(another.ship_get_length())):
                if(anotherX == currentX and anotherY == currentY):
                    return True
                increment = another.get_increment()
                anotherX += increment["x"]
                anotherY += increment["y"]
            increment = self.get_increment()
            currentX += increment["x"]
            currentY += increment["y"]
            
    def is_the_same(self,ship2):
        return (self.ship_get_x() == ship2.ship_get_x() and self.ship_get_y() == ship2.ship_get_y())
           
    class ShipClassTest(unittest.TestCase):

        """
            This function is called before any test cases.
            We can add initialization code common to all methods here 
                (e.g. reading an input file)
        """
        def setUp(self):
            self.repo = create_repository()
            self.ship1 = create_ship(1,2,3,3)
            self.ship2 = create_ship(4,5,4,4)
            self.ship3 = create_ship(3,3,2,2)
    
        """
            This function is called after all test function are executed
            It's like the opposite of setUp, here you dismantle the test scaffolding
        """
        def tearDown(self):
            unittest.TestCase.tearDown(self)   
              
        def test_ship_creation(self):
            assert self.ship1.ship_get_x() == 1,1
            assert self.ship1.ship_get_y() == 2,2
            assert self.ship1.ship_get_direction() == 3,3
            assert self.ship1.ship_get_length() == 4,4
            
        def test_add_a_ship(self):
            assert self.repo == [],5
            self.repo.add_object(self.ship1),6
            assert len(self.repo.objectList) == 1
            
            
            
            