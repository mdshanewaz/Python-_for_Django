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
    def __init__(self, nam, job):
        #super().__init__(self, nam) This method will not work because it will handel only one constructor of First(A) class in MRO
        A.__init__(self, nam)
        B.__init__(self, job)
    
    def hello(self):
        super().hello()
        B.hello(self)
        print("Hello from C")


obj1 = C("Shah", "Newaz")
obj1.hello()
#print(dir(obj1))
#print(C.__mro__)