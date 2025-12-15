class Solution:
    def repeatedCharacter(self, s: str) -> str:
        d = {}
        for i in s:
            if i in d.keys():
                return i    # Yaha i already d ke keys me hai aur  agar fir vahi aya isliye return kardo kyuki 1st to come twice print return karna hai
            else:
                d[i] = 1    
        