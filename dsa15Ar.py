class Solution(object):  # o(n) time lookup
    def runningSum(self, nums):
        prefix_sum = 0
        result = []
        for num in nums:
            prefix_sum += num
            result.append(prefix_sum)
        return result
        #nums =
#[1,2,3,4]
#Output
#[1,3,6,10]
class Solution(object):    # in place approach for 0(1) space lookup
    def runningSum(self, nums):
        for i in range(1, len(nums)):
            nums[i] = nums[i]+nums[i-1]
        return nums
