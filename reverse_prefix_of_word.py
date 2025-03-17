# https://leetcode.com/problems/reverse-prefix-of-word/description/
class Solution(object):
    def reversePrefix(self, word, ch):
        if ch in word:
            i = word.index(ch)
            return word[0:i + 1][::-1] + word[i + 1:]
        return word
