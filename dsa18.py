class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_area =0
        while left < right:
            # min height cause water can be held upto smaller pole
            h = min(height[left], height[right])
            # distance betn the index to find width
            width = right - left
            area = h*width
          # compare area after change of either of pointer .
            max_area = max(area, max_area)
            # increase pointer which is small.
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
        
