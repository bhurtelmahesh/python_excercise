# list, set and dictionary comprehensions

my_list = []
a = "abcdefghijklmnopqrstuvwxyz"
for i in a:
    my_list.append(i)
print(my_list) #['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#now, the same with list comprehension
my_list = [i for i in a]
print(my_list) #['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#or
my_list = [i for i in "abcdefghijklmnopqrstuvwxyz"]
print(my_list) #['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#or
my_list = [i for i in a if i not in "aeiou"]
print(my_list) #['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
#or
my_list = [i for i in a if i not in "aeiou" and i not in "bcdfg"]
print(my_list) #['h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
#or
my_list = [i for i in a if i not in "aeiou" and i not in "bcdfg" and i not in "hjklm"]
print(my_list) #['n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
#or
my_list = [i for i in a if i not in "aeiou" and i not in "bcdfg" and i not in "hjklm" and i not in "npqrst"]
print(my_list) #['v', 'w', 'x', 'y', 'z']
#or
my_list = [i for i in a if i not in "aeiou" and i not in "bcdfg" and i not in "hjklm" and i not in "npqrst" and i not in "vwxyz"]
print(my_list) #[]



