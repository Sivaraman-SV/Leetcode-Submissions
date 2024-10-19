class Solution(object):
    def isPalindrome(self, s):
        strlist = s.split()
        l = []
        for i in strlist:
            for j in i:
                if j.isalnum():
                    l.append(j)
        print(l)
        res = ''
        for i in range(len(l)):
            res += l[i]
        res = res.lower()
        print(res)
        if res == res[::-1]:
            return True
        else:
            return False
            
        