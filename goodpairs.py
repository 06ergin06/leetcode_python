# https://leetcode.com/problems/number-of-good-pairs/description/
class Solution(object):
    def numIdenticalPairs(self, nums):
        y = 0
        for i in range(0,len(nums)):
            for j in range(i + 1,len(nums)):
                if nums[i] == nums[j]:
                    y += 1
        return y