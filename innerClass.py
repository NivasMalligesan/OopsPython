class student:
    def __init__(self,name,rollNo):
        self.name = name
        self.rollNo = rollNo
        self.lap  = self.laptop() #initialization of Laptop class
    def show(self):
        print(self.name,self.rollNo)
    
    class laptop:               #innerClass
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8
            
        
s1 = student('Nivas',2)
s2 = student('Kiran',3)
print(s1.lap.brand) #how to access innerClass
s1.show()
