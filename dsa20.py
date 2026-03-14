class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]
        # loop for 3-sum (causes- o(n^2))
        for i in range(len(nums)):
            left = i+1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right] # get total for each iteration
                if abs(total - target) < abs(closest - target): # compare the difference betn total and closest 
                    closest =  nums[i] + nums[left] + nums[right] # store the value closest to target in "closest"
                if total < target: # update pointers
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    return total # return if condn satisfied
                
        return closest
            

        
