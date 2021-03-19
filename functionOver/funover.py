class A:
    def hello1(self,name=None,age=None):
        self.name=name
        self.age=age
        if self.name!=None and self.age!=None:
            print("hello")
        elif self.name!=None and self.age==None:
            print("hello")
        else:
            print("hello")    
b = A()
b.hello1()
b.hello1("nirmal")
b.hello1("nirmal")
b.hello1("nirmal","35")            