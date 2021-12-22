#python gives us a option to check if the class is an instance or not using the isinstance(instance,Class) keyword
class Parent:
    pass
class Wizard(Parent):
    def __init__(self,name,power):
        self.name = name
        self.power = power

wizard1 = Wizard('Andrew',200)

print(isinstance(wizard1,Wizard))   #isinstance(instance,class)
print(isinstance(wizard1,Parent))   #child class is also a instance of Parent class


  
