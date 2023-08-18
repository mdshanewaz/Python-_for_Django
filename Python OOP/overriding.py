class A:
    def __init__(self, nam):
        self.name = nam
        print(self)
    
    def hello(self):
        print("Hello from class A for {}".format(self))

obj = A("Shawon")
obj.hello()

class B(A):
    def __init__(self):
        print(self)
        print("Hello from class B for {}".format(self))

    def hello(self):
        print("Hello its overrided!")

obj2 = B()
obj2.hello()
