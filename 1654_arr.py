class Solution:
    def minimumDeletions(self, s: str) -> int:
        cntb, f = 0, 0 # f 代表左边至少需要删除的字符数目
        for ch in s:
            if ch == 'b':
                cntb += 1
            else:
                f = min(cntb, f+1)
        return f