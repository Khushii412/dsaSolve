class Solution(object):
    def threeSum(self, nums):
        nums.sort() # sorting so that we know where to move 
        result = []
        for i in range(len(nums)): # iteration
            if i>0 and nums[i]==nums[i-1]: # skipping duplicate values
                continue
            left = i+1
            right = len(nums) - 1
            while left < right: # checking sum , while to not use loop unnecesarily 
                
                total = nums[i] +nums[left] + nums[right]
                if total < 0: #move pointers
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i],nums[left] ,nums[right]]) # append in result array
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]: # moving if same value appears
                        left+=1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
        return result 
        
