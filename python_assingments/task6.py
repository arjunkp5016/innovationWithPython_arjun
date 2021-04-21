#Q1 Write a program in Python to find out the character in a string which is uppercase using list comprehension.

string = "MyNameisARjUn"
lst = [x for x in string if x.isupper() == True]
print(lst)

#Q2 Write a program to construct a dictionary from the two lists containing the names of students and
#their corresponding subjects. The dictionary should map the students with their respective subjects.

def consutruct_dict(lst1, lst2):
    val = zip(lst1, lst2)
    return dict(val)
    
    
students = ['Smit','Jaya','Rayyan']
subjects = ['CSE', 'Networking', 'Operating System']

res = consutruct_dict(students, subjects)
print(res)

#Q4 Write a program in Python using generators to reverse the string.

String = "Consultadd Training"

def reverse_string(word):
    yield word[::-1]

res = reverse_string(String)
print(res.__next__())

#Q5 Write an example on decorators.

def modified_div(func):
    def helper(a,b):
        if b == 0:
            a,b = b,a
        return func(a,b)
    return helper


# @modified_div
def division(a,b):
    return a/b



res = modified_div(division)
print("Result is {}".format(res(2,0)))
