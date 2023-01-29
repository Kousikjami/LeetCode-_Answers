class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        x=[]
        s=s.split(" ")
        for i in range(k):
            x.append(s[i])
        return ' '.join(x)
    #.join([str(elem) for elem in s])