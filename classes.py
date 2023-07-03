class ABC :
    def sqr(x):
        return x*x
    # it is not a constructor
    def ABC():
        print("Hello constructor")

    def __init__(self):
        print("I am in python constructor")
        print(self)
            



# obj = new ABC()
obj =  ABC()
obj.ABC()
obj.sqr(5)