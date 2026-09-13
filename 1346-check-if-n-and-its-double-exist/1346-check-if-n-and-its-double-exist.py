class Solution(object):
    def checkIfExist(self, arr):
        for i in arr:
            if (2*i) in arr and i!=0:
                return True
        return arr.count(0)>=2