class car :
    
    wheels = 4                  #class Variable
    
    def __init__(self):         #variable inside init is instance variable
        self.name = "BMW"  
        self.milage = 10
    
    
    
        
car1 = car()
print(car1.wheels) # at starting thw whees where 4 which is common since it is a class variable to all the methods
car.wheels = 5  #changing the value of wheels
print(car.wheels) #changed Value of variable
print(car1.wheels) #changed Value of variable which is common to all


# 4
# 5
# 5
