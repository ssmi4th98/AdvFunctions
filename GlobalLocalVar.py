country = 'USA'
city = 'Washington'

def somefunc():
    print(country)
    print(city)

somefunc()

def func2():
    country = 'India'  #here the local variable is set and overrides the global var

    print(country)
    print(city)

func2()

def func3():
    city = 'Washington'  #by defining 'city' the append works below.
    city = city + 'Seattle'  #this results in an error as local variable "city" and it is not called.

    print(country)
    print(city)


func3()

# global and local variables live in the same name space declaring the variable in the function, e.g., \n
#  func4(country,city): makes it a local variable
# to reference the global variable locally it must be declared in the function:

def func4():
    global city

    city = city + ' Seattle'
    print(country)
    print(city)


func4()

# the above changes the global variable to the stated changed variable by the executed function

print(country, city)