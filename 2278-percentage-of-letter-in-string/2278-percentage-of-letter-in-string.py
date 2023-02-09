class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        return int((len([i for i in s if i==letter])/len(s))*100)