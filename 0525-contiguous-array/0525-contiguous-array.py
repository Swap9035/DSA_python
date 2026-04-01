class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zero = 0
        one = 0
        hash = {0 : -1}
        res = 0

        for i in range(len(nums)):

            if nums[i] == 0:
                zero +=1
            else:
                one +=1
            
            diff = zero - one
            if diff  in hash:
                length = i - hash[diff]
                res = max(length , res)
            else:
                hash[diff] = i
        return res