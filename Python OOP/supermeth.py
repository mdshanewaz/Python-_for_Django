class A:
    def __init__(self, nam):
        self.name = nam
        print(self)
    
    def hello(self):
        print("Hello from class A for {}".format(self))

class B(A):
    def __init__(self, nam, job):
        A.__init__(self, nam)
        print(self)
        print("Hello from class B for {}".format(nam))
        print(job)

    def hello(self):
        print("Hello its overrided!")

obj2 = B("Shawon", "SE")
obj2.hello()

#using super fun
class A:
    def __init__(self, nam):
        self.name = nam
        print(self)
    
    def hello(self):
        print("Hello from class A for {}".format(self))

class B(A):
    def __init__(self, nam, job):
        super().__init__(nam)
        print(self)
        print("Constructor from class B for {}".format(nam))
        print(job)

    def hello(self):
        print("Hello its overrided!")

obj2 = B("Shawon", "SE")
obj2.hello()