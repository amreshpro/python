# Prime Number

# 2,3,5,7,11
# 5-> 1,2,3,4,5 -> Divide by 1,5  # Prime, ODD
# 9 -> 1,2,3,4,5,,6,7,8,9 -> Divide by 1,3,9 # Not Prime , ODD
# even can be prime
# 9 odd may or may not be prime

def checkPrime(n):
    # even prime
    if n==1 : return "NO"
    if n==2: return "Yes"
    if n!=2 and n%2==0 : return "NO"
    #odd
    for i in range(3,n) :   #last value or n is not included
           if n%i==0:return "NO"
    return "Yes"       



print(checkPrime(1))
print(checkPrime(37))
print(checkPrime(-3))
print(checkPrime(49))
print(checkPrime(13))
print(checkPrime(267))
print(checkPrime(289))



# # n=36
# 6*6 
# #  37->  3......36
# # 36 -> 6*6
# # sqrt(36) = 6
# sqrt(37) = 6.33333
2-----
6%2==0
# # 
