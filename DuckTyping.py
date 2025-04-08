#polymorphism
#duck typing
#same method in different class

class compiler:
    def execute(self):
        print("Compiling")
        print("Running")
        
class Editor:
    def execute(self):
        print("Spell Check")
        print("Compiling")
        print("Running")

class Laptop :
    def code(self,ide):
        ide.execute()
        
        
ide = Editor()       #execute is there in compiler referes to class Compiler 
ide = compiler()     #execute is there in Editor referes to class Editor 
lap1 = Laptop()
lap1.code(ide) #now ide refers to compier class so execute in class compiler works
