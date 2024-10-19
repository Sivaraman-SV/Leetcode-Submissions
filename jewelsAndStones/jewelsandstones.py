class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        count = 0
        x = list(jewels)        
        y = list(stones)

        for i in range(len(y)): 
            if y[i] in x:
                count+=1
        return count