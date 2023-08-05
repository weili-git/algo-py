class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num
        ro = xor & (~xor + 1) # right most 1
        a = 0
        for num in nums:
            if ro & num:
                a ^= num
        return [a, a^xor]

