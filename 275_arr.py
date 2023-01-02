class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # log time complexity\
        n = len(citations)
        right = len(citations) - 1
        left = 0
        res = 0
        while left <= right:
            mid = left + (right-left)//2
            h = n - mid
            if h <= citations[mid]:
                right = mid - 1
                res = h
            else:
                left = mid + 1
        return res
        # n = len(citations)
        # right = len(citations) - 1
        # left = 0
        # while left < right:
        #     mid = left + (right-left)//2
        #     h = n - mid
        #     if h <= citations[mid]:
        #         right = mid
        #     else:
        #         left = mid + 1
        # if citations[left]>=n-left:
        #     return n-left
        # else:
        #     return 0


# 本题不可能同时存在多个h，证明过程如下： 
# 存在一个符合题目条件的数组，使得h=n，h=m，其中m>n，根据题目描述，意味着该数组中，存在以下两个命题： 
# [0,0,0,0,h,h,h,h]
# 1，有且仅有n个数皆大于等于n 
# 2，有且仅有m个数大于等于m
# 但是由于m>n,所以命题2成立时，命题1一定不成立，即两者不可能同时成立。