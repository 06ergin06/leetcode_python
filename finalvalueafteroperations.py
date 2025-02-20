# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description/
class Solution(object):
    def finalValueAfterOperations(self, operations):
        y = 0
        for op in operations:
            if op == "++X" or op == "X++":
                y += 1
            elif op == "--X" or op == "X--":
                y -= 1
        return y