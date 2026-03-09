class Solution(object):
    def sortedSquares(self, nums):
        n = len(nums)
        result = [0] * n
        left = 0 # left ptr posn
        right = n-1 # right ptr posn
        pos = n-1 # from here we start filling result
        while left<=right: # loop iterates as long as left is <= right
            if abs(nums[left])>abs(nums[right]):  # if abs val at left pos is greater store sq.     of left else sq. of right
                result[pos] = nums[left] ** 2
                left += 1
            else:
                result[pos] = nums[right] ** 2
                right -= 1
            pos -= 1
        return result
        

        
