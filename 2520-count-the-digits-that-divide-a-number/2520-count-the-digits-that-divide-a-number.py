class Solution(object):
    def countDigits(self, num):
        n = num
        c = 0
        while n!=0:
            if num%(n%10)==0:
                c+=1
            n//=10
        return c