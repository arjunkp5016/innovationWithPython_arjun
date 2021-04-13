'''Q1 Create three variables in a single line and assign values to them in such a manner that each one of
them belongs to a different data type.'''
a,b,name = 3, 2.14, "Arjun"
print(type(a))
print(type(b))
print(type(name))

#Q2 Create a variable of type complex and swap it with another variable of type integer.

complex_number = complex(2,3)
value = 3
value, complex_number = complex_number, value
print(value)
print(complex_number)

#Q3 Swap two numbers using a third variable and do the same task without using any third variable.

#using the third variable
x, y = 5, 8.2
print("Before the Swap")
print("Value of X:",x)
print("Value of Y:",y)
z = x
x = y
y = z

print("After the swap")
print("Value of X:",x)
print("Value of Y:",y)

# #without using the third variable
a,b = 4, 9.6
print("Before the Swap")
print("Value of a:",a)
print("Value of b:",b)
a,b = b,a 
print("After the swap")
print("Value of a:",a)
print("Value of b:",b)

#Q4 Write a program that takes input from the user and prints it using both Python 2.x and Python 3.x Version.

value = input("Enter anything here: ")
print("Value is:", value)
print "value is: ", value

""" Q5 Ask users to enter any 2 numbers in between 1-10 , add the two numbers and keep the sum in
another variable called z. Add 30 to z and store the output in variable result and print result as the
final output. """

value1 = int(input("Enter a number between 1-10: "))
value2 = int(input("Enter a number between 1-10: "))
z = value1 + value2
result = z + 30
print("Final Result is:", result)


#Q6 Write a program to check the data type of the entered values.

value = eval(input("Enter a something here: "))
if isinstance(value, str) :
    print("The data type of the input value is: String")
elif isinstance(value, int):
    print("The data type of the input value is: integer")
elif isinstance(value, bool):
    print("The data type of the input value is: boolean")
elif isinstance(value, float):
    print("The data type of the input value is: float")
else:
    print("The data type of the input value is:", type(value))



# Q7 Create Variables using formats such as Upper CamelCase, Lower CamelCase, SnakeCase and UPPERCASE.


UpperCamelCase = "ArjunPoudel"
lowerCamelCase = "arjunPoudel"
snake_case = "arjun_poudel"
UPPERCASE = "ARJUN POUDEL"


'''Q8 8. If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’
again. Will it change the value? If Yes then Why?'''

# yes it will change the value because the value stored in the variable is the last one assigned to it. It could be any data type.
