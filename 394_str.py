class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        digit = 0
        string = ""
        for i in s:
            if i.isdigit():
                if string != "":
                    stack.append(string)
                    string = ""
                digit *= 10
                digit += int(i)
            elif i=="[":
                stack.append(digit)
                digit = 0
            elif i=="]":
                while not isinstance(stack[-1], int):  # 判断数据类型
                    string = stack.pop() + string
                stack.append(stack.pop() * string)
                string = ""
            else:
                string += i
        return "".join(stack) + string 

