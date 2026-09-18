class Solution(object):
    def intersect(self, nums1, nums2):
        common = list(set(nums1).intersection(set(nums2)))
        l = []
        for i in common:
            x = nums1.count(i)
            y = nums2.count(i)
            for j in range(min(x,y)):
                l.append(i)
        return sorted(l)