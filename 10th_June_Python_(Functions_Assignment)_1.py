
"""
=============================== Start Q 1 ======================================
Q.1 In Python, what is the difference between a built-in function and a user-defined function? Provide an
    example of each.
Ans =>
    Functions that readily comes with Python are called built-in functions.
    like 
        print("Hello")
    We can also create your own functions
    def sum_two_num(a, b):
        return a + b
================================ End Q 1 ========================================


=============================== Start Q 2 ======================================
Q.2 How can you pass arguments to a function in Python? Explain the difference between positional
    arguments and keyword arguments.
Ans =>
    A positional argument is a name that is not followed by an equal sign (=)
    like : def sum_two_num(a, b):
                return a + b
    A keyword argument is followed by an equal sign and an expression that gives its default value
    like : def sum_two(a=a, b=b):
        return a + b
================================ End Q 2 ========================================


=============================== Start Q 3 ======================================
Q.3 What is the purpose of the return statement in a function? Can a function have multiple return
    statements? Explain with an example.
Ans =>
    Whatever calculation or test  we have done inside of function, if we want to show and do something for that we use return
    def sum_two_num_and_multi(a, b):
        sum_num = a + b
        multi_num = a * b
        return sum_num, multi_num
================================ End Q 3 ========================================


=============================== Start Q 4 ======================================
Q4 What are lambda functions in Python? How are they different from regular functions? Provide an
    example where a lambda function can be useful.
Ans =>
    A lambda function is an anonymous function,
    and How is the different from regular function, if we have small task like in one line we can use lambda
    if we have big code of line then we use normal function
    lambda like: 
                sum_num = lambda  x, y : x + y
                print(sum_num(5, 5))
================================ End Q 4 ========================================


=============================== Start Q 5 ======================================
Q.5 How does the concept of "scope" apply to functions in Python? Explain the difference between local
    scope and global scope.
Ans =>
    Scope like we can say access of veritable or function, if we have veritable in side of function we can say that is local scope's function, global scope function we can use any where like in class or inside of any function,

    global_var = 10
    def test():
        local_var = 20
        return global_var + local_var
    test()
    print(local_var) // it will give an error because of this has local score
    print(global_var)
================================ End Q 5 ========================================


=============================== Start Q 6 ======================================
Q.6 How can you use the "return" statement in a Python function to return multiple values?
Ans =>
    def test():
        return [10], 1, "A"
================================ End Q 6 ========================================


=============================== Start Q 7 ======================================
Q.7 What is the difference between the "pass by value" and "pass by reference" concepts when it
    comes to function arguments in Python?
Ans =>
    When you give function parameters via reference, you are just passing references to values that already exist. When you pass arguments by value, the arguments become copy of the original value.
================================ End Q 7 ========================================


=============================== Start Q 8 ======================================
Q.8 Create a function that can intake integer or decimal value and do following operations:
    a. Logarithmic function (log x)
    b. Exponential function (exp(x))
    c. Power function with base 2 (2x)
    d. Square root
Ans =>
    import math
    a : def log(x):
            math.log(x)
    b : def exp(x):
            math.exp(x)
    c : def pow(base, x):
            math.pow(base, x)
    d : def sqrt(x):
            math.sqrt(x)
    print(log(2.0))
    print(exp(2.0))
    print(pow(base, 2.0))
    print(sqrt(2.0))
================================ End Q 8 ========================================


=============================== Start Q 9 ======================================
Q.9 Create a function that takes a full name as an argument and returns first name and last name.
Ans =>
    def name_re(name):
        return name[0], name[-1]
    first_name, last_name = name_re("ineuron")
    print(first_name)
    print(last_name)
================================ End Q 9 ========================================

"""

