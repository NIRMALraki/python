class calculation:
    def __init__(self):
        self.list1=[]

    def accept(self):
        n=int(input("enter the length of list"))
        l3=[]
        for i in range(n):
            l3.append(int(input("enter the elements")))
        return l3
            
    def __add__(self,num2):
        l3=[]
        for i in range(len(self.list1)):
            l3.append(self.list1[i]+num2.list1[i])
        return l3    

    def __sub__(self,num2):
        l3=[]
        for i in range(len(self.list1)):
            l3.append(self.list1[i]+num2.list1[i])
        return l3    

    def __mul__(self,num2):
        l3=[]
        for i in range(len(self.list1)):
            l3.append(self.list1[i]*num2.list1[i])
        return l3

    def __div__(self,num2):
        l3=[]
        for i in range(len(self.list1)):
            l3.append(self.list1[i]/num2.list1[i])
        return l3

    def __floatdiv__(self,num2):
        l3=[]
        for i in range(len(self.list1)):
            l3.append(self.list1[i]//num2.list1[i])
        return l3