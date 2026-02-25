class Solution(object):
    def moveZeroes(self, nums):
        # 2 pointer approach , 1 to maintain iteration through loop
        # 1 ptr to maintain index of non zero elements, 
        # whenever 1st gets a non-zero , swap with 2nd ptr
        left= 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1 # increament index
         
        
