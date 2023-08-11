def hello(fname="Shah", lname="Newaz"):
    print("Hello {} {}". format(fname, lname))
    print("\n")

hello()

def newHello(**kwargs):
    print(kwargs)
    print("\n")

newHello(fname = "Shah", lname = "Newaz", age = 26)

def newHello2(*args, **kwargs):
    print(args)
    print("\n")
    print(kwargs)
    print("\n")
    
newHello2("Shah", "Newaz", 26, True, nickname = "Shawon", Pos = "Eng")
newHello2()