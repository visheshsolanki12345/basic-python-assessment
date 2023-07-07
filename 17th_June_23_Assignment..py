
"""

=============================== Start Q 1 ======================================
Q.1 What is the role of try and exception block?
Ans =>
    If we know our program may get stuck somewhere then we write that code inside of try block if all good try block will run otherwise we will get exception,
================================ End Q 1 ========================================


=============================== Start Q 2 ======================================
Q.2 What is the syntax for a basic try-except block?
Ans =>
    try:
        print("code run")
    except Exception as e:
        print("Error is", e)
================================ End Q 2 ========================================


=============================== Start Q 3 ======================================
Q.3 What happens if an exception occurs inside a try block and there is no matching
    except block?
Ans =>
    If an exception occurs inside a try block in Python and there is no matching except block to handle that exception, the program will terminate abruptly and an error message called an "unhandled exception" will be displayed. 
================================ End Q 3 ========================================


=============================== Start Q 4 ======================================
Q.4 What is the difference between using a bare except block and specifying a specific
    exception type?
Ans =>
    A bare except block is written as except: without specifying any exception type. It is a generic exception handler that will catch any exception that occurs within the try block. While this approach allows you to handle any type of exception, it can also catch and handle exceptions that you may not have anticipated. 
================================ End Q 4 ========================================



=============================== Start Q 5 ======================================
Q.5 Can you have nested try-except blocks in Python? If yes, then give an example.
Ans =>
    try:
        first = 20
        second = 0
        try:
            result = first / second
            print(result)
        except ZeroDivisionError:
            print("Cannot divide by zero")
    except ZeroDivisionError:
        print("Cannot divide by zero in the outer try block")
================================ End Q 5 ========================================


=============================== Start Q 6 ======================================
Q.6 Can you have nested try-except blocks in Python? If yes, then give an example.
Ans =>
    try:
        result = 10 / 0
        print("Result1:", result)
        my_list = [1, 2, 3, 4]
        value = my_list[6]
        print("result 2", value)

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

    except IndexError:
        print("Error: Index is out of range.")

================================ End Q 6 ========================================


=============================== Start Q 7 ======================================
Q.7 Write the reason due to which following errors are raised:
    a. EOFError
    b. FloatingPointError
    c. IndexError
    d. MemoryError
    e. OverflowError
    f. TabError
    g. ValueError
Ans =>
    a. EOFError:
        This error is raised when the input() function or any other function that reads input from the user

    b. FloatingPointError:
        This error is raised when a floating-point operation encounters an exceptional condition that cannot be handled,

    c. IndexError:
        This error is raised when you try to access an index that is outside the range of valid indices  

    d. MemoryError:
        This error is raised when the program runs out of available memory to perform an operation. 
    
    e. OverflowError:
        This error is raised when the result of an arithmetic operation exceeds the maximum representable value for a numeric type.

    f. TabError:
        This error is raised when the Python interpreter encounters an indentation-related issue, 
    
    g. ValueError:
        This error is raised when a built-in operation or function receives an argument of the correct type but an invalid value.
    ================================ End Q 7 ========================================


=============================== Start Q 8 ======================================
Q.8 Write code for the following given scenario and add try-exception block to it.
    a. Program to divide two numbers
    b. Program to convert a string to an integer
    c. Program to access an element in a list
    d. Program to handle a specific exception
    e. Program to handle any exception
Ans =>
    a. Program to divide two numbers:
        try:
            result = 10 / 0
            print(result)
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")

    b. Program to convert a string to an integer:
        try:
            num = int('Ram')
            print(num)
        except ValueError:
            print("Error: Invalid input. Please enter a valid integer.")

    c. Program to access an element in a list:
        try:
            my_list = [1, 2, 3]
            value = my_list[5]
            print("result", value)
        except IndexError:
            print("Error: Index is out of range.")

    d. Program to handle a specific exception:
        try:
            print("=====run)
        except SpecificExceptionType:
            print("=====not)

    e. Program to handle any exception:
        try:
            pass
        except Exception:
            pass
    ================================ End Q 8 ========================================

"""
