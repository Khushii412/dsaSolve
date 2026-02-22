class Solution(object):
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))
    # check if array conatins any duplicate element. if yes then return true else false
