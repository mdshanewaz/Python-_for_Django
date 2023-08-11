myList = [2, 7, 1, 3, 9, 4]

def odd(n):
    return n%2 == 1

newList = list(filter(odd, myList))
print(newList)

newList2 = list(filter(lambda n: n%2==1, myList))
print(newList2)