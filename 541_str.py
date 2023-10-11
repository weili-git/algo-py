class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if len(s) < k:
            r = reversed(s)
            return ''.join(r)
        elif len(s) < k * 2:
            r = reversed(s[:k])
            return ''.join(r) + s[k:]
        else:
            r = reversed(s[:k])
            return ''.join(r) + s[k:k*2] + self.reverseStr(s[k*2:], k)
        
        # a[::-1]