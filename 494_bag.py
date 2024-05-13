from scipy.special import comb

class Solution:
    # def findTargetSumWays(self, nums: List[int], target: int) -> int:
    #     # backtrace - timeout
    #     self.num = 0
    #     self.backtrace(nums, target)
    #     return self.num

    # def backtrace(self, nums, target):
    #     if len(nums)==0:
    #         if target==0:
    #             self.num += 1
    #     else:
    #         self.backtrace(nums[1:], target+nums[0])
    #         self.backtrace(nums[1:], target-nums[0])
    # 5 min

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # knapsack
        # int weight!
        # sum - 2*neg = target
        # neg: sum of negative flag number
        s = sum(nums)
        n = len(nums)
        diff = s - target
        if diff<0 or diff%2==1:
            return 0
        neg = diff//2
        dp = [[0 for j in range(neg+1)] for i in range(n+1)]
        dp[0][0] = 1
        for i in range(1, n+1):
            num = nums[i-1]
            for j in range(neg+1):
                dp[i][j] = dp[i-1][j]
                if j>=num:
                    dp[i][j] += dp[i-1][j-num]
        return dp[n][neg]



