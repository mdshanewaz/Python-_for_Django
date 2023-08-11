def cuve(n):
    return n*n*n

listM = [2, 7, 1, 3, 9, 4] 

#using map function
newL = list(map(cuve, listM)) #function is passed (or defination passed) only not called (invoked) 
newT = tuple(map(cuve, listM))
newS = set(map(cuve, listM))
print(newL)
print(newS)
print(newT)

#using compension
ornewL = [i*i*i for i in listM]
ornewT = tuple(i*i*i for i in listM)
ornewS = {i*i*i for i in listM}
print(ornewL)
print(ornewT)
print(ornewS)

#using lambda function
lamnewL = list(map(lambda n: n*n*n, listM))
lamnewT = tuple(map(lambda n: n*n*n, listM))
lamnewS = set(map(lambda n: n*n*n, listM))
print(lamnewL)
print(lamnewT)
print(lamnewS)

#function call => functionname()
#function pass => functionname

l = ["Hello", "Shawon", "Bangladesh"]
l2 = list(map(list, l)) #function is passed (or defination passed) only not called (invoked)
print(l2)