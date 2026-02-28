class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding window will be used 
        # we will actually remove and shift the left window when the same element comes 
        char_set = set() # set is used because we only care wheter the char exits not abt its count
        longest = 0
        left = 0
        for right in range(len(s)):
            while s[right] in char_set: # Check if the char is already in set 
                char_set.remove(s[left]) # By this we shrink the window from left till we get distinct char
                left +=1
            char_set.add(s[right])
            longest = max(longest , right - left + 1 ) # This gives the max of all the substring . For eg. right = 5 left = 2 -> 5 - 2 + 1 = 4(len = 4)
        return longest        


        ### Code usig dictionary ###

        #   freq = {} , left = 0 , longest = 0
        #   for right in range(len(s)):
        #         freq[s[right]] = freq.get(s[right],0)+1
        #          while freq[s[right]] > 1:
        #               freq[s[left]] -=1  
        #               left+=1
        #          longest = max(longest, right - left + 1)
        #  
        #    return longest
        #       













        