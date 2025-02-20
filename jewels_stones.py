#https://leetcode.com/problems/jewels-and-stones/description/
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        y = 0
        for i in range(0,len(jewels)):
            y += stones.count(jewels[i])
        return y