class Solution(object):
    def transpose(self, matrix):
        new = []
        for i in range(len(matrix[0])):
            tem = []
            for j in range(len(matrix)):
                tem.append(matrix[j][i])
            new.append(tem)
        return new