class Solution(object):
    def check(self, nums):
        n = len(nums)
        count = 0
        for i in range(n): # We need to check till n-1   
            next = (i +1) % n # mod is used in circular array to prevent going out of bound
            if nums[i] > nums[next]:
                count +=1
        return(count <=1)