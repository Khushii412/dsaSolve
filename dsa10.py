class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        eSum = n*(n+1)//2 # esum= expected sum
        aSum = sum(nums) # aSum = actual sum
        return eSum - aSum # missing num is the difference betn them.
        
