class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        sum = 0
        d = {}
        for i in nums:
            if i in d.keys():
                d[i]+=1
            else:
                d[i]=1
        for i in d.keys():
            if d[i] == 1: # Unique ele will have freq 1 coz they will come oonly one time 
                sum = sum + i
        return sum        
        