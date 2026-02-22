###########         Functions and Recursions        ##############

### Functions
#Functions is a block of statements that perform a specific task.
# def func_name(param1, param2, ...):
#     # function body
#     return value
#func_name(arg1, arg2, ...)

def sum(a, b):  # a & b are parameters of the function
    s = a + b
    return s
print(sum(2, 3))    # function call with arguments 2 and 3, will print the return value of the function


def print_hello():
    print("Hello")

print_hello()   # how many times we call the function, it will print "Hello" that many times
print_hello()
print_hello()
print_hello()   # will print "Hello"


# Practise Questions
# WAP tp print the elements of list in the same line
heroes = ["Superman", "Batman", "Spiderman", "Wonder woman"]
def print_list(lst):
    for el in lst:
        print(el, end=" ")
    print()  # Print a newline after the list elements

print_list(heroes)

# WAP to find the factorial of a number n
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

factorial(4)

# WAP to convert USD to INR
def calc_conv(usd):
    inr = usd * 90.72
    print(usd, "USD =", inr, "INR")

calc_conv(100)

#WAP to check if number is even or not
def number(n):
    if n % 2 == 0:
        print(n, "is even")
    else:
        print(n, "is odd")

number(5)
number(6)


### Recursions
# When a function calls itself repeatedly until a base condition is met, it is called recursion.
def show(n):
    if(n == 0):   #base condition to stop the recursion
        return
    print(n)
    show(n-1)

show(5)  

# Recurence relation
def fact(n):
    if(n == 0 or n == 1):   #base condition to stop the recursion
        return 1
    return n * fact(n-1)
print(fact(5))

# Practise Questions
#WAP a recursive function to calculate the sum of first n natural numbers
def sum_natural(n):
    if n == 0:
        return 0
    return n + sum_natural(n-1)
print(sum_natural(5))
