# Program_1.py

# Explanation about OOP's concept : class & Object creation & class variable usage.


# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 18:56:33 2020
@author: gshambul
"""

class Employees:
    #declares your name company name here
    #class variable
    company = "@company.com"
    
    def __init__(self,first_name,last_name,middle_name,monthly_salary):
        '''
        "__init__" is a reseved method in python classes. It is known as a constructor in object oriented concepts. 
        This method called when an object is created from the class and it allow the class to initialize the attributes of a class.
        The "__init__" method of a class is used to initialize new objects, not create them. As such, it should not return any value. 
        Returning None is correct in the sense that no runtime error will occur, but it suggests that the returned value is meaningful, which it is not.
        
        Usage of "self" in class to access the methods and attributes.
        '''
        self.fname = first_name
        self.mname = middle_name
        self.lname = last_name
        self.pay = monthly_salary
        
        
    def full_name_of_emp(self):
        return (self.fname+self.mname+self.lname)
    
    def email_id(self):
        full_name = self.full_name_of_emp()
        print("Employee {}'s Monthly wage will be : {} ".format(full_name,self.pay))
        
        
        #class variables can be called by object reference/name and also with class name too
        
        #with object reference 
        #print("The Employee's company email id will be : {}".format(full_name+self.company))
        
        #class name
        print("The Employee's company email id will be : {}".format(full_name+Employees.company))
        
    
    def annual_appraisal(self):
        #assuming that every company will gives 15% of hike for an employee's annual salary 
        
        annual_salary = 12 * self.pay
        annual_appraisal_of_emp = (annual_salary * 0.15 ) + annual_salary
        print("The Employee {}'s annual appraisal will be shown with a value of amount is : {}".format(self.full_name_of_emp(),annual_appraisal_of_emp))
        
        



if __name__ == "__main__":
    print("Welcome to the main program !! ")
    count_emps = int(input("Enter the count of employess to be stored in company's list : "))
    emp_name_list = list()
    for emp in range(1,count_emps+1):
        first_name = str(input("Enter Employee {} first name here : ".format(emp)))
        middle_name = str(input("Enter Employee {} middle name here : ".format(emp)))
        last_name = str(input("Enter Employee {} last name here : ".format(emp)))
        monthly_salary = int(input("Enter Employee {} monthly salary here : ".format(emp)))
        
        Temp_full_name = first_name+middle_name+last_name
        
        if(Temp_full_name in emp_name_list):
            print("The employee name is already there in company list , so try with other name ")
            continue
        else:
            emp_name_list.append(Temp_full_name)
            Employee = Employees(first_name,last_name,middle_name,monthly_salary)
            Employee.email_id()
            Employee.annual_appraisal()
            
            
    print("Ends the main program here !!")
