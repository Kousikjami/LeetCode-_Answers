class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res=[]
        for i in range(n):
            s=start+2*i
            res.append(s)
        res1 = reduce(lambda x, y: x ^ y, res)
        return res1
        