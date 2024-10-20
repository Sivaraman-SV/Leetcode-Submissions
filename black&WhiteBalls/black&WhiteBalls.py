class Solution(object):
    def minimumSteps(self, s):
        #tried to do the brute-force solution and it was just messy, hence doing the two pointer solution.
        counter = 0
        left = 0
        right = len(s) - 1
        l = list(s)
        while left < right:
            if l[left] == '1' and l[right] == '0':
                l[left],l[right] = l[right],l[left]
                counter += (right - left)
            if l[left] == '0':
                left+=1
            elif l[right] == '1':
                right-=1
        return counter