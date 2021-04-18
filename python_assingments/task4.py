from functools import reduce
#Q1 Write a program to reverse a string.

#function to reverse string
def reverse(inp):
    return inp[::-1]

value = input("Enter the String: ")
print(reverse(value))

#Q2 Write a function that accepts a string and prints the number of uppercase letters and lowercase letters.

def count_case(value):
    upper, lower = 0,0
    for x in value:
        if x.isupper():
            upper+= 1
        else:
            lower+=1
    return upper, lower

value = input("Enter the String: ")
upper, lower = count_case(value)
print("No. of Uppercase characters: {}, No. of lowercase characters: {}".format(upper, lower))


#Q3 Create a function that takes a list and returns a new list with unique elements of the first list.

def fun(lst):
    unique_elements  = set(lst)
    return list(unique_elements)

print(fun([1,1,2,2,3,3,4,4,]))

#Q4 Write a program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.

def sort_alpha(words):
    lst = words.split('-')
    lst.sort()
    x = "-".join(lst)
    return x

print(sort_alpha("arjun-poudel-kumar-minebrook"))

#Q5 Write a program that accepts a sequence of lines as input and prints the lines after making all characters in the sentence capitalized.

def capitalize(lines):
    lst = [x.upper() for x in lines.split(' ')]
    x = " ".join(lst)
    return x

lines = input("Enter the sentence: ")
print(capitalize(lines))

#6 Define a function that can receive two integral numbers in string form and compute their sum and print it in the console.

def sum(a,b):
    print("Sum is: ", int(a)+int(b))

a= input("Enter  the value of A: ")
b= input("Enter the value of B: ")
sum(a, b)

'''Q7 Define a function that can accept two strings as input and print the string with the maximum length
in the console. If two strings have the same length, then the function should print both the strings line
by line.'''

def max_length(a, b):
    len_a = len(a)
    len_b = len(b)
    if len_a > len_b:
        print(a)
    elif len_b > len_a:
        print(b)
    else:
        print(a,b, end= "\n")

#user input
value = input("Enter the word: ")
value1 = input("Enter the second word: ")

max_length(value, value1)


#Q8 Define a function which can generate and print a tuple where the values are square of numbers between 1 and 20 (both 1 and 20 included).

def gen_square():
    tup = tuple(x**2 for x in range(1,21))
    print(tup)

gen_square()

#Q9 Write a function called showNumbers that takes a parameter called limit. It should print all the numbers between 0 and limit with a label to identify the even and odd numbers.

def showNumbers(limit):
    for x in range(0, limit+1):
        if x%2 == 0:
            print(x," EVEN")
        else:
            print(x," ODD")

showNumbers(3)

#Q10 Write a program which uses filter() to make a list whose elements are even numbers between 1 and 20 (both included)

even_lst = list(filter(lambda x: x%2 ==0, range(1,21)))
print(even_lst)

#Q11 Write a program which uses map() and filter() to make a list whose elements are squares of even numbers in [1,2,3,4,5,6,7,8,9,10].

even_squared = list(map(lambda x: x**2,(filter(lambda x: x%2==0, range(1,11)))))
print(even_squared)


#Q12 Write a function to compute 5/0 and use try/except to catch the exceptions

def compute():
    try:
        5/0
    except ZeroDivisionError as e:
        print("Number can't be divided by zero.", e)

compute()

#Q13 Flatten the list [1,2,3,4,5,6,7] into 1234567 using reduce().

flattten_lst = reduce(lambda x,y : str(x)+''+str(y),  range(1,8))
print(flattten_lst)

#Q14 Write a program in Python to find the values which are not divisible by 3 but are a multiple of 7. Make sure to use only higher order functions.

multiple_seven = list(filter(lambda x: x%7 == 0,(filter(lambda x: x%3 != 0, range(1,300)))))
print(multiple_seven)


#Q15 Write a program in Python to multiply the elements of a list by itself using a traditional function and pass the function to map() to complete the operation.

def multiply(x):
    return x*x

res = list(map(multiply,range(1,7)))
print(res)


#Q16 What is the output of the following codes:

# i)
# def foo():
#     try:
#         return 1
#     finally:
#         return 2
# k = foo()
# print(k)

#output : 2

# ii)

# def a():
#     try:
#         f(x, 4)
#     finally:
#         print('after f')
#         print('after f?')
# a()

#output 
'''after f
after f?
NameError: name 'f' is not defined'''