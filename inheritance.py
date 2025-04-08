class A:
    def feature1(self) :
        print("Feature 1 Working")
    def feature2(self):
        print("Feature 2 Working")

class B(A): #inheritance
    def feature3(self) :
        print("Feature 1 Working")
    def feature4(self):
        print("Feature 2 Working")
    

      
a1 = A()
a1.feature1()
a1.feature2()

b1 = B()
b1.feature1() #using the def of class A
