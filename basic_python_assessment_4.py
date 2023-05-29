
"""
            Basic Python Assessment 4 by visheshsolanki12345@gmail.com

=============================== Start Q 1 ======================================
Q.1 What exactly is []?
Ans =>
    This [] represent list in python. 
================================ End Q 1 ========================================


=============================== Start Q 2 ======================================
Q.2 In a list of values stored in a variable called spam, how would you assign the value 'hello' as the third value? (Assume [2, 4, 6, 8, 10] are in spam.)
Ans =>
    spam = [2, 4, 6, 8, 10]
    spam.insert(2, "hello")
    print(spam)
================================ End Q 2 ========================================


=============================== Start Q 3 ======================================
Q.3 What is the value of spam[int(int('3' * 2) / 11)]?
Ans =>
    spam = ['a', 'b', 'c', 'd']
    spam[int(int('3' * 2) / 11)]
    The output will be (d) because in the spam (d) exists 3 index
================================ End Q 3 ========================================


=============================== Start Q 4 ======================================
Q.4 What is the value of spam[-1]?
Ans =>
    spam = ['a', 'b', 'c', 'd']
    The output will be (d) because in the spam (d) exists 1 index from the last
================================ End Q 4 ========================================


=============================== Start Q 5 ======================================
Q.5 What is the value of spam[:2]?
Ans =>
    spam = ['a', 'b', 'c', 'd']
    The output will be getting from index 0 to index 1 in the spam
    output will be = ['a', 'b'] 
================================ End Q 5 ========================================

=============================== Start Q 6 ======================================
Q.6 What is the value of bacon.index('cat')?
Ans =>
    bacon = [3.14, 'cat', 11, 'cat', True]
    bacon.index('cat')
    Output will be (1) because 'cat' is in bacon 1 index 
================================ End Q 6 ========================================


=============================== Start Q 7 ======================================
Q.7 How does bacon.append(99) change the look of the list value in bacon?
Ans =>
    bacon = [3.14, 'cat', 11, 'cat', True]
    bacon.append(99)
    new_bacon = [3.14, 'cat', 11, 'cat', True, 99]
================================ End Q 7 ========================================


=============================== Start Q 8 ======================================
Q.8 How does bacon.remove('cat') change the look of the list in bacon?
Ans =>
    bacon = [3.14, 'cat', 11, 'cat', True]
    bacon.remove("cat")
    First ('cat') will be removed from the bacon
    new_bacon = [3.14, 11, 'cat', True]
================================ End Q 8 ========================================


=============================== Start Q 9 ======================================
Q.9 What are the list concatenation and list replication operators?
Ans =>
    List concatenation like concat 2 list and return new list
================================ End Q 9 ========================================


=============================== Start Q 10 ======================================
Q.10 What is difference between the list methods append() and insert()?
Ans =>
    The difference between the list methods append() and insert() 
    append() :-
        append methods do add new element in the list at the last position,
    insert() :-
        insert methods do add new element in the list according to index we need to pass 2 argument inside of (insert) first does index and second does value. 

================================ End Q 10 ========================================


=============================== Start Q 11 ======================================
Q.11 What are the two methods for removing items from a list?
Ans =>
    bacon = [3.14, 'cat', 11, 'cat', True]
    
    1 remove() :-
        bacon.remove('cat')
        after_remove_func_bacon = [3.14, 11, 'cat', True]

    2 pop() :-
        bacon.pop()
        after_use_del_bacon = [3.14, 'cat', 11, 'cat']
        pop method delete item from last in the list and return delete item value

================================ End Q 11 ========================================



=============================== Start Q 12 ======================================
Q.12 Describe how list values and string values are identical.
Ans =>
    In string we write under double code and integer we write without double code.
    so we can say easily where we see in the list under double code values those are string, and without double code values are integer values .
    
================================ End Q 12 ========================================

=============================== Start Q 13 ======================================
Q.13 What's the difference between tuples and lists?
Ans =>
    List is mutable and tuple is not mutable.
================================ End Q 13 ========================================


=============================== Start Q 14 ======================================
Q.14 How do you type a tuple value that only contains the integer 42?
Ans =>
    a_number = (22,)
    print(a_number)
================================ End Q 14 ========================================


=============================== Start Q 15 ======================================
Q.15 How do you get a list value's tuple form? How do you get a tuple value&#39;s list form?
Ans =>
    tuple to list :-
        tuple_number = (22, 10, 30)
        list_number = list(tuple_number)
        print(list_number)
    
    list to tuple :-
        list_number = [22, 10, 30]
        tuple_number = list(list_number)
        print(tuple_number)
================================ End Q 15 ========================================


=============================== Start Q 16 ======================================
Q.16 Variables that 'contain' list values are not necessarily lists themselves. Instead, what   do they contain?
Ans =>
    They can contain float or string or integer
================================ End Q 16 ========================================


=============================== Start Q 17 ======================================
Q.17 How do you distinguish between copy.copy() and copy.deepcopy()?
Ans =>
    Copy() create reference to original object. If you change copied object you change the original object, deepcopy() creates new object and does real copying of original object to new one.
================================ End Q 17 ========================================
"""

