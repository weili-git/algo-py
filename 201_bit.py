import math

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left==right:
            return left
        res = left & right
        diff = right - left
        bits = int(math.log(diff+0.1, 2)) + 1
        res >>= bits
        res <<= bits
        return res
        # 每一位翻转所需要的差值分别都是2的幂次
        # 0     ->  left
        # 1     ->  xxxx,xxx0
        # 2~3   ->  xxxx,xx00
        # 4~7   ->  xxxx,x000
        # 8~15  ->  xxxx,0000