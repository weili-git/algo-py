import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        mid = (m+n)//2
        # if m==0:
        #     if n%2==0:
        #         return (nums2[n//2-1] + nums2[n//2]) / 2.0
        #     else:
        #         return nums2[n//2]
        # if n==0:
        #     if m%2==0:
        #         return (nums1[m//2-1] + nums1[m//2]) / 2.0
        #     else:
        #         return nums1[m//2]

        i, j, k = 0, 0, 0
        m1, m2 = 0, 0
        while k<=mid and (i<m or j<n):
            m1 = m2
            if i==m or (i!=m and j!=n and nums2[j] < nums1[i]): # merge
                m2 = nums2[j]
                j += 1
            else:
                m2 = nums1[i]
                i += 1
            k += 1
        if (m+n)%2==1:
            return m2
        return (m1+m2)/2

    def solution(self, nums1: List[int], nums2: List[int]) -> float:    # log(m+n)
        m = len(nums1)
        n = len(nums2)
        left = (m+n+1)//2
        right = (m+n+2)//2
        return (self.getKth(nums1, 0, m-1, nums2, 0, n-2, left) + self.getKth(nums1, 0, m-1, nums2, 0, n-1, right)) * 0.5

    def getKth(self, nums1, start1, end1, nums2, start2, end2, k):
        len1 = end1 - start1 + 1
        len2 = end2 - start2 + 1
        if len1 > len2:
            return self.getKth(nums2, start2, end2, nums1, start1, end1, k)
        if len1 == 0:
            return nums2[start2+k-1]
        if k==1:
            return math.min(nums1[start1], nums2[start2])
        i = start1 + math.min(len1, k//2) - 1
        j = start2 + math.min(len2, k//2) - 1
        if nums1[i] > nums2[j]:
            return self.getKth(nums1, start1, end1, nums2, j+1, end2, k-(j-start2)+1)
        else:
            return self.getKth(nums1, i+1, end1, nums2, start2, end2, k-(i-start1)+1)



