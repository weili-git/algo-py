class Solution:
    def lastRemaining(self, n: int) -> int:
        first = 1
        step = 1
        remain = n
        isLeft = True
        while remain>1:
            if isLeft or (remain&1 == 1): # key
                first += step
            isLeft = not isLeft
            step <<= 1
            remain >>= 1
        return first