class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res=[]
        for i in range(n):
            s=start+2*i
            res.append(s)
        x=0
        for i in range(len(res)):
            x=x^res[i]
        return x
        