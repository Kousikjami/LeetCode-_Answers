class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x=[]
        s=s[::-1]
        for i in range(len(s)):
            x=s.split()
        return len(x[0])