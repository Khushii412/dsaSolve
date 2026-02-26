class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        xorall = 0
        
        for num in range(n+1):
            xorall ^= num
        for num in nums:
            xorall ^= num
        return xorall
        # xor cancel the same number i.e. a^a = 0, and a^0 = a, a^b^a = b , sequence doesnt matter, if num is same it cancels.
# we use loop 2 times , once to get xor of values, then to get xor of values but range is len(arr)+1 , as len takes fron 0 to n-1, so to get 0 to all elements , n+1.
        
