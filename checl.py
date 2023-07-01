 

# def find_max(nums):
# #    max_num = float("-inf") # smaller than all other numbers
#      max_num=nums[0]
#      for num in nums:
#                 if num > max_num:
#                      max_num=num
#                 return max_num
     
def find_max(nums):
     max_num = nums[0]
     for num in nums:
          if num>max_num:
               max_num=num
     return max_num           


a=[62,8,9,5,34]
res=find_max(a)
print("max:",res)