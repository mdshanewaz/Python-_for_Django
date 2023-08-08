myList = [letter for letter in "Bohubrihi"]

print(myList)

matrix = []

for i in range(3):
    matrix.append([])
    for j in range(4):
        matrix[i].append(j)

print(matrix)

myMatrix = [[j for j in range(4)] for i in range(3)]
print(myMatrix)

flatList = [i[0] for i in myMatrix]
print(flatList)