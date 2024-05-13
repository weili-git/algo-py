class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.res = []
        self.path = []
        self.k = k
        self.backtrace(n)
        return self.res

    def backtrace(self, left_sum):
        if len(self.path)==self.k and left_sum==0:
            t = self.path.copy()
            self.res.append(t)
        else:
            last_digit = self.path[-1] if self.path else 0
            for i in range(last_digit+1, min(9, left_sum)+1):
                self.path.append(i)
                self.backtrace(left_sum-i)
                self.path.pop()