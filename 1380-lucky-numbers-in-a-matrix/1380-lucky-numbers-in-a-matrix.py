class Solution(object):
    def luckyNumbers(self, matrix):
        row = len(matrix)
        col = len(matrix[0])
        mi , ma = [] , []
        for i in matrix:
            mi.append(min(i))
        for i in range(col):
            maxi = -1
            for j in range(row):
                if matrix[j][i] > maxi:
                    maxi = matrix[j][i]
            ma.append(maxi)
        num = []
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == mi[i] and matrix[i][j] == ma[j]:
                    num.append(matrix[i][j])
        return num