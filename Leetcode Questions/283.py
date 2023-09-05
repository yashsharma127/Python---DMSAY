## 1st
class Solution(object):
    def moveZeroes(self, nums):
        left, right = 0, 1
        while right < len(nums):
            if nums[left] == 0:
                if nums[right] != 0:
                    nums[left] = nums[right]
                    nums[right] = 0
                    left += 1
                    right += 1
                else:  # You can remove the condition 'elif nums[right] == 0' because it's not needed
                    right += 1
            else:
                left += 1
                right += 1

# Example usage:
sol = Solution()
nums1 = [0, 1, 0, 3, 12]
sol.moveZeroes(nums1)
print(nums1)  # Output: [1, 3, 12, 0, 0]

nums2 = [0]
sol.moveZeroes(nums2)
print(nums2)  # Output: [0]




## 2nd
def moveZeroes(nums):
    nonZeroPtr = 0  # Points to the position where non-zero elements should be placed
    
    for currentPtr in range(len(nums)):
        if nums[currentPtr] != 0:
            # Swap the non-zero element to the correct position
            nums[nonZeroPtr], nums[currentPtr] = nums[currentPtr], nums[nonZeroPtr]
            nonZeroPtr += 1

# Example usage:
nums1 = [0, 1, 0, 3, 12]
moveZeroes(nums1)
print(nums1)  # Output: [1, 3, 12, 0, 0]

nums2 = [0]
moveZeroes(nums2)
print(nums2)  # Output: [0]


