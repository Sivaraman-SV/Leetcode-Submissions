class Solution(object):
    def multiply(self, num1, num2):
        l = []
        l.append(num1)
        l.append(num2)
        for i in range(len(l)-1):
            prod = int(l[i])*int(l[i+1])
        return str(prod)