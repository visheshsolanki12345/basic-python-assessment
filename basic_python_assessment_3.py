
"""
            Basic Python Assessment 3 by visheshsolanki12345@gmail.com

================================ Start Q 1 ====================================
Q.1 Why are functions advantageous to have in your programs?
Ans =>
    We have many advantageous if we you functions
    1. code quality
    2. code size reduce
    3. we can use same function if we get same problem in many places
    3. readable
================================ End Q 1 ========================================


================================ Start Q 2 ======================================
Q.2 When does the code in a function run: when it's specified or when it's called?
Ans =>
    First we need define an function then we call that function then inside of function code run. 
    def add():
        return 10 + 10
    addition = add()
    print(addition)
================================ End Q 2 ========================================


================================ Start Q 3 ======================================
Q.3 What statement creates a function?
Ans =>
    First we need to write (def) that means define function then we write function name like (add) then (colon) and then write the logic inside of (colon) and then if we want to return something we can also return by return statement

    Ex:
        def add():
            return 10 +10
        print(add())
================================ End Q 3 ========================================


================================ Start Q 4 ======================================
Q.4 What is the difference between a function and a function call?
Ans =>
    The function can be our code logic, inside of the function has code and can be any task to perform, 
    function call means whatever we have wrote the function, by call we basically execute or run that particular function.
================================ End Q 4 ========================================




================================ Start Q 5 ======================================
Q.5 How many global scopes are there in a Python program? How many local scopes?
Ans =>
    In python only one global Python scope per program execution,
    A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.
================================ End Q 5 ========================================


================================ Start Q 6 ======================================
Q.6 What happens to variables in a local scope when the function call returns?
Ans =>
    When the execution of the function terminates (returns), the local variables are destroyed.
================================ End Q 6 ========================================


================================ Start Q 7 ======================================
Q.7 What is the concept of a return value? Is it possible to have a return value in an expression?
Ans =>
    The concept of a return value when we have an function also inside of function we have calculation and if as soon as calculation has done then return give us that calculation value,
    expression :-
        def add():
            a_b = 5 + 10
            return {"add":a_b}
        call_func = add()
        call_func["minus"] = 10 - 5
        print(call_func)
================================ End Q 7 ========================================


================================ Start Q 8 ======================================
Q.8 If a function does not have a return statement, what is the return value of a call to that function?
Ans =>
    If a function does not have a return statement then function always return None 
================================ End Q 8 ========================================


================================ Start Q 9 ======================================
Q.9 How do you make a function variable refer to the global variable?
Ans =>
    def func():
        global x
        x = "hello"
    func()
    print(x)
================================ End Q 9 ========================================


================================ Start Q 10 ======================================
Q.10 What is the data type of None?
Ans =>
    The data type of None is NoneType.
================================ End Q 10 ========================================



================================ Start Q 11 ======================================
Q.11 What does the sentence import areallyourpetsnamederic do?
Ans =>
    That import statement imports a module named areallyourpetsnamederic.
================================ End Q 11 ========================================


================================ Start Q 12 ======================================
Q.12 If you had a bacon() feature in a spam module, what would you call it after importing spam?
Ans =>
    from spam import bacon
    call_func = bacon() 
    print(call_func)
================================ End Q 12 ========================================


================================ Start Q 13 ======================================
Q.13 What can you do to save a programme from crashing if it encounters an error?
Ans =>
    We use if we know may error come Try Except.
================================ End Q 13 ========================================


================================ Start Q 14 ======================================
Q.14 What is the purpose of the try clause? What is the purpose of the except clause?
Ans =>
    If we know the error may come into the program then we use (try-except) if the program runs well then (except) will not work only the program run inside of the (try) block but if the program will not run then the code run inside of (except) block.
================================ End Q 14 ========================================
"""
