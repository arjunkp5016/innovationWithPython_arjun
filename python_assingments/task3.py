#Q1 Create a list of 10 elements of four different data types like int, string, complex and float.

lst = ["python", "training", 4, 13, 20.21, True, complex(2,3), 85.25, complex(5,4), False]


#Q2 Create a list of size 5 and execute the slicing structure

lst = [x for x in range(5)]
#print first element in the list
print(lst[0])
#print  first 3 elements in the list
print(lst[0:3])
#print every elements in even index 
print(lst[::2])
#reverse listt
print(lst[::-1])


#Q3 Write a program to get the sum and multiply of all the items in a given list.

lst = [x for x in range(1,11)]
sum = 0
product = 1
for x in lst:
    sum+= x
    product*= x
print("Sum is:",sum)
print("Product is:",product)


#Q4 Find the largest and smallest number from a given list.
lst = [x for x in range(1,11)]
largest = max(lst)
smallest = min(lst)
print("Largest of list is:",largest)
print("Smallest of the list is:",smallest)


#Q5 Create a new list which contains the specified numbers after removing the even numbers from a predefined list.

lst = [x for x in range(1,21)]
new_lst = list(filter((lambda x: x%2!=0),lst))
print(new_lst)

#Q6 Create a list of elements such that it contains the squares of the first and last 5 elements between 1 and30 (both included).

lst = [x**2 for x in range(1,31) if x <6 or x > 25]
print(lst)

#Q7 Write a program to replace the last element in a list with another list.

lst = [1,3,5,7,9,10]
lst1 = [2,4,6,8]
lst.pop()
lst.extend(lst1)
print(lst)


#Q8 Create a new dictionary by concatenating the following two dictionaries:

a = {1:10, 2:20}
b = {3:30, 4:40}
a.update(b)
print(a)


#Q9 Create a dictionary that contain numbers in the form(x:x*x) where x takes all the values between 1 and n(both 1 and n included).

n = int(input("Enter the number of elements you want in dictionary: "))
d = {x:x*x for x in range(1,n+1)}
print(d)

#Q10 Write a program which accepts a sequence of comma-separated numbers from console and generates a list and a tuple which contains every number in the form of string.

value = input("Enter the sequence of number seperated by comma: ")
lst = value.split(',')
tup = tuple(lst)
print(lst,end='')
print(tup)