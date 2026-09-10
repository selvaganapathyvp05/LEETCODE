class Solution(object):
    def peakIndexInMountainArray(self, arr):
        st, ed = 0, len(arr) - 1
        while st < ed:
            m = (st + ed) // 2
            if arr[m] < arr[m + 1]:
                st = m + 1
            else:
                ed = m
        return st