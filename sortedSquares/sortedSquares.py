class Solution(object):
    def sortedSquares(self, nums):
        '''for i in range(len(nums)):
            nums[i]= nums[i]**2
        nums.sort()
        return nums --- this was pretty easy but i want to do it using two pointers approach.'''
        for i in range(len(nums)):
            nums[i]= nums[i]**2
        left = 0
        right = len(nums) - 1
        result = [0]*len(nums)
        index = len(nums) - 1
        while left <= right:
            if nums[left] > nums[right]:
                result[index] = nums[left]
                left += 1
            else:
                result[index] = nums[right]
                right -= 1
            index -= 1
        return result