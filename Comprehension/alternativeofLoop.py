myList = [1, 3, 5, 2, 8]

newList = []

for i in myList:
    newList.append(i*i)

print("Old list myList: ", myList)
print("New list newList: ", newList)

comList = [i*i for i in myList]

print("Com list comList:", comList)

#making list for the odd number of myList

newListofOdd = []
for i in myList:
    if i%2 == 1:
        newListofOdd.append(i*i)

print(newListofOdd)

comList2 = [i*i for i in myList if i%2 == 1]
print(comList2)