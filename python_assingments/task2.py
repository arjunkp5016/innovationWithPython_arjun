#Q1 Write a program in Python to perform the following operation:

number = int(input("Enter a number: "))

#check if number is divisible by both 3 and 5
if number % 3 == 0 and number % 5 == 0:
    print("Consultadd - Python Trainning")
elif number % 3 == 0: #check if number is divisible by 3
    print("Consultadd")
elif number % 5 == 0: # check if number is divisible by 5
    print("Python Training")

#Q2 Write a program in Python to perform the following operator based task:

print("Choose an option below:")
print("1 - Addition\n2 - Subtraction\n3 - Division\n4 - Multiplication\n5 - Average")
case = int(input("Enter a number to perform operation you choose: "))

#Ask user for 2 numbers
def ask_user():
    num1 = int(input("Enter a First Number: "))
    num2 = int(input("Enter a Second Number: "))
    return num1, num2

#Addition
if case == 1:
    num1, num2 = ask_user()
    sum= num1+num2
    if sum >= 0:
        print("The Sum of {} and {} is:".format(num1,num2),sum)
    else:
        print("NEGATIVE")
elif case == 2: #Subtraction
    num1, num2 = ask_user()
    difference = num1-num2
    if difference >= 0:
        print("The difference of {} and {} is:".format(num1,num2),difference)
    else:
        print("NEGATIVE")
elif case == 3: #Division
    num1, num2 = ask_user()
    result = num1/num2
    if result >= 0:
        print("{} divided by {} is:".format(num1,num2),result)
    else:
        print("NEGATIVE")
elif case == 4: #Multiplication
    num1, num2 = ask_user()
    result = num1*num2
    if result >= 0:
        print("{} multiplied by {} is:".format(num1,num2),result)
    else:
        print("NEGATIVE")
elif case == 5: #Average
    num1, num2 = ask_user()
    num3 = int(input("Enter a Third Number: "))
    num4 = int(input("Enter a Fourth Number: "))
    sum = num1+num2+num3+num4
    average = sum / 4
    if average >= 0:
        print("Average of {},{},{},{} is:".format(num1,num2,num3,num4),average)
    else:
        print("NEGATIVE")
else:
    print("Invalid choice.")


#Q3 Write a program in Python to implement the given flowchart:

a, b, c = 10, 20, 30 
#average of numbers
avg = (a+b+c)/3
print("Average = ",avg)
if avg > a and avg > b and avg > c:
    print("Average is higher than a, b, c")
else:
    if avg > a and avg > b:
        print("average is higher than a, b")
    elif avg > a and avg > c:
        print("average is higher than a, c")
    elif avg > b and avg > c:
        print("average is higher than b, c")
    elif avg > a:
        print("average is just higher than a")
    elif avg > b:
        print("average is just higher than b")
    elif avg > c:
         print("average is just higher than c")
    


#Q4 4. Write a program in Python to break and continue if the following cases occurs:

while True:
    num = int(input("Enter a number: "))
    if num > 0:
        print("Good Going")
    else:
        print("It's Over")
        break


#Q5 5. Write a program in Python which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200.

for x in range(2000,3200):
    if x%7 == 0 and x%5 !=0:
        print(x)


#Q6 What is the output of the following code examples?
x=123
for i in x:
    print(i)

#output
#TypeError: 'int' object is not iterable

i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
    else:
        print("error")

#output
# 0
# error
# 1
# error
# 2

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        Break


#Output
# 0
# 1
# 2
# 3
# 4
# NameError: name 'Break' is not defined

#Q7 Write a program that prints all the numbers from 0 to 6 except 3 and 6.

for x in range(0,6):
    if x ==3 or x == 6:
        continue
    else:
        print(x)

#Q8 Write a program that accepts a string as an input from the user and calculate the number of digits and letters.

word = str(input("Enter a String here: "))
digits = 0
letters = 0
for x in word:
    if x.isdigit():
        digits+=1
    elif x.isalpha():
        letters+=1
print("Letters:",letters)
print("Digits",digits)

'''Q9 9. Read the two parts of the question below: Write a program such that it asks users to “guess the lucky number”. If the correct number is
guessed the program stops, otherwise it continues forever.Modify the program so that it asks users whether they want to guess again each time. Use two
variables, ‘number’ for the number and ‘answer’ for the answer to the question whether they wantto continue guessing. The program stops if the user guesses the correct number or answers “no”. (
The program continues as long as a user has not answered “no” and has not guessed the correctnumber)'''

lucky_number = 7

while True:
    user_input = int(input("Guess the Lucky Number."))
    if user_input == lucky_number:
        print("You guessed it right.")
        break

#Modified Version
lucky_number = 7
answer = ''
number = 0
while True:
    number = int(input("Guess the Lucky Number."))
    
    if number == lucky_number:
        break 
    else:
        answer = input("Do you want to guess again? ")
    if answer == 'no':
        break


#Q10 Write a program that asks five times to guess the lucky number. Use a while loop and a counter
import random 
counter = 1
lucky_number = random.randint(0,10)
while counter <= 5:
    number = int(input("Guess the number: "))
    print("Trial",counter,": The number guessed is",number)
    counter+=1
    if number == lucky_number:
        print("Good guess!")
    else:
        print("Try Again!")
print("Game Over!")


"""Q11 In the previous question, insert break after the “Good guess!” print statement. break will terminatethe while loop so that users do not have to continue guessing after they found the number. If the user
does not guess the number at all, print “Sorry but that was not very successful """

import random 
counter = 1
lucky_number = random.randint(0,10)
while counter <= 5:
    number = int(input("Guess the number: "))
    print("Trial",counter,": The number guessed is",number)
    counter+=1
    if number == lucky_number:
        print("Good guess!")
        break
    else:
        if counter == 6:
            print("Sorry but that was not very successful")
        else:
            print("Try Again!")
    
print('Game Over!')
