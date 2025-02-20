# https://leetcode.com/problems/build-array-from-permutation/description/
class Solution(object):
    def buildArray(self, nums):
        list = []
        for i in range(0,len(nums)):
            list.append(nums[nums[i]])
        return list         