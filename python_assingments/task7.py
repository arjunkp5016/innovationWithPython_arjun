#Q1 Write a program that calculates and prints the value according to the given formula:

class SquareRoot:

    def __init__(self):
        self.C = 50
        self.H = 30

    def square_root(self, value):
        return ((2*self.C*value)/self.H)**0.5

obj = SquareRoot()
usr_inp = input("Enter numbers seperated with commas: ")
lst = usr_inp.split(',')

for i in lst:
    res  = obj.square_root(int(i))
    print("The result of {} applied to the function is: {:.2f}".format(i, res))


#Q2 Define a class named Shape and its subclass Square. The Square class has an init function which
#takes length as argument. Both classes have an area function which can print the area of the shape
#where Shape’s area is 0 by default.

class Shape:

   
    def __init__(self, length):
        self.area_shape = 0

        self.inner = self.Square(length)

    def area(self):
        print("The area is: {}".format(self.area_shape))


    class Square:
        def __init__(self, length):
            self.length = length
        
        def area(self):
            print("The area Square is : {}".format(self.length * self.length))



obj = Shape.Square(10)
obj.area()


#Q3 Create a class to find three elements that sum to zero from a set of n real numbers

class SumZero:

    
    def __init__(self, lst):
        self.lst = lst

    def func(self):
        res = []
        
        for i in range(0,len(self.lst)-1):
            l = i + 1
            r = len(self.lst) - 1
            x = self.lst[i]

            while l < r:
                if x + self.lst[l]+self.lst[r] == 0:
                    res.append([x,self.lst[l], self.lst[r]])
                    l+=1
                    r-=1
                elif x + self.lst[l]+self.lst[r]<0:
                    l+=1
                else:
                    r-=1

        return res

        
obj = SumZero([-25,-10,-7,-3,2,4,8,10])
print(obj.func())


#Q4 Create a Time class and initialize it with hours and minutes.
#Create a method addTime which should take two Time objects and add them.

class Time:

    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def addTime(self, obj1, obj2):
        self.hour = obj1.hour + obj2.hour

        if obj1.minute + obj2.minute > 59:
            self.hour+= 1
            self.minute = (obj1.minute + obj2.minute) - 60
        else:
            self.minute = obj1.minute + obj2.minute

        return self.hour, self.minute

    def displayTime(self):
        print("The time is {} hr {} min".format(self.hour, self.minute))

    def displayMinute(self):
        min = self.hour*60+self.minute
        print("{} hr {} min in minutes is: {}".format(self.hour, self.minute, min))


obj1 = Time(2,50)
obj2 = Time(1,20)
obj1.addTime(obj1, obj2)
obj1.displayTime()
obj1.displayMinute()


#Q5 Write a Person class with an instance variable “age” and a constructor that takes an integer as a
#parameter. The constructor must assign the integer value to the age variable after confirming the
#argument passed is not negative; if a negative argument is passed then the constructor should set
#age to 0 and print “Age is not valid, setting age to 0”. In addition, you must write the following instance methods:


class Person:

    def __init__(self, age):
        if age < 0:
            self.age = 0
            print("Age is not valid, setting age to 0")
        else:
            self.age = age

    
    def yearPasses(self, year):
        self.age+= year
        print("Age is now:",self.age)

    
    def amIOld(self):
        if self.age in range (0,13):
            print("You are a young.")
        elif self.age in range(13,20):
            print("You are a teenager.")
        else:
            print("You are old.")


obj1 = Person(-1)

obj2 = Person(4)
obj2.amIOld()

obj3 = Person(10)
obj3.amIOld()

obj4 = Person(16)
obj4.amIOld()

obj5 = Person(18)
obj5.amIOld()

obj6 = Person(64)
obj6.amIOld()

obj7 = Person(38)
obj7.amIOld()
obj7.yearPasses(4)
