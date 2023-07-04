class Testing:
    author="" #global varialbe at class level  # -> pronounced -> properties
    # constructor not return anything- work -> initialization
    def __init__(self,author)->None:
        # author -> variable /parameter -> formal
        self.author=author
     

    def changeAuthorName(self,name:str)->str:
        self.author = name
        print(type(name))
        return self.author    
   
        


    


# obj1 = Testing("RD Sharma") #sucess  //calling constructor
# obj2 = Testing("Rs Aggarwal")
# obj3 = Testing("HC Verma")
# obj4 = Testing("Dinesh ")
# changedNameIs = obj2.changeAuthorName("Lala Har Dayal")  # calling method
# print(changedNameIs)
# print(obj2.author)   # printing

