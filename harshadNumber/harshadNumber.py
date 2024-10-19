class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        l = list(str(x))
        for i in range(len(l)):
            l[i] = int(l[i])
        summ = sum(l)
        if x%summ == 0:
            return summ
        else:
            return -1