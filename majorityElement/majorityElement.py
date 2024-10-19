class Solution(object):
    def majorityElement(self, nums):
        l=[]
        n = len(nums)
        x = n/2
        for i in nums:
            if i not in l:
                if nums.count(i)>x:
                    return i
