# Python Programs

# List 

    A list is defined using square brackets and holds data that is separated by commas. The list is mutable and ordered. 
    It can contain a mix of different data types.

    > dir(list)
    > Output : 
        append
        clear
        copy
        count
        extend
        index
        insert
        pop
        remove
        reverse
        sort


# Tuple

    A tuple is another container. It is a data type for immutable ordered sequences of elements. 
    Immutable because you can’t add and remove elements from tuples, or sort them in place.

    > dir(tuple)
    > Output :
        count
        index


# Dictionary

    Dictionary is a mutable and unordered data structure. It permits storing a pair of items (i.e. keys and values).
    As the example below shows, in the dictionary, it is possible to include containers into other containers to create compound 
    data structures.

    > dir(dict)
    > Output :
        clear
        copy
        fromkeys
        get
        items
        keys
        pop
        popitem
        setdefault
        update
        values

# Set

    Set is a mutable and unordered collection of unique elements. It can permit us to remove duplicate quickly from a list.

    > dir(set)
    > Output:
        add
        clear
        copy
        difference
        difference_update
        discard
        intersection
        intersection_update
        isdisjoint
        issubset
        issuperset
        pop
        remove
        symmetric_difference
        symmetric_difference_update
        union
        update


# String
    The str() method will converts the specified value into a string.

    > dir(str)
    > Output :
        capitalize
        casefold
        center
        count
        encode
        endswith
        expandtabs
        find
        format
        format_map
        index
        isalnum
        isalpha
        isascii
        isdecimal
        isdigit
        isidentifier
        islower
        isnumeric
        isprintable
        isspace
        istitle
        isupper
        join
        ljust
        lower
        lstrip
        maketrans
        partition
        replace
        rfind
        rindex
        rjust
        rpartition
        rsplit
        rstrip
        split
        splitlines
        startswith
        strip
        swapcase
        title
        translate
        upper
        zfill

# File operations

    File related operations achieved with help of python . like reading,writing,appending to file.

# OOP's concept based

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

# Daily_coding_problems

    Please subscribe to the below link by providing your gmail Id to get problems everyday which were asked in the interview    
    from Big MNC/product companies.

    link : https://www.dailycodingproblem.com/

   
# CodingBat Programs

    Please sign up or login with your account & try to solve the program questions which were thrown on the webpage link.
    link : https://codingbat.com/python 


# CodeSignal app Python challenges 

    Please sign up or login with your account/gmail id & try to solve the interview coding questions about each topics.
    link : https://codesignal.com/developers/interview-practice/


# Adhoc_Programs

    Adhoc questions will be taken & solved from different websites/persons/interview process.


# Python Packages

    Working on Programs which is developed using different python packages rather than builtin/basic packages.

    * Selenium
    * PySimpleGUI
    * BeautifulSoup
