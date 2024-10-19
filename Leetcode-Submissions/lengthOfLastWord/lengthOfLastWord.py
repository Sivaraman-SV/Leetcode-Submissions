class Solution(object):
    def lengthOfLastWord(self, s):
        s=s.lstrip()
        s=s.rstrip()
        a = s.split()
        for i in a:
            if a[-1] != " " and " " not in a[-1]:
                x = len(a[-1]) 
        return x
