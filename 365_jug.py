# 贝祖定理
# 1. 两水壶不能同时不满
# 2. 不满水壶加水无意义
# 3. 不满水浒倒掉无意义

# 因此，每次操作只能给两水壶的总水量增加x或者y

# 满足 ax+by=z 即可，a和b的正负代表加水还是倒空

class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if x + y < z:
            return False
        if x == 0 or y == 0:
            return z == 0 or x + y == z
        return z % math.gcd(x, y) == 0

