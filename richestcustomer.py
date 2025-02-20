#https://leetcode.com/problems/richest-customer-wealth/description/
class Solution(object):
    def maximumWealth(self, accounts):
        y = 0
        num = 0
        for i in range(0, len(accounts)):
            for j in range(i, len(accounts)):
                num = sum(accounts[i])
                y = max(y, num)
        return y