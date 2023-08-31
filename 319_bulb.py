class Solution:
    def bulbSwitch(self, n: int) -> int:
        # 一个数的因数成对出现，但平方数的因数（因为重复）会出现奇数次
        return int(math.sqrt(n))