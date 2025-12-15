class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # Create a dictionary of sentence then check if its len is 26
        d ={}

        for i in sentence:
            if i in d.keys():
                d[i] += 1
            else:
                d[i] = 1
        if len(d.keys()) == 26: #d.keys() will give a list([]) hence we can find length
            return True 
        else:
            return False        
        