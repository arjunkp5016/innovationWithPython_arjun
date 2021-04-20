#Q1 Create a list of given structure and get the Access list as provided below:

x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]

print(x[5][:4])
print(x[6:8])
print(x[::2])
print(x[::-1])
print(x[5][5][:1])
print(x[8:8])

#Q2 Create a list of thousand numbers using range and xrange and see the difference between each

lst = range(1001)

# xrange is deprecated in python 3.X 

# syntaxfor python 2.X
x = xrange(1,11)
print(x)

 #Output:
# xrange(1, 11)


#Q3 How Tuple is beneficial as compared to the list?

#if you want to store a data that should'nt be altered, using tuple would be benificial. Also tuple is faster for the big numbers of elements, and tuples can't be copied.


#Q4 Write a program in Python to iterate through the list of numbers in the range of 1,100 and print the number which is divisible by 3 and is a multiple of 2

for x in range(1,101):
    if x%3 == 0 and x%2== 0:
        print(x)

#Q5 Write a program in Python to reverse a string and print only the vowel alphabet if it exists in the string with their index.
vowel = ['a','e','i','o','u']
word = input("Enter the string: ")
reverse_string = word[::-1]
i = 0
while i < len(reverse_string):
    if reverse_string[i].lower() in vowel:
        print(reverse_string[i], i)
    i+=1


#Q6 Write a program in Python to iterate through the string “hello my name is abcde” and print the string which is having an even length.

line = "hello my name is abcde"

words = list(filter(lambda x: len(x)%2 == 0, line.split(' ')))
for x in words:
    print(x)

#Q7  Write a program in python to print the pair of numbers whose sum is equal to the result number that is let's say 8.

x = [1,2,3,4,5,6,7,8,9,-1]

lst = []
counter = 0
while counter < len(x):
    inc = counter+1
    while  inc < len(x):
        if x[counter] + x[inc] == 8:
            lst.append([x[counter], x[inc]])
        inc+= 1
    counter+= 1

print(lst)



#Q8 Write a program in Python to complete the following task:
# from functools import reduce

def maximum():
    even = []
    odd = []

    while True:
        value = int(input("Enter the value between 1 to 50: "))

        if value%2 == 0 and len(even) < 5:
            even.append(value)
        elif value%2 == 1 and len(odd) < 5:
            odd.append(value)
        elif len(even) == 5  and len(odd) == 5:
            break


    sum_even  = reduce(lambda x,y: x+y, even)
    sum_odd  = reduce(lambda x,y: x+y, odd)

    if sum_even > sum_odd:
        return "Maximum is {} of even list {}".format(sum_even, even)
    else:
        return "Maximum is {} of odd list {}".format(sum_odd, odd)


print(maximum())


#Q9 Write a program in python to print the pair of numbers whose sum is equal to the result number that is let's say 8.

def occurence(word, letter):
    count = 0
    for x in word:
        if letter == x:
            count+=1
    return letter, count

userInput = input("Enter the String: ") 
char = input("Enter the character to count: ")
a, b = occurence(userInput, char)
print("{} = {}".format(a,b))


#Q10 10. Generate and print another tuple whose values are even numbers in the given tuple

tup = (1,2,3,4,5,6,7,8,9,10)

new_tup = tuple(x for x in tup if x%2==0)
print(new_tup)