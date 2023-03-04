from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # n = len(gas)
        # arr = [gas[i]-cost[i] for i in range(n)]
        #
        # # arr = [0, 0] is impossible since unique solution is guaranteed
        # if n == 1 and arr[0] == 0:
        #     return 0
        #
        # if sum(arr)<0:
        #     return -1
        #
        # for i in range(n):
        #     # [(p, p, n, n), p, n, ...] if the sum less than 0, just step forward
        #     # [p, p, n, n, (p), n, ...]
        #     if arr[i]>0:    # >= will cost much time
        #         gas_ = 0
        #         for j in range(n):
        #             gas_ += arr[(i+j)%n]
        #             if gas_<0:
        #                 i += j
        #                 break
        #         if gas_>=0:
        #             return i
        # return -1
        # 超时
        n = len(gas)
        total = 0
        curr = 0
        start = 0
        for i in range(n):
            total += gas[i] - cost[i]
            curr += gas[i] - cost[i]
            if curr < 0:
                start = i + 1
                curr = 0
        return start if total >= 0 else -1

    # 重点就两句话：
    # 1、两个数组之差的总和必须大于等于0，否则不能完成绕行；反之，一定可以绕行！！！
    # 2、一个站的收益如果小于0，肯定不能作为起点；而连续的多个站也可以等效地看做一个站，如果其累积收益小于0，就跳过，寻找下一个。


    def test(self):
        print(self.canCompleteCircuit([5,1,2,3,4], [4,4,1,5,1])) # [1, -3, 1, -2, 3]

s = Solution()
s.test()