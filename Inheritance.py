class Parent:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def __str__(self):
        return f"'First name: ' + {self.fname} + ' lastname: ' + {self.lname}"
    
    def printname(self):
        print(self.fname,self.lname)
    
class Child(Parent):
    def __init__(self,fname,lname):
        Parent.__init__(self,fname,lname)

child_obj = Child("Shivam","Kashyap")

child_obj.printname()   


class Child2(Parent):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

child_obj2 = Child2(fname="Shivam",lname="Kashyap")
child_obj2.printname()