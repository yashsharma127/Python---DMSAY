class MaxFinder:
    def __init__(self,nums):
        self.nums = nums
        self.maxim = None

    def linearUnsorted(self):
        if not self.nums:
            return None
        self.maxim = self.nums[0]
        for num in self.nums:
            if num > self.maxim:
                self.maxim = num
        return self.maxim
    
    
nums = [12, 100, 7, 23, 67, 89]
findMax = MaxFinder(nums)
max_linear = findMax.linearUnsorted()

print(max_linear)