class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Sliding window problem because all elements are given positive 
        # We will find continuous sum 1st then if the sum is greater or equal to the target then we shrink the window from left and shift to next element
        left = 0
        current_sum = 0
        min_len = float('inf') # set to infinity to find most min
        for right in range(len(nums)):
            current_sum += nums[right]

            while current_sum >= target:
                min_len = min(min_len , right - left + 1) # Gives min len before shrinking (We are doing this before  coz once we shrink og window is gone)
                current_sum -= nums[left] # removes the leftmost ele
                left +=1 # shifts a window to right
        return 0 if min_len == float('inf') else min_len        

                
        
        