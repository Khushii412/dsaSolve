class Solution(object):
    def intersection(self, nums1, nums2):
        set1 = set(nums1)
        result = set()
        for num in nums2:
            if num in set1:
                result.add(num)
        return list(result)
        # convert one arr into set , then apply loop to check if num in arr2 apear in arr1 (set1) if occur add it to resulting set . 
      #return in list format. 
      # (more compact version)
      #class Solution(object):
      #def intersection(self, nums1, nums2):
       # return list(set(nums1) & set(nums2))
