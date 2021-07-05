# OOP's concepts in Python

   **The main principles in OOP(Object Oriented Programming)'s in Python language :**

   * **Class**
        * *Its a Blueprint which is followed by objects*
        * *It is logical structure with some specific attributes and methods*
        * *class is a logical entity*
        * *\_\_init__(self)* method :
          > "\_\_init__" is a reseved method in python classes. It is known as a constructor in object oriented concepts. 
          > This method called when an object is created from the class and it allow the class to initialize the attributes of a class.
          > The "\_\_init__" method of a class is used to initialize new objects, not create them. As such, it should not return any value. 
          > Returning None is correct in the sense that no runtime error will occur, but it suggests that the returned value is meaningful, which it is not.
        
          > Usage of "self" in class to access the methods and attributes.
        
   * **Object**
        * *Its an instance/reference of a class*
        * *When we define a class, it needs to create an object to allocate the memory.*
        * *it may be a real world objects like pen,car,mouse,keyboard,humans etc*
        * *Object is the physical entity*
        
   * **Abstraction**
        * *hiding the important data or implementation data* 
        * *showing the essential data*
            > Ex: we do install .exe application that is called essential data , but we dont care about implementation data that is we dont bother about the background data/process.
            
   * **Encapsulation**
        * *Binding/wrapping up the data & functions into a single entity*
        * *To achieve the encapsulation we do use access specifier:*
           - *Public:* *Datas can be accessed by any function in any class*
           - *Protected:* *Datas can be accessed by only class or class inherited* 
           - *Private:* *Datas can be accessed by only by the class*
           
   * **Inheritance**
        * *derived class inherits the properties from base class*
        * *Base class-Parent class , Derived class-child class*
        * *It provides the re-usability of the code*
        
   * **Polymorphism**
        * *Polymorphism contains two words "poly" and "morphs". Poly means many, and morph means shape*
        * *implementing the same method in different context*
            > Ex: '+' Arithematic addition , '+' string concatination
            
   * **Role of Underscore_**
        * *Please check out the webpage for easy understanding : https://www.datacamp.com/community/tutorials/role-underscore-python*


### Program_1.py

    Explanation about class variable & its usage . 

    The Program_1.py will explains us about the declaration of class variable & how we can call it within a 
    class , and also the program will shows the company's employee email id and employee salary , annual 
    appraisal value.

    
