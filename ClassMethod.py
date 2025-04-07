class student:
    
    school = "Vijay Vidyalala" #class variable
    
    def __init__(self,m1,m2,m3): #instance variables listed below
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    
    
    @classmethod        #classmethod you can get or change the value in the class wi=hich reflects in all the objects
    def get_School(cls):
        return cls.school
    
    @staticmethod   #it does not work with class or instance it is just a function 
    def info():
        print("ITs very simple")
        
    
        
s1 = student(80,90,86)
s2 = student(35,54,80)

print(student.get_School())
student.info()
