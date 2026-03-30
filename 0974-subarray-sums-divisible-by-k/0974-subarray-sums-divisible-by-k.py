class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        current_sum = 0
        unordered_dict = {0:1}
        ans = 0
        for i in nums:
            current_sum += i
            remainder = current_sum % k
            if remainder in unordered_dict:       
                ans = ans + unordered_dict[remainder]
            unordered_dict[remainder] = unordered_dict.get(remainder , 0) + 1
        return ans
        