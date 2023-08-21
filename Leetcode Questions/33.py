def search(nums, target):
    lo,hi=0,len(nums)-1
    while lo <= hi:
        mid = (lo+hi)//2

        if nums[mid] == target:
            return mid
        
        if nums[lo] <= nums[mid]:
            #this mean left part is sorted
            if nums[lo] <= target <= nums[mid]:
                hi = mid-1
            else:
                lo = mid+1
        else: 
            if nums[mid] <= target <= nums[hi] :
                lo = mid+1
            else:
                hi = mid-1

    return -1


    
nums = [4,5,6,7,0,1,2,3] 
target = 0
result = search(nums,target)

print(result)