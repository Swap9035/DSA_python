class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # We will use lamda function here 
        d ={}
        # Here 2 strings are given we will take one as key one as its value . We will take height as key coz its value is not repeating We cant have       duplicates in key
        for i in range(len(names)):
            d[heights[i]] = names[i] # Made a dictionary with heights as keys 
        d = sorted(d.items() , key = lambda x:x[0] , reverse = True) # Here we applied sorted coz we want the values in sorted manner then reversed is true beacuse it will sort in asc we want in desc d.items() will give tuples of each key value and lamda function to get 1st value i.e key
        for i in range(len(d)):
            names[i] = d[i][1] # 1 coz its actually value i.e names 0 will be keys i.e heights and we want name 
        return names    

        