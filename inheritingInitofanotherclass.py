#multilevel Inheritance
class A:
    
    def __init__(self):
        print("Init in A is working")
    
    def feature1(self) :
        print("Feature 1 Working")
    def feature2(self):
        print("Feature 2 Working")

class B(A): #inheritance
    def __init__(self):
        super().__init__() #inherits the init from class A
        print("Init in B is working")
    def feature3(self) :
        print("Feature 1 Working")
    def feature4(self):
        print("Feature 2 Working")



a1 = A()  #parent class cannot access all the methods of child class
# a1.feature3() error will come 
b1 = B() #child Class can access all the methods in parent class can access the constructor if you have Constructor in B class it will call it


