class Solution(object):
    def intersection(self, nums1, nums2):
        l = []
        if len(nums1) > len(nums2):
            x = len(nums1)
            for i in range(x):
                if nums1[i] in nums2 and nums1[i] not in l:
                    l.append(nums1[i])
        elif len(nums2) > len(nums1):
            x = len(nums2)
            for i in range(x):
                if nums2[i] in nums1 and nums2[i] not in l:
                    l.append(nums2[i])
        elif len(nums1) == len(nums2):
            x = len(nums1)
            for i in range(x):
                if nums2[i] in nums1 and nums2[i] not in l:
                    l.append(nums2[i])
        return l