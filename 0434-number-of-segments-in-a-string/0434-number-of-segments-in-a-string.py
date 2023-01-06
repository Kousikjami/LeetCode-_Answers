class Solution:
    def countSegments(self, s: str) -> int:
        x=[]
        for i in range(len(s)):
            x=s.split()
        return len(x)