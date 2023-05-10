class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res1=0
        res2=0
        for i in range(len(num1)):
            res1=(res1*10)+(ord(num1[i])-48)
        for i in range(len(num2)):
            res2=(res2*10)+(ord(num2[i])-48)
        return str(res1*res2)