class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=[i for i in s]
        t=[i for i in t]
        if sorted(s)==sorted(t):
            return True
        return False