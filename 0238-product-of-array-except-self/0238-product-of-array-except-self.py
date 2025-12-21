class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # logic : (Product of elements) * (product of right elements)
        n = len(nums)
        answer = [1] * n # answer = [1,1,1,1] coz len=4
        # For left product
        left = 1
        for i in range(n): # 0,1,2,3
            answer[i] = left
            left = left * nums[i]
        # For right prod
        right = 1
        for i in range(n-1,-1,-1): # 3,2,1,0
            answer[i] = answer[i] * right
            right = right * nums[i]
        return answer    

        