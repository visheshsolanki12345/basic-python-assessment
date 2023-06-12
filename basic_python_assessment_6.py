
"""
            Basic Python Assessment 6 by visheshsolanki12345@gmail.com

=============================== Start Q 1 ======================================
Q.1 What are keywords in python? Using the keyword library, print all the python keywords.
Ans =>
    Python keywords likes specific functions, There are 35 keywords in Python.
    import keyword
    print(keyword.kwlist)
================================ End Q 1 ========================================


=============================== Start Q 2 ======================================
Q.2 What are the rules to create variables in python?
Ans =>
    Variable should  not be starting as number or special character.
================================ End Q 2 ========================================


=============================== Start Q 3 ======================================
Q.3 What are the standards and conventions followed for the nomenclature of variables in
    python to improve code readability and maintainability?
Ans =>
    Variable should be start small letter and if we have long word as name conventions then we can use '_' to join that variable name like vishesh_solanki = '23 years'
================================ End Q 3 ========================================


=============================== Start Q 4 ======================================
Q.4 What will happen if a keyword is used as a variable name?
Ans => 
    That can be python keyword override so we won't be able to take advantage inbuilt function of python.
================================ End Q 4 ========================================


=============================== Start Q 5 ======================================
Q.5 For what purpose def keyword is used?
Ans => 
    def used for define function.
================================ End Q 5 ========================================


=============================== Start Q 6 ======================================
Q.6 What is the operation of this special character ‘\’?
Ans => 
    In Python strings, the backslash "\" is a special character, also called the "escape" character. It is used in representing certain whitespace characters: "\t" is a tab, "\n" is a newline, and "\r" is a carriage return. Conversely, prefixing a special character with "\" turns it into an ordinary character.
================================ End Q 6 ========================================


=============================== Start Q 7 ======================================
Q.7 Give an example of the following conditions:
    (i) Homogeneous list
    (ii) Heterogeneous set
    (iii) Homogeneous tuple
Ans => 
    (i) Homogeneous list
        homogeneous_list = [1, 2, 3]
    (ii) Heterogeneous set
        heterogeneous_set = {1, 2, 3}
    (iii) Homogeneous tuple
        homogeneous_tuple = (1, 2, 3)
================================ End Q 7 ========================================


=============================== Start Q 8 ======================================
Q.8 Explain the mutable and immutable data types with proper explanation & examples.
Ans => 
    Mutable data type like we can modify or change data and immutable we cannot do change data
    Example :-
        Mutable
            list_fruits = ["apple"]
            list_fruits.append("mango")
            => in new list will be contain ["apple", "mango"]
        immutable
            tuple_fruits = ("apple")
            => Now we can't add "mango" in tuple_fruits
================================ End Q 8 ========================================


=============================== Start Q 9 ======================================
Q.9 Write a code to create the given structure using only for loop.
        *
       ***
      *****
     *******
    *********
Ans => 
    user_input = 10
    loop_list = list(range(1, user_input)).reverse()
    import math
    half = math.floor((user_input - 1) / 2)
    space = " "
    for i in range(1, half + 2):
        print(f"{space * half}{('*'*(i+i-1))}{space*half}")
        half -= 1
================================ End Q 9 ========================================


=============================== Start Q 10 ======================================
Q.10 Write a code to create the given structure using while loop.
    |||||||||
     |||||||
      |||||
       |||
        |
Ans => 
    user_input = 10
    loop_list = list(range(1, user_input)).reverse()
    import math
    half = 0
    space = " "
    revers_loop  = list(range(1, math.floor((user_input - 1) / 2) + 2))
    revers_loop.reverse()
    
    while half < len(revers_loop):
        print(f"{space * half}{('|'*(revers_loop[half]+revers_loop[half]-1))}{space*half}")
        half += 1
=============================== Start Q 10 ======================================

"""
