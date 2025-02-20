# https://leetcode.com/problems/find-words-containing-character/description/
class Solution(object):
    def findWordsContaining(self, words, x):
        lst = []
        for i in range(0,len(words)):
            if x in words[i]:
                lst.append(i)
        return lst