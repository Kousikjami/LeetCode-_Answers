class Solution:
    def average(self, s: List[int]) -> float:
        res=0
        s=sorted(s)
        for i in range(1,(len(s)-1)):
            res+=s[i]
        return (res/(len(s)-2))