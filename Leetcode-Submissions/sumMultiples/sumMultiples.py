class Solution(object):
    def sumOfMultiples(self, n):
        l = []
        for i in range(1,n+1):
            if i%3 == 0 or i%5 == 0 or i%7 == 0:
                l.append(i)
        s = sum(l)
        return s