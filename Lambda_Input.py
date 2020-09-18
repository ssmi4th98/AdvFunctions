add = lambda x,y: x + y

sub = lambda x,y: x - y

mult = lambda x,y: x * y

div = lambda x,y: x / y

def calc(*args, operation = 'add'):
    return operation(*args)


print(calc(4,5, operation=sub))

#lambdas are considered "one offs" to run and disguard, e.g.:

print(calc(10,4, operation=lambda x,y: x**y))

print((lambda x: x + 2)(10))  # this is x + 2 where the X value is 10

print((lambda x: x ** 10)(4))

# takes multiple arguments

print((lambda x,y: x ** y)(4,3))

# there are contraints to lambda

def check_if_even(x):
    assert x % 2 == 0  #this cannot be done with lambda as you cannot take keywords and other statements, e.g., assert

print(check_if_even(2))

# lambda can take in multiple variables it uses positional args.

total_score = lambda math, science, history, art=90: math + science + history + art

print(total_score(70,80,95,67))
print(total_score(math=70,science=80,history=95))  # these also take default values

#lambdas also take variable length arguments:

print((lambda *numbers: sum(numbers))(4,6,7,5,1,8,9))

#they also take variable length keyword arguments:

print((lambda **num_dic: sum(num_dic.values()))(a=5,b=7,c=8,d=22))  #the double * designates it as a keyword arg