# values created within a function can be used outside it by passing a reference


fruit_list = ['apples','grapes','oranges']

def change_list(fruit_list):  #this brings in the original list

    fruit_list[0] = 'Kiwi'  #this changes the contents of the list as we use [] with the 0 or first var.

    print("Inside function: ",fruit_list)

change_list(fruit_list)
print()
print('Outside list: ',fruit_list)  #Here the inside function repaces value for outside global var


fruit_list = ['kiwi','banana']

def list2(fruit_list):
    fruit_list.append('mango')

    print('list2 inside: ',fruit_list)

list2(fruit_list)
print()
print('Outside list: ',fruit_list)

fruit_list = ['kiwi','banana']

def list2(fruit_list):
    fruit_list.remove('banana')  #rmoval

    print('list2 inside: ',fruit_list)

print()
list2(fruit_list)
print()
print('Outside list: ',fruit_list)


new_list = ['orange','mango','pear']  #complex types can change except for tuples, as they are immutable

def new_func(new_list):
    new_list.sort()
    new_list.pop()

    print('Inside new: ',new_list)

new_func(new_list)
print()
print('Outside new: ',new_list)



car_dictionary = {
                "ford": 150,
                "toyota": 200,
                'audi': 150
    }


#this works for dictionaries as well.

def new_func2(some_dictionary):
    some_dictionary['audi'] = 310
    print('Inside somelist: ',some_dictionary)

new_func2(some_dictionary)
print()
print('New list: ',car_dictionary)

