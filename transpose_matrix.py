# https://leetcode.com/problems/transpose-matrix/description/
class Solution(object):
    def transpose(self,matrix):
        col = len(matrix[0])
        row = len(matrix)
        transMatrix = [[0 for _ in range(row)] for _ in range(col)]
        for i in range(0,row):
            for j in range(0,col):
                transMatrix[j][i] = matrix[i][j]
        return transMatrix