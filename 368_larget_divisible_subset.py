class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # 不一定是指数
        # [3, 12]
        # [15, 18, 30, 60, 90, 120] -> [15, 30, 60, 120]
        nums.sort()
        n = len(nums)
        f, g = [0 for i in range(n)], [0 for i in range(n)]
        # f[i]表示以nums[i]结尾的最长【整数子集】的长度
        for i in range(n):
            length, prev = 1, i
            for j in range(i):
                if nums[i] % nums[j]==0:
                    if f[j] + 1 > length: # 可接上以nums[j]结尾的【整数子集】，并且比当前查询的还要长，更新最值
                        length = f[j] + 1
                        prev = j
            f[i] = length
            g[i] = prev # 生成路径，方便输出对应的集合
        max_len = idx = -1
        for i in range(n):
            if f[i] > max_len:
                max_len = f[i]
                idx = i
        ans = []
        while len(ans) < max_len:
            ans.append(nums[idx])
            idx = g[idx]
        ans.reverse()
        return ans

    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        f = [[x] for x in nums] # answer at nums[i]
        for j in range(len(nums)):
            for i in range(j):
                if nums[j]%nums[i]==0 and len(f[i])+1 > len(f[j]):
                    f[j] = f[i] + [nums[j]]
        return max(f, key=len)
