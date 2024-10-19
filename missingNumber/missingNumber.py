class Solution(object):
    def missingNumber(self, nums):
       n = len(nums)
       l=[]
       for i in range(0,n+1):
          l.append(i)
       print(l)
       for j in range(len(l)):
          if l[j] not in nums:
            return j
  