#you can make the function more useful by using the "*args" variable to allow for multiple arguments


def calc(*args,fn):
    return fn(*args)

def diam_circle(radius):
    return 2 * radius

def rec_area(len,wid):
    return len * wid

def rec_perim(len,wid):
    return 2 * (len + wid)

print(calc(10,fn=diam_circle))  #here you need to 'set' the function def with fn=