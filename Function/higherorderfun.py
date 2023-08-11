def hof(fn):
    fn()
    print(fn.__name__)

def great():
    print("It's great")

def hello():
    print("Hello world!")

hof(hello)
hof(great)

myList = [0, 1, 2, 3, 4, 5, 6, 7, 8]
newList = list(filter(lambda x: x%2==1, myList))
print(newList)


def myFilter(fn, l):
    newL = []
    for i in l:
        if fn(i):
            newL.append(i)
    return newL

newList2 = list(myFilter(lambda x: x%2==1, myList))
print(newList2)

def even(n):
    if n % 2 == 0:
        return n

newList3 = list(myFilter(even, myList))
print(newList3)