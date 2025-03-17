# https://leetcode.com/problems/divide-array-into-equal-pairs/description/
class Solution(object):
    def divideArray(self, nums):
        if len(nums) % 2 != 0:
            return False
        nums = sorted(nums)
        for i in range(0,len(nums) + 1,2):
            if i < len(nums) and nums[i] == nums[i+1]:
                continue
            else:
                return False
        return True