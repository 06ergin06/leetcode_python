# https://leetcode.com/problems/three-divisors/description/
class Solution(object):
    def isThree(self, n):
        y = 0
        for i in range(1,n+1):
            if n % i == 0:
                y += 1
            if y == 4:
                break
        return y == 3