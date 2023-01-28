class Solution:
    def frequencySort(self, s: str) -> str:
        res=''
        leng=sorted(list(set(s)),key=s.count,reverse=True) 
        for i in leng:
            res=res+i*s.count(i)
        return res