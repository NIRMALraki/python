d={}
class employee:
    def calculate(self,name,address,pan,basic,tds,deduct,hra,da):
        self.name=name
        self.address=address
        self.pan=pan
        self.basic=basic
        self.tds=tds
        self.deduct=deduct
        self.hra=hra*1.176
        self.da=da*0.25
        self.pf=3000
        salcal=self.basic+self.hra+self.da-(self.pf+self.tds)
        return salcal
    def accept(self):
        name=input("enter your name")
        address=input("enter your address")
        pan=input("enter your pan no")
        basic=int(input("enter basic pay"))
        tds=200
        deduct=300
        hra=67
        da=78
        self.sal=self.calculate(name,address,pan,basic,tds,deduct,hra,da)

    def display(self):
        print("name",self.name)
        print("address",self.address)
        print("pan",self.pan)
        print("salary",self.sal)
    
    def search(self,name):
        for k,v in d.items():
            print("k==",k)
            print("v==",v)
            if k==name:
                print(k.__dict__)
'''creating object and accepting  the values'''
e=employee()
e.accept()
'''displaying details'''
print("displaying details")
e.display()
'''updating to dictionary'''
d.update({e.name:e})
'''saerching inside d dictionary'''
print ("searching")
e.search("nirmal")


            
