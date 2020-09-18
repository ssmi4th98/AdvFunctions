def square(x):
    return x ** 2

print(square(3))

print(square)

#anonymous function = lambda
# cannot have complex function or if and or args.
#lambda functions can be used in the same way as any other function


cube = lambda x: x * x * x

print(cube(3))

add = lambda x,y: x + y

sub = lambda x,y: x - y

mult = lambda x,y: x * y

div = lambda x,y: x / y

def calc(*args, operation = 'add'):
    if operation == 'add':
        return add(*args)
    if operation == 'sub':
        return sub(*args)
    if operation == 'mult':
        return mult(*args)
    if operation == 'div':
        return div(*args)

print(calc(5,6, operation = 'mult'))
