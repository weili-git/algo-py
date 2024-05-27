class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.temp = []
        self.dfs(0, float("-inf"), nums)
        return self.res

    def dfs(self, cur, last, nums):
        if cur==len(nums):
            if len(self.temp)>=2:
                self.res.append(self.temp.copy())
            return
        if nums[cur]>=last:
            self.temp.append(nums[cur]) # select
            self.dfs(cur+1, nums[cur], nums)
            self.temp.pop()
        if nums[cur]!=last:
            self.dfs(cur+1, last, nums)

        # for repeated items a, a, a, a
        # selection will be
        # [1, 1, 1, 1]
        # [0, 1, 1, 1]
        # [0, 0, 1, 1]
        # [0, 0, 0, 1]
        # [0, 0, 0, 0]


