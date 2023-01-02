class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        res=[]
        def dfs(cur,temp):
            if len(cur)<=n:
                res.append(cur)
            for i in range(len(temp)):
                if i>0 and temp[i-1]==temp[i]:
                    continue
                dfs(cur+[temp[i]],temp[i+1:])
        dfs([],nums)
        return res
