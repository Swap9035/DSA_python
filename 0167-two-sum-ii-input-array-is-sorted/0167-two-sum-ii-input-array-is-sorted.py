class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(numbers)):
            needed = target - numbers[i]
            if needed in seen:
                return[seen[needed]+1,i+1] 
            seen[numbers[i]] = i    
        