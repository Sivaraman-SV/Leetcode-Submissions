class Solution(object):
    def majorityElement(self, nums):
        n = len(nums)
        x = n/3
        l=[]
        for i in nums:
            if i not in l:
                if nums.count(i)>x:
                    l.append(i) 
        return l    
        