class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left = 0
        for i in range(len(nums)):
            right = total_sum - nums[i] - left
            if(left == right):
                return i
            left += nums[i]
        return -1

    
    









        

        