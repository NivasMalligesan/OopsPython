class computer:#class
    
    def __init__(self):
        print("In init")
    
    def config(self): #method
        print("i5 16gb")
    

#object creation
comp1  = computer() #constructer #calls init
comp2  = computer() #constructer #calls init

comp1.config() #comp1 belongs to 
comp2.config() #comp2 belongs to 

#output 
# In init
# In init
# i5 16gb
# i5 16gb
