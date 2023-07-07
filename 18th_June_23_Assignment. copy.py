
"""

=============================== Start Q 1 ======================================
Q.1 What is the role of the 'else' block in a try-except statement? Provide an example
    scenario where it would be useful.
Ans =>
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("it cannot divide by 0")
    else:
        print(result)
================================ End Q 1 ========================================

=============================== Start Q 2 ======================================
Q.2 Can a try-except block be nested inside another try-except block? Explain with an
    example.
Ans =>
    try:
        first = 10
        second = 0
        try:
            print(first / second)
        except ZeroDivisionError:
            print("Cannot divide by zero in the inner try block")
    except ValueError:
        print("please enter a valid integer in the outer try block")

================================ End Q 2 ========================================


=============================== Start Q 3 ======================================
Q.3 How can you create a custom exception class in Python? Provide an example that
    demonstrates its usage.
Ans =>
    class CustomException(Exception):
        def __init__(self, message):
            self.message = message

        def __str__(self):
            return f"Custom Exce {self.message}"


        def divide_two_numbers(first, second):
            try:
                if first == 0:
                    raise CustomException("Cannot divide with zero")
                print(first / second)
            except CustomException as e:
                print(e)

    divide_two_numbers(10, 0)

    summery:
        In the above code, we define a custom exception class named CustomException that inherits from the base Exception class. The CustomException class has an __init__ method to initialize the exception with a custom error message and a __str__ method to provide a string representation of the exception.

        Inside the divide_two_numbers function, we check if the first is zero. If it is, we raise an instance of the CustomException class with the corresponding error message. The raised exception is then caught in the except block and the error message is printed.
================================ End Q 3 ========================================



=============================== Start Q 4 ======================================
Q.4 What are some common exceptions that are built-in to Python?
Ans =>
    SyntaxError, IOError, AttributeError, MemoryError, ValueError and more etc.
================================ End Q 4 ========================================


=============================== Start Q 5 ======================================
Q.5 What is logging in Python, and why is it important in software development?
Ans =>
    We can get info through by logging  like warnings, errors, and other
    1. Debugging 
    2. Troubleshooting
    3. Collect info from servers or system
    4. For Enhance our application ETC.
================================ End Q 5 ========================================


=============================== Start Q 6 ======================================
Q.6 Explain the purpose of log levels in Python logging and provide examples of when
    each log level would be appropriate.
Ans =>
    We can get info through by logging  like warnings, errors, and other
    We have log levels like:
        DEBUG : For Printing variable values, function call details, or detailed flow information.
        INFO : Startup messages, configuration details, or high-level progress updates.
        WARNING : incorrect function calls.
        ERROR : Exception handling with detailed error messages
        CRITICAL : Unrecoverable errors,
================================ End Q 6 ========================================



=============================== Start Q 7 ======================================
Q.7 What are log formatters in Python logging, and how can you customise the log
    message format using formatters?
Ans =>
    import logging
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler = logging.FileHandler("site.log")
    logger = logging.getLogger("site_logger")
     logger.addHandler(file_handler)
    logger.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.debug("This is a debug message.")
    logger.info("This is an informational message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
    logger.critical("This is a critical message.")
================================ End Q 7 ========================================


=============================== Start Q 8 ======================================
Q.8 What are log formatters in Python logging, and how can you customise the log
    message format using formatters?
Ans =>
    import logging
    logger1 = logging.getLogger("module1")
    logger2 = logging.getLogger("module2")
    file_handler = logging.FileHandler("app.log")
    console_handler = logging.StreamHandler()
    logger1.addHandler(file_handler)
    logger2.addHandler(file_handler)
    logger2.addHandler(console_handler)
    logger1.setLevel(logging.INFO)
    logger2.setLevel(logging.DEBUG)
    logger1.setLevel(logging.INFO)
    logger2.setLevel(logging.DEBUG)
================================ End Q 8 ========================================



=============================== Start Q 9 ======================================
Q.8 What is the difference between the logging and print statements in Python? When
    should you use logging over print statements in a real-world application?
Ans =>
    print statements are typically used for immediate output , statement outputs messages to the standard output 
    Debugging and Troubleshooting: 
        Logging is better for debugging.
    
    Runtime Control:
        logging allows you to fine-tune the amount of information emitted at runtime
    
    Flexibility:
         Logging provides more flexibility in terms of output destinations
================================ End Q 9 ========================================


=============================== Start Q 10 ======================================
Q.10 Write a Python program that logs a message to a file named "app.log" with the
    following requirements:
    ● The log message should be "Hello, World!"
    ● The log level should be set to "INFO."
    ● The log file should append new log entries without overwriting previous ones.
Ans =>
    import logging
    logging.basicConfig(filename="app.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    logging.info("Hello, World!")
================================ End Q 10 ========================================



=============================== Start Q 11 ======================================
Q.11 Create a Python program that logs an error message to the console and a file named
    "errors.log" if an exception occurs during the program's execution. The error
    message should include the exception type and a timestamp.
Ans =>
    import logging
    import datetime
    logging.basicConfig(filename="errors.log", level=logging.ERROR,
                        format="%(asctime)s - %(levelname)s - %(message)s")
    try:
        result = 10 / 0 
    except Exception as e:
        error_msg = f"{type(e).__name__} occurred {datetime.datetime.now()}: {str(e)}"
        logging.error(error_msg)
        print(error_msg)
================================ End Q 11 ========================================
"""
