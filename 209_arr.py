class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 滑动窗口
        if not nums:
            return 0

        n = len(nums)
        minLen = n + 1
        start = end = 0
        sum = 0
        while end<n:
            sum += nums[end]
            while sum >= target: # 每次加完就得判断，否则end到达n-1就跳出循环，可能不是最优解
                minLen = min(minLen, end-start+1)
                sum -= nums[start]
                start += 1
            end += 1
        return 0 if minLen==n+1 else minLen