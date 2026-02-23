class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff  = float('inf')
        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1
            while left < right:
                total_sum = nums[i] + nums[left] + nums[right]
                d = abs(target - total_sum)
                if d < diff:
                    diff = d 
                    result_sum = total_sum
                if total_sum == target:
                    return result_sum
                elif total_sum < target:
                    left +=1
                else:
                    right -=1
        return result_sum

        