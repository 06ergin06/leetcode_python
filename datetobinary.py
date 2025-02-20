# https://leetcode.com/problems/convert-date-to-binary/description/
class Solution(object):
    def convertDateToBinary(self, date):
        dates = date.split("-")
        rdates = ""
        for i in range(0, len(dates)):
            rdates += bin(int(dates[i]))[2:]
            if i < len(dates) - 1:
                rdates += "-"
        return rdates
