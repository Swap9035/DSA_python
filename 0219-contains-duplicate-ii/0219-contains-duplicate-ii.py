class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        for i in range(len(nums)):
            if nums[i] in seen:
                if i - seen[nums[i]] <= k:# i-> current index seen[nums[i]]->seen[value]->returns the index of that value in seen 
                    return True 
            seen[nums[i]] = i # Stores the currnt latest index where value appeared so that can later directly check for diff     
        return False         



        