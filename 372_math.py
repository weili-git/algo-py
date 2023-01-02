class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        a %= 1337
        x = 0
        for i in b:
            x = (10*x + i) % 1140 # euler
        ans = 1
        for i in range(x):
            ans = ans*a%1337
        return ans
        
# (axb)%c = (a%c x b%c)%c
# a^b%c = a^(b%phi(c))  欧拉-费马降幂