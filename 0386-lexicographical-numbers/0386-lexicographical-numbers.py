class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        x=[]
        for i in range(1,n+1):
            x.append(i)
        s=[str(i) for i in x]
        s.sort()
        return [int(i) for i in s]