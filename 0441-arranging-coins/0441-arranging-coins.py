class Solution(object):
    def arrangeCoins(self, n):
        s = 0
        c = 0
        steps = 1
        while s<=n:
            s = s + (2*steps-steps)
            steps+=1
            if s<=n:
                c+=1
        return c