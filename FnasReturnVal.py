def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def multi(a,b):
    return a * b

def div(a,b):
    return b/a

# you can return a function from within a function as you can other data types:

def get_fn(operator='+'):
    if operator == '+':
        return add

    if operator == '-':
        return sub

    if operator == '*':
        return multi

    if operator == '/':
        return div

func = get_fn('*')

print(func(4,5))

# function objects can be elements in a list or values in a python dictionary

calc_dic = {
    '+': add,
    '-': sub,
    '*': multi,
    '/': div
    }

func2 = calc_dic['/']

print(func2(4,12))

print(calc_dic['*'](8,9))  # here you can invoke the calc_dic and pass in the variables to the proper function.

print(calc_dic['+'](8,9))