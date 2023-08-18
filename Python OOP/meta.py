#type is a meta class the class which helps to create another class is called meta class

myStr = "DBF"
myNum = 10
myDict = {"Name" : "Sawon"}
myList = [1, 2, 3, 4]

class A: 
    pass

print(type(A))

obj = A()

print(type(myStr))
print(type(myNum))
print(type(myDict))
print(type(myList))

print(type(obj))