class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # We will use sliding window here as our lenght(here k) is fixed 
        # We will 1st find the sum till the k and then slide the window by 1 . This can be done by adding the next element after k to our window sum and subtracting the 1st ele by this our window will shift by 1 
        window_sum = sum(nums[0:k]) # Gives sum till k
        max_sum = window_sum # Current max sum
        for i in range(k,len(nums)): # we want to calculate sum of next eles (here 4,5 coz length is 6 in 1eg given)
            window_sum += nums[i] # Adding new ele to window sum
            window_sum -= nums[i - k] # Subtracting 1st ele (Here in 1eg i = 4(currently) - 4(k given 4)= 0 (i.e 1st ele))
            max_sum = max(max_sum,window_sum) # Returns maximum sum out of all subarray
        return max_sum / k    # Returns avg



          



        

        