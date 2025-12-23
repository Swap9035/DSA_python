class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # Two pointers will be used here
        j = 0 # --> decides position for next non zero 
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i],nums[j] = nums[j],nums[i]
                j +=1
           
      
        