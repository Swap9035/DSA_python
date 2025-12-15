class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        d = {} # Make a dictionary of stones where will store the frequency(No. of time alpahbet occurs) as values
        for i in stones:
            if i in d.keys():
                d[i] += 1
            else:
                d[i] = 1
        # We got the frequency now check whether its a jewel if it is then count == Freq
        count = 0
        for i in d.keys():
            if i in jewels:
                count +=d[i] # d[i] its basically values(here freq)
        return count                      

        