def search(nums,target):
    lo, hi = 0, len(nums) - 1

    while lo <= hi :
        mid = ( lo + hi )//2
        
        if nums[mid] == target:
            return True
        if nums[lo] == nums[mid] == nums[hi]:
            lo += 1
            hi -= 1
        if nums[lo] <= nums[mid]:
            #left side is sorted
            if nums[lo] <= target <= nums[mid] :
                hi = mid-1
            else :
                lo = mid+1
        else :
            if nums[mid] < target < nums[hi] :
                lo = mid+1
            else:
                hi = mid-1

    return False



nums = [1,0,1,1,1]
target = 0

result = search(nums,target)

print(result)