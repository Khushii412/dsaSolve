class Solution(object):
    def subarraySum(self, nums, k):
        prefix_count = {0:1} #to store sum and its frequency
        count = 0 # total valid sub arrays
        cur_sum = 0 # sum at each iteration
        for num in nums: # iterate the loop to get num
            cur_sum += num
            # cur_sum - k = prev_sum , if prev sum in prefix_count
            # then increase the count  
            if cur_sum - k in prefix_count:
                count += prefix_count[cur_sum - k]
                print(count) # to observe increase
        # this to increase the frequency, i.e. val for a key, using get(cur, 0) to get the val if key exist else return 0, then increase val of key by one
            prefix_count[cur_sum] = prefix_count.get(cur_sum, 0) + 1
        return count
        
