class Solution(object):
    def missingNumber(self, nums):
        nums = sorted(nums)
        for i in range(0,len(nums)+1):
            if i not in nums:
                return i