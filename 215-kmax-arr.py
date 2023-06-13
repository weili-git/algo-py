from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickSearch(nums, k-1)

    def quickSearch(self, nums, k):
        l = 0
        r = len(nums) - 1
        pivot = nums[(l+r)//2]
        list = [i for i in nums if i>pivot]
        if len(list) == k:
            return pivot
        elif len(list) > k:
            return self.quickSearch(list, k)
        else:
            list_ = [i for i in nums if i<pivot] + [i for i in nums if i==pivot][1:]
            return self.quickSearch(list_, k-len(list)-1)

s = Solution()
a = s.findKthLargest([3,2,1,5,6,4], 2)
print(a)