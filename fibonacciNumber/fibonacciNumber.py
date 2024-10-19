class Solution(object):
    def fib(self, n):
        l = [0,1]
        l2 = l
        for i in range(0,31):
            l[0] = 0
            l[i] = l[i-1] + l[i-2]
            l2.append(l[i])

        for j in range(len(l2)):
            if j == n:
                return l2[j]

