#The isBadVersion API is already defined for you.
#@param version, an integer
#@return a bool
#def isBadVersion(version):
class Solution(object):
    def firstBadVersion(self, n):
        s = 1
        l = n
        while s<l:
            m = (s+l)//2
            if isBadVersion(m):
                l = m
            else:
                s = m + 1
        return l