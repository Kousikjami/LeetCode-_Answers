class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        s=[str(i) for i in num]
        res=int("".join(s))
        res=res+k
        return [int(i) for i in str(res)]