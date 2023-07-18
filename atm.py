class ATM:
    
    def __init__(self,initialMoney) -> None:
     self.totalBalance = initialMoney
        
    def checkBalance(self):
        return self.totalBalance
    
    def addMoney(self,money):
        self.totalBalance = self.totalBalance + money
     
    def withDrawMoney(self,money):
        if money >=self.totalBalance :
            return "Tere Pass Itne Paise Nhi h be"
        self.totalBalance = self.totalBalance - money
        
        
   
        
 
    
# object
sachidanand =    ATM(0)
# print(sachidanand.checkBalance()  )
# sachidanand.addMoney(5000)
# print(sachidanand.checkBalance())
# sachidanand.withDrawMoney(10456)
print(sachidanand.checkBalance())       
        
        
        
amresh = ATM(500)
# initial = 1500
print(amresh.checkBalance())   
# amresh.addMoney(1500)
     