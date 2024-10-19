class Solution(object):
    def addDigits(self, num):
        while num not in range(0,10):
            x = [] 
            sum1 = 0
            x = list(str(num))
            for i in range(len(x)):
                if type(x[i]) == str:
                    x[i] = int(x[i])
            print(x)
            numlist = []
            numlist = x      
            for i in numlist:
                sum1 += i
            num = sum1
        return num
        

