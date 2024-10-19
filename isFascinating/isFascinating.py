class Solution(object):
    def isFascinating(self, n):
        n_2 = n*2
        n_3 = n*3
        x = str(n)
        x += str(n_2)
        x += str(n_3)      
        l = set(x)
        if len(x) == 9 and '0' not in x:
            if l == {'1','2','3','4','5','6','7','8','9'}:
                return True
        else:
            return False        