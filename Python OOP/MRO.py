class A:
    def __init__(self, nam):
        self.name = nam

    def hello(self):
        print("Hello form A")

class B:
    def __init__(self, job):
        self.possition = job

    def hello(self):
        print("Hello form B")

class C(A, B):
    def __init__(self):
        pass

    def hello(self):
        print("Hello form C")

obj1 = C()
obj1.hello()
#print(dir(obj1))
print(C.__mro__)