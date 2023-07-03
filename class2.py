class Test:
    # variable/properties
    author="Sachidanand" # Test -> globall
# name = null  globally
    def __init__(self,name,surname):
        print("I am constructor")
        # name parameter or locally
        self.name = name # must line
        self.surname =surname

    def sqr(self,x):
        self.x=x*x 
        return self.x   


# constructor
obj = Test("Amresh","Maurya")  

print(obj.author) # access global
print(obj.name)
print(obj.surname)
print(obj.sqr(5))
