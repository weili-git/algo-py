class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        number = "" # save the number
        flag = False # check op
        for i in range(len(s)):
            if '0' <= s[i] <= '9':
                number += s[i]
            elif s[i] == ' ':
                continue
            else:
                #########
                stack.append(int(number))
                number = ""
                if flag: # mul or div
                    num1 = stack.pop()
                    op = stack.pop()
                    num2 = stack.pop()
                    if op=="*":
                        stack.append(num1*num2)
                    else:
                        stack.append(num2//num1)
                    flag = False
                #########
                if s[i] == "+":
                    stack.append("+")
                elif s[i] == "-":
                    stack.append("-")
                elif s[i] == "*":
                    stack.append("*")
                    flag = True
                elif s[i] == "/":
                    stack.append("/")
                    flag = True
        #########
        stack.append(int(number))
        number = ""
        if flag: # mul or div
            num1 = stack.pop()
            op = stack.pop()
            num2 = stack.pop()
            if op=="*":
                stack.append(num1*num2)
            else:
                stack.append(num2//num1)
            flag = False
        #########
        res = stack[0]
        ii = (len(stack)-1) // 2
        for i in range(ii):
            if stack[i*2+1] == "+":
                res += stack[i*2+2]
            else:
                res -= stack[i*2+2]
        return res
