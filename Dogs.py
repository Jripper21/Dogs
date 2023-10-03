class Dog:
    species = "Canis familiaris"
    
    def __init__(self, name, age, tricks=[]):
        self.name = name
        self.age = age
        self.tricks = tricks
        
    def bark(self):
        return f"{self.name} says Woof!"
    
    def do_trick(self, trick):
        if trick in self.tricks:
            return f"{self.name} is doing the {trick} trick!"
        else:
            return f"{self.name} doesn't know how to {trick}."

class GermanShepherd(Dog):
    
    def guard(self):
        return f"{self.name} is guarding the house!"
    
dog1 = Dog("Buddy", 2, ["sit", "roll"])
dog2 = Dog("Bella", 3, ["sit", "jump"])
gs_dog = GermanShepherd("Max", 4, ["guard", "sit"])

print(dog1.bark())  
print(dog2.bark())  
print(gs_dog.guard())  

print(f"{dog1.name} is {dog1.age} years old.")
print(f"{dog2.name} is {dog2.age} years old.")
print(f"{gs_dog.name} is {gs_dog.age} years old and is a {gs_dog.species}.")

print(dog1.do_trick("sit"))  # Output: Buddy is doing the sit trick!
print(dog2.do_trick("roll"))  # Output: Bella doesn't know how to roll.
print(gs_dog.do_trick("guard"))  # Output: Max is doing the guard trick!
