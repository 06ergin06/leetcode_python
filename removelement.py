# https://leetcode.com/problems/remove-element/description/
class Solution(object):
    def removeElement(self, nums, val):
        numss = []
        for x in nums:
            if x != val:
                numss.append(x)
        nums[:] = numss
        return len(nums)   
 