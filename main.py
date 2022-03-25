#reduce
from functools import reduce

mylist = [1, 2, 3, 4, 5]

def reduceAdd(x, y):
    return x + y

def reduceMulty(x, y):
    return x * y

print(reduce(reduceAdd, mylist)) # add all elements
#15

print(reduce(reduceMulty, mylist)) # multiply all elements
#120



#lambda expression

print(list(map(lambda x: x*2, mylist))) #double every element
#[2, 4, 6, 8, 10]

print(list(filter(lambda x: x%2 ==1, mylist))) #filter odd numbers
#[1, 3, 5]

print(list(filter(lambda x: x%2 ==0, mylist))) #filter even numbers
#[2, 4]

print(reduce(lambda x, y: x+y, mylist)) #sum all elements
#15

print(reduce(lambda x, y: x*y, mylist)) #multiply all elements
#120


#excercise lambda
print(list(map(lambda x: x**2, mylist))) #square every element
# [1, 4, 9, 16, 25]

# list sorting with lambda expression ascending order and descending order
a = [(0,2), (4,3), (9,9), (10,-1)]

a.sort(key= lambda a: a[1]) #sort by second element
print(a) #[(10, -1), (0, 2), (4, 3), (9, 9)]

a.sort(key= lambda a: a[0]) #sort by first element
print(a) #[(0, 2), (4, 3), (9, 9), (10, -1)]

a.sort(key= lambda a: a[0], reverse=True) #sort by first element in reverse order
print(a) #[(10, -1), (9, 9), (4, 3), (0, 2)]

a.sort(key= lambda a: a[1], reverse=True) #sort by second element in reverse order
print(a) #[(9, 9), (4, 3), (0, 2), (10, -1)]

