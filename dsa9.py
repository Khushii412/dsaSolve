class Solution(object):
    def majorityElement(self, nums):
        count = 0
        candidate = None
        for i in nums:
            if count == 0:
                candidate = i
            if i == candidate:
                count += 1
            else:
                count -= 1
        return candidate
        # return element which appears most. 
      # count to track the no. of occurance , increase is same number appears, else decrease. 
      # candidate store the element.
