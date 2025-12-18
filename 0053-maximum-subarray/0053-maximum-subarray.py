class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = 0 # Best subarray fo given index
        max_sum = nums[0] # Best sub array so far
        for i in nums:
            current_sum += i 
            max_sum = max(max_sum,current_sum)
            if current_sum < 0 :
                current_sum = 0
              
        return max_sum            

        