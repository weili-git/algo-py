class Solution:
    def numberToWords(self, num: int) -> str:
        if num==0: return "Zero"
        words4 = ["", "Thousand", "Million", "Billion"]
        i = 0
        res = ""
        while num!=0:
            tri = num%1000
            if tri==0:
                pass
            elif i==0:
                res = self.ToEnglish(tri)
            elif res=="":
                res = self.ToEnglish(tri) + " " + words4[i]
            else:
                res = self.ToEnglish(tri) + " " + words4[i] + " " + res
            i += 1
            num //= 1000
        return res

    def ToEnglish(self, num):
        words1 = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        words2 = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen",
                "Nineteen"]
        words3 = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        a = num % 10
        b = (num // 10) % 10
        c = (num // 100) % 10

        if c == 0:
            res = ""
        else:
            if b!=0 or a!=0:
                res = words1[c] + " Hundred "
            else:
                res = words1[c] + " Hundred"
                return res

        if b == 0:
            res = res + words1[a]
            return res
        elif b == 1:
            res = res + words2[a]
            return res
        else:
            res = res + words3[b]

        if a != 0:
            res = res + " " + words1[a]

        return res