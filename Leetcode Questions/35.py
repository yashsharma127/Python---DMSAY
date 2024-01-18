def searchInsert( nums, target):
        lo,hi = 0,len(nums)-1
        print(nums,target)
        while lo <= hi:
            mid = (lo+hi)//2
            print(mid)
            if nums[mid] == target:
                return mid+1
            elif nums[mid] > target:
                lo = mid+1
               
            else:
                hi = mid-1
                
        return 0


nums = [1,3,5,6]
target = 5
result = searchInsert( nums,target)
print(result)