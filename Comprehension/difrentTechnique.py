myList = [2, 7, 10, 3, 6]

print(myList)

newList = [i+2 for i in myList]

newDict = {
    key : 0 for key in myList 
}

newSet = {i**3 for i in myList}

newTuple = tuple(i*4 for i in myList)

newTupleList = [(i, i*i, i*2) for i in myList]

print(newList)

print(newDict)

print(newSet)

print(newTuple)

print(newTupleList)

myDict = {
    "Name" : "Rimi",
    "Country" : "Bangladesh",
    "Age" : 24
}

newListFromFDict = [value for key, value in myDict.items()]
print(newListFromFDict)

newTupleList = [(key, value) for key, value in myDict.items()]
print(newTupleList)

newDict2 = {
    "Key " + key : value for key, value in myDict.items()
}
print(newDict2)