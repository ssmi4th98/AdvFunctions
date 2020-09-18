#lambdas are used with filters

num = [3,55,786,990,761,545]

mylist=list(filter(lambda x: x < 100, num))

print(mylist)

even_list=list(filter(lambda x: x % 2 == 0,num))  # must pass in list object to get return in form of list

print(even_list)

greaterThanTen_LessThanHundred=list(filter(lambda x: x > 10 and x < 100, num))

print(greaterThanTen_LessThanHundred)