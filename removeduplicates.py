# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
class Solution(object):
    def removeDuplicates(self, nums):
        nums[:] = sorted(set(nums)) 
        """
        The difference between nums[:] = and nums = is that the latter doesn't replace elements in the original list.
        *nums = not accepted*
        """
        return len(nums)
        