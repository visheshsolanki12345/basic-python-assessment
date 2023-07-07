
"""
=============================== Start Q 1 ======================================
Q.1 What is a lambda function in Python, and how does it differ from a regular function?
Ans =>
    A lambda function is an anonymous function,
    and How is the different from regular function, if we have small task like in one line we can use lambda
    if we have big code of line then we use normal function
    lambda like: 
                sum_num = lambda  x : x
                print(sum_num(5))
================================ End Q 1 ========================================


=============================== Start Q 2 ======================================
Q.2 Can a lambda function in Python have multiple arguments? If yes, how can you define and use
    them?
Ans =>
    lambda like: 
        sum_num = lambda  x, y : x + y
        print(sum_num(5, 5))
================================ End Q 2 ========================================


=============================== Start Q 3 ======================================
Q.3 How are lambda functions typically used in Python? Provide an example use case.
    them?
Ans =>
    In Python, we generally use Lambda Functions as an argument to a higher-order function.
    numbers = [1, 2, 3, 4, 5]
    lab_func = filter(lambda x: x > 2, numbers) 
    print(list(lab_func))
================================ End Q 3 ========================================


=============================== Start Q 4 ======================================
Q.4 What are the advantages and limitations of lambda functions compared to regular functions in
    Python?
Ans =>
    lambda function can be immediately passed and no variable needed also readable,
    regular can be long and not readable and take much heep space that is not good.
================================ End Q 4 ========================================


=============================== Start Q 5 ======================================
Q.5 Are lambda functions in Python able to access variables defined outside of their own scope?
    Explain with an example.
Ans =>
    No.
================================ End Q 5 ========================================


=============================== Start Q 6 ======================================
Q.6 Write a lambda function to calculate the square of a given number.
Ans =>
    suqare = lambda x : x ** 2 
    print(suqare(10))
================================ End Q 6 ========================================


=============================== Start Q 7 ======================================
Q.7 Create a lambda function to find the maximum value in a list of integers.
Ans =>
    min_find = lambda x : max(x)
    print(min_find([1, 2, 3]))
================================ End Q 7 ========================================



=============================== Start Q 7 ======================================
Q.7 Implement a lambda function to filter out all the even numbers from a list of integers.
Ans =>
    data = [1, 2, 3, 4, 5, 6]
    min_find = list(filter(lambda x : x%2 == 0, data))
    print(min_find)
================================ End Q 7 ========================================


=============================== Start Q 8 ======================================
Q.8 Write a lambda function to sort a list of strings in ascending order based on the length of each
    string.
Ans =>
    data = ["abde", "a", "ex","abc"]
    min_find = sorted(data, key=lambda x : len(x))
    print(min_find)
================================ End Q 8 ========================================


=============================== Start Q 9 ======================================
Q.9 Create a lambda function that takes two lists as input and returns a new list containing the
    common elements between the two lists.
Ans =>
    new_list = lambda x,y : x + y
    print(new_list([1, 2], [1, 2, 3, 4]))
================================ End Q 9 ========================================


=============================== Start Q 10 ======================================
Q.10 Write a recursive function to calculate the factorial of a given positive integer.
Ans =>
    def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)
    result = factorial(5)
    print(result)
================================ End Q 10 ========================================



=============================== Start Q  ======================================
Q.11 Implement a recursive function to compute the nth Fibonacci number.
Ans =>
    def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)
    result = fibonacci(6)
    print(result)
================================ End Q 11 ========================================


=============================== Start Q 12 ======================================
Q12 Create a recursive function to find the sum of all the elements in a given list.
Ans =>
    def list_sum(lst):
    if not lst:
        return 0
    else:
        return lst[0] + list_sum(lst[1:])
    result = list_sum([1, 2, 3, 4, 5])
    print(result)
================================ End Q 12 ========================================


=============================== Start Q 13 ======================================
Q.13 Write a recursive function to determine whether a given string is a palindrome.
Ans =>
    def is_palindrome(string):
    if len(string) <= 1:
        return True
    if string[0] == string[-1]:
        return is_palindrome(string[1:-1])
    else:
        return False
    result = is_palindrome("ineuron")
    print(result)
================================ End Q 13 ========================================


=============================== Start Q 14 ======================================
Q.14 Write a recursive function to determine whether a given string is a palindrome.
Ans =>
    def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
    result = gcd(60, 12)
    print(result)
================================ End Q 14 ========================================

"""
