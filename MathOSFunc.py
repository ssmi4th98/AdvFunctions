# help('modules')  #built in functions and modules displayed.

import math  #this is built in: see list
import os

print(math.pi)
print(math.e)
print(math.ceil(0.1))
print(math.sqrt(244))


#os allows access to os level functions

print(os.listdir('.'))

os.mkdir('./my_temp_dir')
print(os.listdir('.'))
os.rmdir('./my_temp_dir')
print(os.listdir('.'))

cwd = os.getcwd()

print(cwd)

print(os.path.isdir(cwd))

# can use specific functions within the modules using "from os import path"

from os import path

print(path.exists(cwd))

