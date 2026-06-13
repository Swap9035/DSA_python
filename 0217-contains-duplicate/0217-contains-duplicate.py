class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for i in nums:
            seen[i] = seen.get(i,0) + 1

        for i , count in seen.items():
            if count >= 2:
                return True 
        return False
        