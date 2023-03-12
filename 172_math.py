class Solution:
    def trailingZeroes(self, n: int) -> int:
        # num of factor 5
        cnt = 0
        while n>=5:
            cnt += n//5
            n //= 5
        return cnt