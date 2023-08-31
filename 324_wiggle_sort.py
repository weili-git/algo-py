class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 3,6,2,5,1,4 先奇数位降序放置，再偶数位降序放置。这样可能存在的重复数字不会相撞
        nums.sort()
        n = len(nums)
        res = [0] * n
        for i in range((n)//2):
            res[i*2+1] = nums[n-1-i]
        for i in range((n+1)//2):
            res[i*2] = nums[n-1-n//2-i]
        # ! nums = res
        nums[:] = res[:]

    # def wiggleSort(self, nums):
    #     nums.sort()
    #     half = len(nums[::2])
    #     nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]