# https://leetcode.com/problems/binary-search/description/
class Solution(object):
    def search(self, nums, target):
        low = 0
        high = len(nums) - 1
        if(high >= low):
            while(high >= low):
                mid = (low + high) / 2 
                if target == nums[mid]:
                    return mid
                elif nums[mid] > target:
                    high = mid - 1 
                elif target > nums[mid]:
                    low = mid + 1
                else: 
                    return -1
        return -1