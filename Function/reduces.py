from functools import reduce


myList = [2, 7, 1, 3, 9, 4] 

def addition(x, y):
    return x+y

sum = (reduce(addition, myList))
print(sum)
