# **Data types :**

## **Numeric data Type :**
    int,float,complex

## **Sequence data Type :**
    list,tuple,range

## **String data Type :**
    string

## **Binary Type :**
    bytes, bytearray, memoryview

## **Mapping Type :**
    Dictionary

## **Boolean Type :**
    bool

## **Set Type :**
    set,frozenset

## **None Type :**
    None

### 1. **integer(int) :**

    They are often called just integers or ints, are positive or negative whole numbers with no decimal point.

    >> dir(int)

    >> output : 

       'as_integer_ratio',
       'bit_length',
       'conjugate',
       'denominator',
       'from_bytes',
       'imag',
       'numerator',
       'real',
       'to_bytes'

       1. (12.5).as_integer_ratio()
            returns the rational numbers in a tuple format. 
            returns --> (25,2)

       2. (10).bit_length
            returns the bit/binary length for the integer value.
            returns --> 4 ('b1010')

       3. (4+5j).conjugate
            returns the complex conjugate of the input number
            returns --> (4-5j)

       4. (12).denominator
            returns its lowest rational denominator value
            returns --> 1 

       5. int.from_bytes(b'\x00\x10', byteorder='big')
            16

       6. (2+3j).imag
            returns the imaginary part of the number , if not presents returns 0.
            3.0

       7. (12).numerator
            returns the numerator part of the number
            12

       8. (12+4j).real
            returns the real part of the number.
            12
          
       9. (1024).to_bytes
            (1024).to_bytes(2, byteorder='big')
            b'\x04\x00'


### 2. **Float(float) :**

    A number or a string that can be converted into a floating point number.

    >> dir(float)

    >> output :

       'as_integer_ratio',
       'conjugate',
       'fromhex',
       'hex',
       'imag',
       'is_integer',
       'real'


       1. (12.5).as_integer_ratio()
            returns the rational numbers in a tuple format. 
            returns --> (25,2)

       2. float.fromhex('0x1.8000000000000p+1')
            returns --> 3.0

       3. float.hex(3.0)
            returns --> '0x1.8000000000000p+1'

       4. (4+5j).conjugate
            returns the complex conjugate of the input number
            returns --> (4-5j)

       5. (2+3j).imag
            returns the imaginary part of the number , if not presents returns 0.
            3.0

       6. (3.0).is_integer()
            returns --> True

          (3.5).is_integer()
            returns --> False
            
       7. (12.0+5j).real
            returns the real part of the number
            12.0

          (3+6j).real
            returns --> 3.0
        

