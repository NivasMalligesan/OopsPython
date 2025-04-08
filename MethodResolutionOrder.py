#method resolution order (MRO) 
class A:
    
    def __init__(self):
        print("Init in A is working")
    
    def feature1(self) :
        print("Feature 1-A Working")
    def feature2(self):
        print("Feature 2 Working")

class B(A): #inheritance
    def __init__(self):
        print("Init in B is working")
    def feature1(self) :
        print("Feature 1-B Working")
    def feature2(self):
        print("Feature 2 Working")

class C(A,B): #inheritance
    def __init__(self):
        print("Init in c is working")
    
c1 = C()
c1.feature1()


