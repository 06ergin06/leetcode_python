# https://leetcode.com/problems/fibonacci-number/description/
class Solution(object):
    def fib(self, n):
        if n == 0 or n == 1:
            return n
        else:
            return self.fib(n - 1) + self.fib(n - 2)