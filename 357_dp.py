class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n==0:
            return 1
        elif n==1:
            return 10
        else:
            num = 9
            factor = 9
            for i in range(n-1):
                num *= factor
                factor -= 1
            return self.countNumbersWithUniqueDigits(n-1) + num

# f(0)=1 
# f(1)=10
# f(2)=9*9+f(1)
# f(3)=9*9*8+f(2)
# f(4)=9*9*8*7+f(3)
# 第一位非零
# 选出n位非重复数字的组合，然后加上n-1位以下的结果