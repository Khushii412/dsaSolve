class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        if k>n:
            k = k%n
        nums.reverse() # reverse the whole array
        nums[:k] = reversed(nums[:k]) # reverse first k elements
        nums[k:] = reversed(nums[k:]) # reverse remaining n-k elements.
        
        
        
