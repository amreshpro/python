# base class
# object reserved -base class of all  class
class Animal(object):
    author="Om Puri"
    def eat(self,golgappa):
        print(golgappa)
        print( "I can eat!")
    
    def sleep(self):
        print("I can sleep!")

# derived class
class Dog(Animal):
    
    def bark(self):
        print("I can bark! Woof woof!!")

# Create object of the Dog class
dog1 = Dog() #class
anim = Animal() #class

anim.eat("Sachin")
anim.sleep()
print(anim.author)

# Calling members of the base class
dog1.eat("food") #paramerter
dog1.sleep()
# Calling member of the derived class
dog1.bark();  # self method