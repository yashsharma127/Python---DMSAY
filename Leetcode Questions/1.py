# Brute  force
def twosum(nums, target):
    n = len(nums)
    for i in range(n):
        element1 = nums[i]
        for j in range(i+1,n):
            element2 = nums[j]
            sum = element1+element2
            if sum == target:
                return i,j 
           

# Optimal using hash map
def twoSum( nums, target):
    num_indices = {}        
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_indices:
            return num_indices[complement], i                 
        num_indices[num] = i    
    return None 





nums = [3,3]
target = 6

result = twosum(nums,target)
print(result)

