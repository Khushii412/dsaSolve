class Solution(object):
    def twoSum(self, nums, target):
        # empty dictionary
        seen={}
        # loop to get value and index using enumerate
        for i, num in enumerate(nums):
            need = target - num
            if need in seen:
                return [seen[need], i]
            seen[num]=i
# two sum . sum of any 2 element to get the target element. need var contain target-num . seen is a dictionary . 
