class Person:
    """
    __init__() is just like constructor in java
    """
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        """
        __str__() is similar to toString() in java
        """
        return str("Name: "+self.name+" Age: " + str(self.age))
    
    def get_name(self):
        return f"{self.name}"


p1 = Person("Shivam",31)

print(p1.get_name())