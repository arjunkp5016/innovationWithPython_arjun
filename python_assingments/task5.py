#Q1 Write a program in Python to allow the error of syntax to be handled using exception handling.

try:
    eval("a+a=a")
except SyntaxError as e:
    print("You made the syntax Error.", e)

# however without eval its not possible to catch syntax error because  the execption is caught by the compiler even before the execution of try/execpt 

#Q2 Write a program in Python to allow the user to open a file by using the argv module. If the entered name is incorrect throw an exception and ask 
# them to enter the name again. Make sure to use read only mode.

import sys

def file_open(a): 
    try:
        _ = open(a, 'rt')
        print("File opened")
    except FileNotFoundError:
        print("Incorrect file name")
        file1 = input("Enter the file name again: ")
        file_open(file1)
    

file_open(str(sys.argv[1:2]))
        

#Q3 Write a program to handle an error if the user entered a number more than four digits it should return “The length is too short/long !!! Please provide only four digits”

def fun_four():
    try:
        value = int(input("Enter digits: "))
        if len(value) > 4 or len(value)< 4:
            raise Exception
    except Exception:
        print("The length is too short/long!!! Please provide only four digits")


fun_four()

#Q4 Create a login page backend to ask users to enter the username and password. Make sure to
#ask for a Re-Type Password and if the password is incorrect give chance to enter it again but it
#should not be more than 3 times.

#validate user password
def login(username, password):
    saved_pass = {'consultadd': 'python'} #user -> consultadd, password -> python
    if username in saved_pass:
        if saved_pass[username] == password:
            print("Login successful")
        else:
            print("Login Failed")

    else:
        print("User doesn't exists.")

#ask user for username and password
def usr_inp():
    count = 0
    # verified = True
    userName = input("Enter the username: ")
    userPass = input("Enter the password: ")
    re_pass = input("Retype the password: ")
    while re_pass != userPass and count<3:
        print("Password didn't match:")
        re_pass = input("Retype the password: ")
        count+=1
    login(userName, userPass)

usr_inp()


#Q6 Read doc.txt file using Python File handling concept and return only the even length string from the file.

#Get the file name from user
file = input("Enter the file you want open: ")
try:
    f = open(file, 'r+')
    while True:
        words = f.readline().strip('.')
        lst = list(filter(lambda x: len(x)%2==0, words.split()))
        print(' '.join(lst))

        if not words:
            break
except FileNotFoundError as e:
    print("File doesn't exists:", e)

























