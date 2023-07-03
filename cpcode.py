
n = 7
arr = [1,2,3,4,5,6,7]
# arr index - 0 , arr[0] = first value

def checkPerfectArray(n,arr) :
    # first condition
    if n>1000 or n<1 : return -1
    # second condition
    for i in range(0,n):
        if arr[i]%(i+1) ==0:
            # third condition
            sum = 0
            for i in range(0,n) :
                sum =sum+ arr[i]
                if sum%n==0:  
                    print(arr[i])  
        else:
            return -1    
        


checkPerfectArray(n,arr)       