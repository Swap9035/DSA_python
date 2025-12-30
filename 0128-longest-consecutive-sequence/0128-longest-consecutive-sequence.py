class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums) # Set is used here as it reduces the complexityyy
        longest = 0

        for i in nums_set:
            if i - 1 not in nums_set: # Used to check whether i is the the 1st no. coz we will start countinh from 1st ele onllyy
                current = i
                length = 1
                while current + 1 in nums_set: # checks if next eles are in set
                    current +=1
                    length +=1
                longest = max(longest,length) # Gives the max length using max 
        return longest        







        