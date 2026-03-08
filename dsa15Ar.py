class Solution(object):
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
