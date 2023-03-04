from functools import reduce
from math import gcd


class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        # return reduce(gcd, nums)==1
        return gcd(*nums) == 1
        # 裴蜀定理