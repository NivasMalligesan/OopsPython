class student:
    
    school = "Vijay Vidyalala" #class variable
    
    def __init__(self,m1,m2,m3): #instance variables listed below
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    
    #instance methods Below it changes only according to the object
    def average(self):           #instance method because it works with the object
        return (self.m1+self.m2+self.m3)/3     #2 methods Accessors and Mutators
        
    def get_m1(self): #Accessors
        return self.m1
    def set_m1(self): #Mutators
        self.m1 = 10;
        return self.m1
        
    
        
s1 = student(80,90,86)
s2 = student(35,54,80)

print(s1.average())
print(s2.average())
print(s2.get_m1())
