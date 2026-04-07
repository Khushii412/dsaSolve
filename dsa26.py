class Solution(object):
    def findMaxAverage(self, nums, k):
        window = sum(nums[:k])
        max_sum = window
        for right in range(k,len(nums)): # start from k postn
            window += - nums[right-k]+nums[right] # remove left and right element
            max_sum = max(window, max_sum)
        return float(max_sum) / k # for exact float value
