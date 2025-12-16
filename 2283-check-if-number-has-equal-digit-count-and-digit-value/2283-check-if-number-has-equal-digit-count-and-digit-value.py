class Solution:
    def digitCount(self, num: str) -> bool:
    # Question says that every index in num should be present exactly the same no of times its value index 0 has value 1 so 0 should be present 1 time
       d ={}
       for i in num:
            if i in d.keys():
                d[i] += 1 
            else:
                 d[i] = 1 
       for i in range(len(num)):
            if d.get(str(i),0) == int(num[i]):
                 # get se hame voh value kitne baar ayi hai voh pata chalega and usko fir apan check karenge num ke us index ke value ke sath
                 continue
            else:
                return False
       return True            
         
            

        