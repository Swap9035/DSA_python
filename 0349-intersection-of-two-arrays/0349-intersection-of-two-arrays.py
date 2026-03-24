class Solution:
    def intersection(self, nums1, nums2):
        seen = set(nums1)
        res = set()

        for num in nums2:
            if num in seen:
                res.add(num)

        return list(res)



        