
"""
            Basic Python Assessment 2 by visheshsolanki12345@gmail.com

================================ Start Q 1 ====================================
Q.1 What are the two values of the Boolean data type? How do you write them?
Ans =>
    The two values are True And False,
    and we define like 
    course_enrolled = True
    course_not_enrolled = False
================================ End Q 1 ======================================


================================ Start Q 2 ====================================
Q.2 What are the three different types of Boolean operators?
Ans => The three different types of Boolean operators 
    1. and
    2. or
    3. not in
================================ End Q 2 ======================================


================================ Start Q 3 ====================================
Q.3 Make a list of each Boolean operator&#39;s truth tables
Ans => 
    should_be_all_true = [2 > 1, 'ram' == 'ram', 5 < 10 ]
================================ End Q 3 ======================================


================================ Start Q 4 ====================================
Q.4 What are the values of the following expressions?
    1. (5 > 4) and (3 == 5)
    2. not (5 > 4)
    3. (5 > 4) or (3 == 5)
    4. not ((5 > 4) or (3 == 5))
    5. (True and True) and (True == False)
Ans => 
    1. False
    2. False
    3 True
    4. False
    5. False
================================ End Q 4 ======================================



================================ Start Q 5 ====================================
Q.5 What are the six comparison operators?
Ans => 
    1. >
    2. <
    3. ==
    4. >=
    5. <=
================================ End Q 5 ======================================


================================ Start Q 6 ====================================
Q.6 How do you tell the difference between the equal to and assignment operators?Describe a
condition and when you would use one.
Ans => 
    The difference between the equal to and assignment operators is that assignment can be a variable and equal is what we use for cooperation,
    
    Ex. Assignment:-
        name = "Manish"
        we use for assign value into the variable 

    Ex. Operators:-
        check_condition = (1 == 10)
        We use it when we need to check that both conditions are having a match
    
================================ End Q 6 ======================================



================================ Start Q 7 ====================================
Q.7 Identify the three blocks in this code:
Ans => 
    spam = 0
    if spam == 10:
        print("eggs")
    if spam > 5:
        print("bacon")
    else:
        print('ham')
        print('spam')
        print('spam')
================================ End Q 7 ======================================


================================ Start Q 8 ====================================
Q.8 Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints
Greetings! if anything else is stored in spam.
Ans => 
    spam = 2
    if spam == 1:
        print("Hello")
    elif spam == 2:
        print("Howdy")
    else:
        print("Greetings!")
================================ End Q 8 ======================================


================================ Start Q 9 ====================================
Q.9 If your programme is stuck in an endless loop, what keys you’ll press?
Ans => 
    If we programme is stuck in an endless loop we can use Control+C 
================================ End Q 9 ======================================


================================ Start Q 10 ====================================
Q.10 How can you tell the difference between break and continue?
Ans => 
    First fall break and continue we use with for loop or while loop 
    Break :-
        if we want to break loop we can write break,
    Continue :-
        If we have condition in the loop and we want to skip if condition match then we can use continue, program will not go inside of the condition. 
================================ End Q 10 ======================================


================================ Start Q 11 ====================================
Q.11 In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?
Ans => 
    range(10) :-
        This will give us range object from 0 to 9 becurse initial first argument does 0.
    range(0, 10) :-
        This will give us range object from 0 to 9, 0 is from where we want to start the range.
    range(0, 10, 1) :-
        This will be start from 0 and will go till 9 and will use pair 1 that is already given us by python.
================================ End Q 11 ======================================



================================ Start Q 12 ====================================
Q.12 Write a short program that prints the numbers 1 to 10 using a for loop. Then write an    equivalent, program that prints the numbers 1 to 10 using a while loop.
Ans => 
    With for loop :-
        for i in range(1, 11):
            print(i)

    With while loop :-
        i = 1
        while i < 11:
            print(i)
            i += 1
    
================================ End Q 12 ======================================


================================ Start Q 13 ====================================
Q.13 If you had a function named bacon() inside a module named spam, how would you call it after
importing spam?
Ans => 
    from spam import bacon
    call_becon = bacon()
    print(call_becon)
================================ End Q 13 ======================================

"""



    
