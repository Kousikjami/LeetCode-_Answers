class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        new=s.split()
        m=len(new)
        n=len(new[m-1])
        return  n
        