class Solution(object):
    def longestConsecutive(self, nums):
        num_set = set(nums)
        longest = 0 # to store the length decalre outside loop 
        for num in num_set: # iterate loop through set  
            if num-1 not in num_set: # iterate loop through set for 0(1) lookup
                current = num # store the num in current to check condn for current num as current and not num. (else time complexity increases o(n2))
                length = 1
    
                while current+1 in num_set:
                    current += 1
                    length += 1
                longest = max(length, longest)
        return longest  
        
