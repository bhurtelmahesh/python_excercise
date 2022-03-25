set1 = {i for i in range(10)}
print(set1) #{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

set2 = {i for i in range(10) if i%2 == 0}
print(set2) #{0, 2, 4, 6, 8}

set3 = {i for i in range(10) if i%2 == 1}
print(set3) #{1, 3, 5, 7, 9}

set4 = {i for i in range(1,1000) if i//3==0 or i//5==0}
print(set4) #{0, 3, 5, 6, 9, 10, 12, 15, 18, 20, 21, 24, 25, 27, 30, 33, 35, 36, 39, 40, 42, 45, 48, 50, 51, 54, 55, 57, 60, 63, 65, 66, 69, 70, 72, 75, 78, 80, 81, 84, 85, 87, 90, 93, 95, 96, 99}


# #now dictionary comprehension

dict1 = {k:k for k in range(0,10)}
print(dict1) #{0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}
# #or
dict2={v:v**2 for v in range(0,10) if v%2==0}
print(dict2) #{0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
# #or 
dict3={v:v**2 for v in range (10) if v%2!=0}
print(dict3) #{1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

dict4 = { v:v*2 for v in range(1,5)}
print(dict4) #{1: 2, 2: 4, 3: 6, 4: 8}

# pair a num with its double as a dict

#pair all the alphabets with their respective numbers
z = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
dict5 = {k:v for k,v in zip(z, range(1,100))}
print(dict5) #{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

#find the duplicates using list comprehension and set comprehension
some_list = ["a", "b", "c", "b", "d", "m", "n", "n"]
# duplicates =list(set([i for i in some_list if some_list.count(i)>1]))
duplicates = list({i for i in some_list if some_list.count(i)>1})
print(duplicates) #['b', 'n']
