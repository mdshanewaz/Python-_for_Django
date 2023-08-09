def hello(fname="Shah", lname="Newaz"):
    print("Hello {} {}". format(fname, lname))

hello()

def newHello(**kwargs):
    print(kwargs)

newHello(fname = "Shah", lname = "Newaz", age = 26)