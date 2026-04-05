class Solution(object):
    def sortColors(self, nums):
        low=mid=0
        high = len(nums)-1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid+= 1
            else:
                nums[mid], nums[high] = nums[high] , nums[mid]
                high -= 1
              # use 3 pointer , mid is moving pointer, low and high from last , 3 condn i.e. 0 1 2, 
