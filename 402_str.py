class Solution:
    def __init__(self) -> None:
        print(self.removeKdigits("1234321", 3))

    def removeKdigits(self, num: str, k: int) -> str:
        if k==len(num): # remove all digits
            return "0"
        stack = []
        for digit in num:
            # 之前肯定是递增的，否则k已经用完。
            while k>0 and len(stack)>0 and int(stack[-1])>int(digit):
                stack.pop()
                k -= 1
            stack.append(digit)
            # print intermediate result
            # for item in stack:
            #     print(item, end=" ")
            # print("")
            
        if k>0:
            stack = stack[:-k]
        
        return "".join(stack).lstrip("0") or "0"
                

Solution()


