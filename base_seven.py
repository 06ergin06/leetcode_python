# https://leetcode.com/problems/base-7/description/
class Solution(object):
    def convertToBase7(self, num):
        if num == 0:
            return "0"
        seven_base = ""
        neg = num < 0 # boolean
        num = abs(num)
        while num != 0:
            seven_base = str(num % 7) + seven_base
            num = int(num / 7)
        if neg:
            seven_base = "-" + seven_base
        return seven_base
