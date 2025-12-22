class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Current_sum - k = old_sum  
        current_sum = 0
        sum_count = {0:1} # Use to store prefix sum (Continuous sum) --> old sum
        answer = 0
        for i in  nums:
            current_sum +=i # Adds the current ele to prefix sum 
            if current_sum - k in sum_count:
                answer  += sum_count[current_sum - k] #“If I have seen a prefix sum equal to (current_sum - k), then a subarray with sum k exists.”
            sum_count[current_sum] = sum_count.get(current_sum , 0) + 1 #Inc the frequency of prefix sum
        return answer    


        