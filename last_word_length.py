# https://leetcode.com/problems/length-of-last-word/description/
class Solution(object):
    def lengthOfLastWord(self, s):
        lis = (s.strip()).split(" ")
        return len(lis[-1])  