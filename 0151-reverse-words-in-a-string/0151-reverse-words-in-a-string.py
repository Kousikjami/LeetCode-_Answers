class Solution:
    def reverseWords(self, s: str) -> str:
        x=""
        res=[]
        for i in s:
            if(i!=" "):
                x+=i
            elif x!="":
                res.append(x)
                x=""
        if x!="":
            res.append(x)
        return " ".join(res[::-1])
  