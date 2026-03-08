class Solution(object):
    def pivotIndex(self, nums):
        total = sum(nums)
        left = 0
        for i in range(len(nums)):
            if left == total - left - nums[i]: # check if left(right) meets the condn
                return i # if condition satisfied return and break loop
            left += nums[i]
            
        return -1 # if no index found return -1
        
