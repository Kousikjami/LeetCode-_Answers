class Solution:
    def sortSentence(self, s: str) -> str:
        
        n=1
        s=s.split()
        k=len(s)
        x=[0]*k
        for word in s:
            x[int(word[-1])-1]=word[:-1]
        return ' '.join(x)