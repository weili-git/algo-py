class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ret, flag = 0, 0
        for n in nums: # python only
            if n<0:
                flag += 1
        flag %= 3
        for i in range(32):
            mask = 1<<i
            cnt = 0
            for n in nums:
                if abs(n)&mask!=0: # abs!! python only
                    cnt += 1
            if cnt%3!=0:
                ret |= mask
        return ret if flag==0 else -ret