class Solution(object):
    def trap(self, height):
        left_max=0
        right_max=0
        water= 0
        left = 0
        right = len(height)-1
       
        while left < right:
            if height[left] < height[right]:
                left_max = max(height[left], left_max)
                water += left_max - height[left]
                left += 1
            else:
                right_max = max(height[right], right_max)
                water += right_max - height[right]
                right -= 1
        return water 
        # after each iteration when pointer move it revaluates height[left] , and height[right]