### 3. **String(str) :**

    The _str()_ function converts the specified value into a string.

    >> dir(str)

    >> output :

       'capitalize',
       'casefold',
       'center',
       'count',
       'encode',
       'endswith',
       'expandtabs',
       'find',
       'format',
       'format_map',
       'index',
       'isalnum',
       'isalpha',
       'isascii',
       'isdecimal',
       'isdigit',
       'isidentifier',
       'islower',
       'isnumeric',
       'isprintable',
       'isspace',
       'istitle',
       'isupper',
       'join',
       'ljust',
       'lower',
       'lstrip',
       'maketrans',
       'partition',
       'replace',
       'rfind',
       'rindex',
       'rjust',
       'rpartition',
       'rsplit',
       'rstrip',
       'split',
       'splitlines',
       'startswith',
       'strip',
       'swapcase',
       'title',
       'translate',
       'upper',
       'zfill'

       1. 'python'.capitalize()
            Return a capitalized version of the string, specifically makes the first character as upper case & rest will be lower case letters.
            returns --> 'Python'

       2. 'Python is programming Language'.casefold()
            Return a version of the string suitable for caseless comparisons.
            returns -->  'python is programming language'

       3. str.center(self, width, fillchar=' ', /)
            Return a centered string of length width.
            Padding is done using the specified fill character (default is a space).

            s='program'
            s.center(len(s)+4,'#')

            returns --> '##program##'

       4. str.count(substring,[start,end])
            where it returns the occurance of substring from the given string from the length of start to end.
            & start,end are optional.

            s='python'
            s.count('o')
            returns --> 1

            s.count('z')
            returns --> 0

       5. 'hi'.encode()
            Encode the string using the codec registered for encoding.
            returns --> b'hi'

           'hi'.encode(encoding='utf-16')
            returns --> b'\xff\xfeh\x00i\x00'

       6. str.endswith()
            returns a boolean value either True or False, checks the string is ends with specific character     
            which is passed as a argument in this method.

            'hi'.endswith('i')
            returns --> True

            'hi'.endswith(',')
            returns --> False

       7. str.expandtabs()
            Return a copy where all tab characters are expanded using spaces.
            If tabsize is not given, a tab size of 8 characters is assumed.

            '\t\tpython'.expandtabs(tabsize=4)
            returns --> '        python'


       8. str.find() , str.rfind()
            str.find(sub,[start,end])
                Return the lowest index in S where substring sub is found within boundary of start & end.
                if there is no substring in the boundary then it will returns -1.

                'why python'.find('y')
                    returns --> 2

            str.rfind(sub,[start,end])
                Return the highest index in S where substring sub is found within boundary of start & end.
                if there is no substring in the boundary then it will returns -1.

                'why python'.rfind('y')
                    returns --> 5

       9. str.format()
            Return a formatted version of S, using substitutions from args and kwargs.
            The substitutions are identified by braces ('{' and '}').

            s='python'
            print("i love {} programming".format(s))

            returns --> i love python programming


       10. str.format_map()
            Return a formatted version of S, using substitutions from mapping.
            The substitutions are identified by braces ('{' and '}').

            point = {'x':4,'y':-5}
            print('{x} {y}'.format_map(point))

            returns --> 4 -5

            point = {'x':4,'y':-5, 'z': 0}
            print('{x} {y} {z}'.format_map(point))

            returns --> 4 -5 0

       11. str.index() , str.rindex()

            str.index(sub,[start,end])
                Return the lowest index in S where substring sub is found,such that sub is contained within 
                S[start:end] , if not found then raises valueerror.

                'python'.index('t')
                    returns --> 2

                'python'.index('m')
                    returns --> ValueError: substring not found

            str.rindex(sub,[start,end])
                Return the highest index in S where substring sub is found,such that sub is contained within 
                S[start:end] , if not found then raises valueerror.

                'pythont'.rindex('t')
                    returns --> 6

                'python'.rindex('m')
                    returns --> ValueError: substring not found



       12. s= 'Python123@#$'
           s.isalnum() # checks whether all characters in a string is numbers or not
             returns --> False

           s.isalpha() # checks whether all characters in a string is alphabets or not
             returns --> False

           s.isascii() # checks whether all characters in a string is ASCII character or not
             returns --> False

           s.isdecimal() # checks whether all characters in a string is decimal  or not
             returns --> False

           s.isdigit() # checks whether all characters in a string is digits or not
             returns --> False

           s.isidentifier() # checks whether the given string is identifier/keyword in a python
             returns --> False

           s.islower() # checks whether all characters in a string is lowercase character or not
             returns --> False

           s.isnumeric() # checks whether all characters in a string is numbers or not
             returns --> False

           s.isprintable() # checks whether all characters in a string is printable or not
             returns --> True

           s.isspace() # checks whether string is space only or not
             returns --> False

           s.istitle() # checks whether string is titled or not
             returns --> True

           s.isupper() # checks whether string contains all upper case letters
             returns --> False


       13. str.join()
             str.join(iterable)
             Concatenate any number of strings.
             The string whose method is called is inserted in between each given string.The result is returned 
             as a new string.
             Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'

             s='a'
             s.join(['1','2','3']) 
             returns --> '1a2a3'


       14. str.ljust() and str.rjust()
              str.ljust(width,fillchar=' ')
                  returns a left-justified string of length width,padding a specified character.

              str.rjust(width,fillchar=' ')
                  Return a right-justified string of length width.

               s='Python'
               length = len(s)
               print(s.ljust(length+4,'$'))
               print(s.rjust(length+4,'$'))

               returns -->
                  'Python$$$$'
                  '$$$$Python' 

       16. str.lower() and str.upper()
              str.lower()
                  returns all the characters in a string into lowercase.
               
              str.upper()
                  returns all characters in a string into upper case.

              s= 'Python'
              print(s.lower())
                    returns --> 'python'
              print(s.upper())
                    returns --> 'PYTHON'

       17. str.lstrip() , str.rstrip() , str.strip()
              str.lstrip()
                  Return a copy of the string with leading whitespace removed.
                  If chars is given and not None, remove characters in chars instead

                  s1 = ' python '
                  s2 = '$python$'
                  s1.lstrip()
                      returns --> 'python '
                  s2.lstrip()
                      returns --> 'python$'

              str.rstrip()
                  Return a copy of the string with trailing whitespace removed.
                  If chars is given and not None, remove characters in chars instead

                  s1 = ' python '
                  s2 = '$python$'
                  s1.rstrip()
                      returns --> ' python'
                  s2.rstrip()
                      returns --> '$python'

              str.strip()
                  Return a copy of the string with leading & trailing whitespace removed.
                  If chars is given and not None, remove characters in chars instead

                  s1 = ' python '
                  s2 = '$python$'
                  s1.strip()
                      returns --> 'python'
                  s2.strip()
                      returns --> 'python'


       18. str.maketrans()
               Python string method maketrans() returns a translation table that maps each character in the   
               intabstring into the character at the same position in the outtab string. Then this table is   
               passed to the translate() function.

               x = 'aeiou'
               y = '12345'
               s = 'python is abcd'
               print(s.translate(''.maketrans(x,y)))

               returns --> 'pyth4n 3s 1bcd'

       19. str.partition() , str.rpartition()

            str.partition()
               Partition the string into three parts using the given separator.
               This will search for the separator in the string.  If the separator is found,
               returns a 3-tuple containing the part before the separator, the separator
               itself, and the part after it.
               If the separator is not found, returns a 3-tuple containing the original string
               and two empty strings. 

               'python'.partition('t')
                    returns --> ('py','t','hon')

               '123'.partition('3')
                    returns --> ('12','3','')


            str.rpartition()
               Partition the string into three parts using the given separator.
               This will search for the separator in the string, starting at the end. If the separator is 
               found, returns a 3-tuple containing the part before the
               separator, the separator itself, and the part after it.
               If the separator is not found, returns a 3-tuple containing two empty strings 
               and the original string. 

               'pythotn'.rpartition('t')
                    returns --> ('pytho', 't', 'n')

               '123'.partition('1')
                    returns --> ('', '1', '23')


       20. str.replace()
               str.replace(old, new, count=-1,)
                   Return a copy with all occurrences of substring old replaced by new.
               count
                   Maximum number of occurrences to replace.
                   -1 (the default value) means replace all occurrences.
               If the optional argument count is given, only the first count occurrences are replaced.

               'python'.replace('t','u')
                    returns --> 'pyuhon'

               'pythontea'.replace('t','x',1)
                    returns --> 'pyxhontea'

               
       21. str.rsplit() , str.split()
               str.rsplit(sep=None, maxsplit=-1)
                    Return a list of the words in the string, using sep as the delimiter string.
    
                    sep
                      The delimiter according which to split the string.
                      None (the default value) means split according to any whitespace,and discard empty
                      strings from the result.

                    maxsplit
                      Maximum number of splits to do, -1 (the default value) means no limit.

               s='hi, hello howAreYou?'
               s.rsplit(' ')
                    returns --> ['hi,', 'hello', 'howAreYou?']


               str.split(sep=None, maxsplit=-1)
                    Return a list of the words in the string, using sep as the delimiter string.
    
                    sep
                      The delimiter according which to split the string.
                      None (the default value) means split according to any whitespace,and discard empty 
                      strings from the result.
                    maxsplit
                      Maximum number of splits to do, -1 (the default value) means no limit.

               s='hi, hello howAreYou?'
               s.rsplit(' ')
                    returns --> ['hi,', 'hello', 'howAreYou?']

       22. str.splitlines()
               Return a list of the lines in the string, breaking at line boundaries.

               s='hi\n how\n are\n'
               s.splitlines()

                    returns --> ['hi', ' how', ' are']

          
       23. str.startswith()
               S.startswith(prefix[, start[, end]]) -> bool
               Return True if S starts with the specified prefix, False otherwise.
               With optional start, test S beginning at that position.
               With optional end, stop comparing S at that position.
               prefix can also be a tuple of strings to try.

               s='python'
               s.startswith('p')
                    returns --> True
               
               s.startswith('t')
                    returns --> False

       24. str.swapcase()
               Convert uppercase characters to lowercase and lowercase characters to uppercase.

               s='PyThoN'
               s.swapcase()
                    returns --> 'pYtHOn'

       25. str.title()
               Return a version of the string where each word is titlecased.
               More specifically, words start with uppercased characters and all remaining cased characters 
               have lower case.

               s='python is a language'
               s.title()
                    returns --> 'Python Is A Language'

       26. str.zfill()
               str.zfill(width)
                    Pad a numeric string with zeros on the left, to fill a field of the given width.The string 
                    is never truncated.

               s = 'python'
               s.zfill(len(s)+2)
                    returns --> '00python'



### 4. **List(list) :** 

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


### 5. **Tuple(tuple) :**

    A tuple is another container. It is a data type for immutable ordered sequences of elements. 
    Immutable because you can’t add and remove elements from tuples, or sort them in place.

    > dir(tuple)
    > Output :
        count
        index


### 6. **Dictionary(dict) :**

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

### 7. **Set(set) :**

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

