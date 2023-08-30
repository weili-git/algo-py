class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # the smallest in lexicographical order
        cnt = [0] * 26
        vis = [False] * 26
        for ch in s:
            cnt[ord(ch)-97] += 1

        stack = []
        for ch in s:
            if not vis[ord(ch)-97]:
                while stack and stack[-1] > ch:
                    top = ord(stack[-1]) - 97
                    if cnt[top] > 0:
                        vis[top] = False
                        stack.pop()
                    else:
                        break
                vis[ord(ch)-97] = True
                stack.append(ch)
            cnt[ord(ch)-97] -= 1
        return "".join(stack)