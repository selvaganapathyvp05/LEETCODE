class Solution(object):
    def reverseVowels(self, s):
        vow = ['A','E','I','O','U','a','e','i','o','u']
        v = ""
        for i in s[::-1]:
            if i in vow:
                v+=i
        ans =""
        l = 0
        for i in s:
            if i in vow:
                ans+=v[l]
                l+=1
            else:
                ans+=i
        return ans