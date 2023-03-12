class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def get(idx):
            if idx==-1 or idx==n:
                return float("-inf")
            return nums[idx]
        n = len(nums)
        left, right = 0, n-1
        ans = -1
        while left<=right:
            mid = left + (right-left)//2
            if get(mid-1)<get(mid) and get(mid)>get(mid+1):
                return mid
            else:
                if get(mid) < get(mid+1):
                    left = mid + 1
                else:
                    right = mid - 1
        return ans