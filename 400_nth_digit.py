class Solution:
    def findNthDigit(self, n: int) -> int:
        # 1~9: 9
        # 10~99: 90
        # 100~999: 900
        if n<=9:
            return n
        digit_num = 1
        count = 9
        while n > count * digit_num:
            n -= count * digit_num
            count *= 10
            digit_num += 1

        start_num = pow(10, digit_num-1)
        offset = (n-1)//digit_num
        idx = (n-1)%digit_num

        return int(str(start_num + offset)[idx])
