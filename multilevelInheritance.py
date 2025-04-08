#multilevel Inheritance
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

class C(B): #ingeriting from B and B inherit A 
    def feature5(self):
        print("Freature 5 working")

      
a1 = A()
a1.feature1()
a1.feature2()

b1 = B()
b1.feature1() #using the def of class A
c1 = C()
c1.feature5()
c1.feature1() #inheriting from a
