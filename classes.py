import random

class Animal:
    info = "a living organism that feeds on organic matter"

    def __int__(self,name):
        print("An animal is created")
        self.name =name
        self.fur =""

class Dog(Animal):
    #info = "A cute friend"

    def __init__(self,name):
        super().__int__(name)
        print("A dog is created")

dog1 = Dog("Lazy")

print(dog1.info)


class community_Development:
    info ="project community"


    def __init__(community, name):
        community.name =name

community1 = community_Development("Los llanitos")
community2 = community_Development("El Zarzal")

print(community1.name)
print(community2.name)

class Bulldog(Dog):

    def __int__(self,name):
        super().__int__(name)
        print("Abulldog is created")

dog1 = Bulldog("Lazy")
