# https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description/
class Solution(object):
    def getSneakyNumbers(self, nums):
        i = 0
        lists = []
        while i < len(nums):
            if nums.count(nums[i]) == 2:
                lists.append(nums[i])
                nums =  list(filter(lambda x: x != nums[i], nums))
            i += 1
        return lists