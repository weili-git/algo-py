class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if k>len(s):
            return 0
        for c in set(s):
            if s.count(c)<k: # c当作分割符，因为c不可能包含在符合条件的最长子字符串中
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)