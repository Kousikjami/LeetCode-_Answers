class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        target=['']*len(s)
        for i in range(len(s)):
            target[indices[i]]=s[i]
        return ''.join(i for i in target)