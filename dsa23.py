class Solution(object):
    def maxProduct(self, nums):
        max_p = min_p = result = nums[0] # storing value at index 0
        n = len(nums)
        for i in range(1,n): # starting from index 1
            num = nums[i]
            t_max = max(num, num*max_p, num*min_p) # compare and store because 2 neg = positive
            t_min = min(num, num*max_p, num*min_p)
            max_p = t_max
            min_p = t_min
            result = max(result, max_p)
        return result
        
