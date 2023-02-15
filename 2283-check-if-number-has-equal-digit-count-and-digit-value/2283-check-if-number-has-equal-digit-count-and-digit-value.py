class Solution:
    def digitCount(self, num: str) -> bool:
        s=[int(i) for i in num]
        for i in range(len(s)):
            if s[i]!=s.count(i):
                return False
        return True