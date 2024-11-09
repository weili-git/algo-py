class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # n = len(nums)
        # if len(nums)==1:
        #     return False
        
        # possible = {nums[0]}
        # for i in range(1, n):
        #     next_possible = set()
        #     for item in possible:
        #         next_possible.add(item + nums[i])
        #         next_possible.add(abs(item-nums[i]))
        #     possible = next_possible
        # return 0 in possible

        # 0-1背包问题变形，离散特性
        # s = sum(nums)
        # if s&1==1:
        #     return False
        # n = len(nums)
        # target = s//2
        # dp = [[False for j in range(target+1)] for i in range(n)]

        # dp[0][0] = True # 用于合并单纯放入物品i时的情况
        # if nums[0] <= target: # 防止越界
        #     dp[0][nums[0]] = True

        # for i in range(1, n):
        #     for j in range(target+1):
        #         dp[i][j] = dp[i-1][j] # 不选物品i，即照抄上一行

        #         if nums[i] <= j:
        #             dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]] # 照抄or如果之前能放j-nums[i]则置True
        #     if dp[i][target]==True: # 已经提前找到
        #         return True
        # return dp[n-1][target]

        # 还能继续优化成一维dp
        n = len(nums)
        if n < 2:
            return False
        
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2
        dp = [True] + [False] * target
        for i, num in enumerate(nums):
            for j in range(target, num - 1, -1):
                dp[j] |= dp[j - num]
        
        return dp[target]
