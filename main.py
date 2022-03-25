#reduce
from functools import reduce

mylist = [1, 2, 3, 4, 5]

def reduceAdd(x, y):
    return x + y

def reduceMulty(x, y):
    return x * y

print(reduce(reduceAdd, mylist)) # add all elements
print(reduce(reduceMulty, mylist)) # multiply all elements



#lambda expression

print(list(map(lambda x: x*2, mylist))) #double every element
print(list(filter(lambda x: x%2 ==1, mylist))) #filter odd numbers
print(list(filter(lambda x: x%2 ==0, mylist))) #filter even numbers
print(reduce(lambda x, y: x+y, mylist)) #sum all elements
print(reduce(lambda x, y: x*y, mylist)) #multiply all elements




