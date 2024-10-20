class Solution(object):
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers) - 1
        while left < right:
            summ = numbers[left] + numbers[right]

            if summ == target:
                return [left+1,right+1]
            if summ < target:
                left+=1
            elif summ > target:
                right-=1