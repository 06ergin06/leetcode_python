# https://leetcode.com/problems/sum-multiples/description/
class Solution(object):
    def sumOfMultiples(self, n):
        lst = [x for x in range(1,n) if x % 3 == 0 or x % 5 == 0 or x % 7 == 0]
        return sum(lst) 