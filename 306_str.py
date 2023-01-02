class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def check(a, b):
            if (a.startswith('0') and a!='0') or (b.startswith('0') and b!='0'):
                return False

            temp = a + b # construct string from two numbers
            a, b = b, str(int(b)+int(a))
            temp += b

            while len(temp) < len(num):
                a, b = b, str(int(b) + int(a))
                temp += b

            return num==temp # compare the string
        
        for j in range(1, len(num)-1):
            for i in range(j):
                if check(num[:i+1], num[i+1:j+1]): # check possible two numbers
                    return True

        return False
    