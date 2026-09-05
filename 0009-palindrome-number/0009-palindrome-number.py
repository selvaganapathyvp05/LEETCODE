class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        n = x
        c = 0
        while n!=0:
            c=c*10 + n%10
            n//=10
        return x==c