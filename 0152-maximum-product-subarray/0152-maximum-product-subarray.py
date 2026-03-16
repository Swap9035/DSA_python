class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        max_prod = nums[0]
        min_prod = nums[0]
        for i in nums[1:]:
            v1 = i
            v2 = max_prod  * i
            v3 = min_prod * i

            max_prod = max(v1 , max(v2,v3))
            
            min_prod = min(v1 , min(v2,v3))

            result = max(result , max_prod)

        return result
        