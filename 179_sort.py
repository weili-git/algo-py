class N2S:
    def __init__(self, num):
        self.s = str(num)

    def __gt__(self, another):
        a, b = self.s + another.s, another.s + self.s
        return a > b


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        arr = [N2S(n) for n in nums]
        arr.sort(reverse=True)
        ans = "".join([a.s for a in arr])
        if ans[0]=="0": # "00000"
            return "0"
        return ans