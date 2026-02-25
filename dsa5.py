class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        result = [1] * n
        pre = 1
        suf = 1
        # prefix calc. i.e. multi.. numbers starting from left side, with 0 index 1, 
        # it leads to leave the last number and the number at that index get multiplied to next iteration in number. 

        # prefix calc
        for i in range(n):
            result[i] = pre
            pre = pre * nums[i] 
        # suffix calc i.e. start from last number, the number at a particular index get multiplied in next iteration. 
        for i in range(n-1, -1, -1):
            result[i] =  result[i] * suf
            suf = suf * nums[i]
        return result 
        
