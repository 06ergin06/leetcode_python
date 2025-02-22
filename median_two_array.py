# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        lst = nums1 + nums2
        lst.sort()
        if len(lst) % 2 == 0:
            return (lst[len(lst) // 2] + lst[(len(lst) // 2 ) - 1]) / 2.0
        else:
              return  lst[len(lst) // 2] 
        