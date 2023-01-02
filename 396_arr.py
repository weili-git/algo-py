class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        if n<=1:
            return 0
        init_val = 0
        s = sum(nums)
        for i in range(n):
            init_val += i*nums[i]
        maxv = -float("inf")
        for j in range(n):
            init_val = init_val + s - n*nums[n-1-j]
            if maxv < init_val:
                maxv = init_val
        return maxv

# 每次旋转相当于增加了nums的总和，并减去最后一项的n倍