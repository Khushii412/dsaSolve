class Solution(object):
    def maxSubArray(self, nums):
        max_s = nums[0]
        cur_sum = nums[0]
        for i in range(1,len(nums)):
            cur_sum = max(nums[i], nums[i]+cur_sum)
            max_s = max(max_s, cur_sum)
        return max_s
      
