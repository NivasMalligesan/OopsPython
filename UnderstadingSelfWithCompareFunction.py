class computer:       #class
    def __init__(self):
        self.name = "Nivas"
        self.age  = 19
    def compare(self,c2):  #self is c1 and argument passed is object c2
        if self.age == c2.age:
            return True
        else :
            return False
    

c1 = computer() #constructor
c2 = computer() #constructor
c2.age = 10 #self is c1 and argument passed is object c2
c1.name = "Virat" # can change value of the entities

if c1.compare(c2):
    print("their age are same")
else :
    print("they are diff")

print(c1.name)
print(c2.name)

