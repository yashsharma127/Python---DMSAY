

def search(nums):
    n = len(nums)

#Edge cases
    if n == 1:
        return nums[0]
    if nums[0] != nums[1]:
        return nums[0]
    if nums[n-1] != nums[n-2]:
        return nums[n-1]


#main algo
    lo,hi = 1,n-1
    while lo <= hi:
        mid = (lo+hi) //2

        if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
            return nums[mid]
        #most important condition
        elif(mid % 2 == 0 and nums[mid] == nums[mid+1]) or (mid % 2 == 1 and nums[mid] == nums[mid-1]):
            lo  = mid+1
        else:
            hi = mid-1

    return -1
    
nums = [1,1,2,2,3,3,4,4,5,8,8]
result = search(nums)
print(result)

