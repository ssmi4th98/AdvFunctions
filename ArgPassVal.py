salary = 1000
expense = 200
name = 'Jimmy'
interest_rate = 0.25

def print_savings_detail():  # this takes no arguments so all vars are global.
    pass


def print_savings_detail(name,salary,expense,interest_rate):  #here vars are local
    name = 'Harry'
    print('Name on account: ', name)

    salary = salary * 2
    expense = expense + 200


    savings = salary - expense
    print('Savings is: ',savings)

    print('Interest rate: ',interest_rate)

print_savings_detail('steven',3000,400,1.5)

print(name, salary,expense, interest_rate)  #This shows that the global variables are not changed by the local vars.


fruit_list = ['apples','pears','oranges','bananas']

def change_list(fruit_list):
    fruit_list = ['kiwi','peach']  #changes inside the function stay inside the function but do not impact global
                                   #this is true for primative and complex data types.
    print('Fruit list: ',fruit_list)

change_list(fruit_list)
print()
print('Outside function: ',fruit_list)