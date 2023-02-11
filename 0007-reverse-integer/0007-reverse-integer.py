class Solution:
    def reverse(self, x: int) -> int:
        res=int(str(abs(x))[::-1])
        if (res.bit_length()>31):
            return 0
        if x<0:
            return -1*res
        else:
            return res
        