#A function that accepts or returns another function as argument is called higher order function
def myFun():
    def hello():
        print("Hello, world!")
    return hello

myVar = myFun() 
print(myVar)
myVar()

#wrapper fun
def myWrapper(fun):
    def test():
        print("I am from test! Before")
        fun()
        print("I am from Test! After")
    
    return test

def great():
    print("Hello World!")

def hello():
    print("Hello BD!")

great = myWrapper(great)
great()

hello = myWrapper(hello)
hello()