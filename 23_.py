dic1 = {1:10, 2:20} 
dic2 = {3:30, 4:40} 
dic3 = {5:50, 6:60}
nums = dict(list(dic1.items())+list(dic2.items())+list(dic3.items()))
nums[7]=70
minimum = min(nums.values())
print (minimum)
