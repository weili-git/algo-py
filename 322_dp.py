def coinChange(self, coins: List[int], amount: int) -> int:
    # 背包问题
    dp = [float("inf")] * (amount+1) # 金额i需要的最少硬币数目

    dp[0] = 0
    for i in range(1, amount+1):
        dp[i] = min(dp[i-c] if i-c>=0 else float("inf") for c in coins) + 1
    return dp[-1] if dp[-1] != float("inf") else -1

# 0-1 背包
# dp[i][j] => 选择0~i的物品, 背包容量j
# 初始化dp[i][0] = 0， dp[0][j]
# dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + value[i])
