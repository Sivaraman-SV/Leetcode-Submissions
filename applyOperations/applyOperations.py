class Solution(object):
    def applyOperations(self, nums):
        n = len(nums)
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                nums[i]*=2
                nums[i+1] = 0
            else:
                pass
        for j in range(n):
            if nums[j] == 0:
                nums.remove(nums[j])
                nums.append(0)
        return nums
        