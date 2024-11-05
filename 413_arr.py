class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        i = 0
        res = 0
        while i+2 < n:
            j = 0
            while i+j+2 < n and nums[i+1+j] - nums[i+j] == nums[i+2+j] - nums[i+1+j]:
                j += 1
            if j==0:
                i += 1
            else:
                # len == j+2
                # j + (j-1) + ... + 1
                res += (1+j)*j/2
                i = i+j+1
        return int(res)
            