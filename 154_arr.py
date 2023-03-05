class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left<right:
            if nums[left]<nums[right]:
                return nums[left]   # no rotation
            else:
                mid = left + (right-left)//2
                if nums[mid]>=nums[left]:   # be careful
                    left = mid + 1
                elif nums[mid]<nums[right]:
                    right = mid
        return nums[left]

        # [2, 1]