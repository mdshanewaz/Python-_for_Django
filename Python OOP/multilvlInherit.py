class A:
    def __init__(self, nam):
        self.name = nam

    def hello(self):
        print("Hello form A")

class B(A):
    def __init__(self, nam, job):
        super().__init__(nam)
        self.possition = job

    def hello(self):
        print("Hello form B")

class C(B):
    pass

obj = C("Shawon", "Newaz")
obj.hello()
print(dir(obj))
print(C.__mro__)