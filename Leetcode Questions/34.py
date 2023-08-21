def position(nums,target):
    lo,hi=0,len(nums)-1

    while lo <= hi:
        mid = (lo+hi)//2

        if nums[mid] == target:
            lo = hi = mid
            while lo > 0 and nums[lo - 1] == target:
                lo -= 1
            while hi < len(nums) - 1 and nums[hi + 1] == target:
                hi += 1
            return lo, hi
            
        elif nums[mid] <= target:
            lo = mid+1
        else:
            hi = mid-1

    return -1,-1


nums = [4,4,4,4,0] 
target = 4

result = position(nums,target)

print(result)