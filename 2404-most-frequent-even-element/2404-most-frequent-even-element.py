class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i % 2 == 0:
                if i in d.keys():
                    d[i] +=1
                else:
                    d[i] = 1
        if not  d:
            return -1 #If the list is empty means no even values
        max_f = max(d.values())

        cand = (num for num , freq in d.items() if freq == max_f) #d.items() wil give tuples of key value pair if the freq is max freq then store it in num
        return min(cand) # we want min of two if freq is same            

        