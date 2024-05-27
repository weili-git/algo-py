class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 1<<32
        max_int = 0x7FFFFFFF
        min_int = max_int + 1
        while b!=0:
            carry = (a&b) << 1
            a = (a ^ b) % mask # range 0 ~ 2^32-1
            b = carry % mask

        return a if a <= max_int else ~((a % min_int) ^ max_int)
        # positive will be as it is, negative will 
        # 01[1111]
        # 00[1111] remove signal
        # 00[0000] flip lower part
        # 11[1111] flip all