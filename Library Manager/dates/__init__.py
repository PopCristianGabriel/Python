import unittest
from repo import *

class create_date():
    def __init__(self,day,month,year):
        self.day = int(day)
        self.month = int(month)
        self.year = int(year)
        
        
        self.months = [0,31,29,31,30,31,30,31,31,30,31,30,31]
        
        
        
    def date_get_day(self):
        return self.day
    
    def date_get_month(self):
        return self.month
    
    
    def date_get_year(self):
        return self.year
    
        
    def date_set_day(self,v):
        self.day = v
    
    def date_set_month(self,v):
        self.month = v
    
    
    def date_set_year(self,v):
        self.year = v        
    
    def __equ__(self,date2):
        return self.date_get_day() == date2.date_get_day() and self.date_get_month() == date2.date_get_month() and self.date_get_year() == date2.date_get_year()
    
    
    def days_left_in_year(self,month):
        i = 1
        days = 0
        while(i < month):
            days += self.months[i]
            i += 1
        return days
    
    def set_due_date(self):
        month = self.date_get_month() + 1
        if(month > 12):
            month = 1
            year = self.date_get_year()+1
        else:
            year = self.date_get_year()
        day = self.months[self.date_get_month()]
        return create_date(day,month,year)
    
        
    def date_is_bigger(self,date2):
        if(self.date_get_year() > date2.date_get_year()):
            return True
        if(self.date_get_year() < date2.date_get_year()):
            return False
        if(self.date_get_month() > date2.date_get_month()):
            return True
        if(self.date_get_month() < date2.date_get_month()):
            return False
        if(self.date_get_day() > date2.date_get_day()):
            return True
        return False
    
    def date_days_between_two_dates(self,date2):
        days = 0
        if(self.date_is_bigger(date2) == True):
            return -1
        while(date2.date_get_year() != self.date_get_year()):
            days += self.days_left_in_year(date2.date_get_month()) + date2.date_get_day()
            date2.date_set_year(date2.date_get_year()-1)
            date2.date_set_month(12)
        while(date2.date_get_month() >= self.date_get_month() + 1):
            days += date2.date_get_day()
            date2.date_set_month(date2.date_get_month()-1)
            date2.date_set_day(date2.months[date2.date_get_month()])
        days += date2.date_get_day() - self.date_get_day()
        return days
        
        
        
        
class DatesClassTest(unittest.TestCase):

    """
        This function is called before any test cases.
        We can add initialization code common to all methods here 
            (e.g. reading an input file)
    """
    def setUp(self):
        self.repo = create_repository()
        self.date1 = create_date(1,1,1998)
        self.date2 = create_date(10,1,1998)

    """
        This function is called after all test function are executed
        It's like the opposite of setUp, here you dismantle the test scaffolding
    """
    def tearDown(self):
        unittest.TestCase.tearDown(self)
    
    def testdate_is_bigger(self):
        assert create_date.date_is_bigger(self.date1,self.date2) == False,1
    
    def testdate_days_between_two_dates(self):
        assert create_date.date_days_between_two_dates(self.date1,self.date2) == 9,2
        
    def testdays_left_in_year(self):
        assert create_date.days_left_in_year(self.date2,self.date2.date_get_month()) == 0,3
        
        
        
        
        
        
        
        
        
        
        
        
        