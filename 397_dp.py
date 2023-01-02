class Solution:
    def integerReplacement_timeout(self, n: int) -> int:
        dp = [float("inf") for i in range(n+1)]
        dp[1] = 0
        for i in range(2, n+1):
            if i%2==0:
                dp[i] = dp[i//2] + 1
            else:
                # dp[i] = min(dp[i-1], dp[i+1]) + 1
                dp[i] = min(dp[i-1]+1, dp[(i+1)//2] + 2)
        return dp[n]
        # 超时

    def integerReplacement(self, n: int) -> int:
        ans = 0
        val = n
        while val>1:
            if val&1==0:
                ans+=1
                val = val>>1
            elif val!=3 and ((val>>1)&1)!=0: # add 1
                ans+=1
                val+=1
            else:
                ans +=2
                val = val>>1
        return ans

# 看被操作数n二进制编码的最低位：
# （1）如果是0，只需要向右移动一位，就可以将0移掉，只需要一次操作；

# （2）如果是1，则需要先加1或减1操作变成0，之后进行移位操作，
#     才能将1移掉，需要两次操作；

# 故，若n二进制编码比特位中的1越少，0越多，则将n变为1需要执行的
# 操作次数就越少。
# 即，若我们进行一次操作将越多的1变成0，总操作次数就越少。


# 若低位有连续m个1： (仅考虑去掉1需要的操作次数？？)
# （1）减一操作：将m个1都变成m个0需要m次减一操作， 
#     1...00[11...11] ---> 1...00[00...00]，
#     共m次操作；

# （2）加一操作：对最低位加1，由于进位，m个1都会变成0，
#     最高位进位，最终形成高位一个1，低位m个0的形式，
#     高位1再通过一次减1操作（或加1操作）变成0， 
#     1...00[11...11] ---> 1...01[00...00] 
#                     ---> 1...00[00...00]，
#     一次加1操作，一次减1操作（或加1操作），共2次操作。

# 因此，当低位有连续m个1时，减一操作需要m次，
# 加一操作+减一操作（或加1操作）只需要2次；

# 故当 m >= 2时，优先用加一操作（外加一次减一操作或加一操作），
#               只需2次；
#   当 m < 2时，优先用减一操作，只需1次。


# 注意： 当n为3时，二进制为11，由于最终结果要变成1，
#       故统计连续1时，不能将高位的1统计在内，也就是
#       n为3时低位连续1的个数只能算1个。