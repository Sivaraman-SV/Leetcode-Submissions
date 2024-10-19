class Solution(object):
    def plusOne(self, digits):
        a = ""
        for i in digits:
            a += str(i)
        a = int(a)
        a = a+1
        b = list(str(a))
        for i in range(len(b)):
            b[i] = int(b[i])
        return b
