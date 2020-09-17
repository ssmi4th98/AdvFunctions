import random as ran
import math


def hello(name):
    print('Hello,',name)

hello('Bruce')

hello  #this is an object that is stored in memory

#user functions can be assigned functions that invoke the defined function:

greet = hello

greet('Tom')  #Prints Tom using the defined hello function

calculate = len   #here you pas the len built in function to calculate and use that to do a len

print(calculate('This is a string'))

my_list = ('time',5.6,'car','fire')

print(calculate(my_list))

def area_circle(radius):
    return math.pi * radius * radius

def perim_circle(radius):
    return 2 * math.pi * radius

def diam_circle(radius):
    return 2 * radius

#functions can be passed as args into other functions

def calc_circle(radius, fn):
    return fn(radius)

print(calc_circle(20,area_circle))

