
myNum = [1, 2, 3, 4, 5]
myFruits = ["Apple", "Banana", "Cherry", "Date", "EMBLICA"]

for i, fruit in enumerate(myFruits):
    print(f"{i} index of {fruit}")
print("\n")

myCars = ["Bugati", "Toytota", "BMW", "Mercedies", "Jaguar"]

for i, j, k in zip(myNum, myFruits, myCars):
    print(i, j, k)
print("\n")

for i in reversed(sorted(myFruits)):
    print(i)