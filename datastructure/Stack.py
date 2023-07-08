class Stack:
    #constructor
    # t = 10 #class level 
    # bucket = [] iska scope - class level 
    def __init__(self):
        # a=7 #only function/method level
        self.bucket=[]
        # self.bucket=[1,3,4,5,6,16,7,8,8,9,14]
        # self.t=11
        #self.bucket[0]
        #self.bucket[1]
        #self.bucket[len(self.bucket)] //error
        #self.bucket[len(self.bucket)-1] //14
        #print(len(self.bucket)) 
        #self.bucket[10] 14
        #self.bucket[11] error
        # list.remove(16) //remove 16

    # push
    def push(self,item):
        # b=19
        # t=1020 #function level
        # print(self.t) #10
        # print(t)
        return self.bucket.append(item)
    
    # pop
    def pop(self):
        # print(b) error
        # t=290
        # print(t)
        if(len(self.bucket)):
            popedItem = self.bucket[len(self.bucket)-1]
            # self.bucket.remove(self.bucket[len(self.bucket)-1])
            self.bucket.pop()  
                        
            return popedItem
        else:
            return -1
         
         
    def peek(self):
           return self.bucket[len(self.bucket)-1]
         
    # display
    def print(self):
        for i in range(0,len(self.bucket)):
            print(self.bucket[i])
            

    
    
stack = Stack()
stack.push(8)
stack.push(2)    
stack.push(3)    
stack.push(8)    
stack.push(5)    
stack.push(6)    
stack.push(7)    
stack.push(8)
print("All Data")
stack.print()
stack.pop()
stack.pop()
stack.pop()
print("Print After POP")
stack.print()    
print("peek:",stack.peek())
    


