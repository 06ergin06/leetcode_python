# https://leetcode.com/problems/smallest-even-multiple/description/
class Solution(object):
    def smallestEvenMultiple(self, n):
        if n % 2 == 0:
            return n
        else: 
            return n * 2