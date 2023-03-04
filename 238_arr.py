class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 0 once, 0 twice
        product = 1
        n = len(nums)
        n_zero = 0
        for i in range(n):
            if nums[i]==0:
                n_zero += 1
                if n_zero>=2:
                    return [0 for num in nums]
            else:
                product *= nums[i]
        if n_zero==1:
            return [(0 if num!=0 else product) for num in nums]
        else:
            return [product//num for num in nums]

    def productExceptSelf(self, nums: List[int]) -> List[int]: # without divison
        n = len(nums)
        left = right = 1
        res = [1] * n
        for i in range(n):
            res[i] *= left
            left *= nums[i]

            res[n-1-i] *= right
            right *= nums[n-1-i]
        return res
