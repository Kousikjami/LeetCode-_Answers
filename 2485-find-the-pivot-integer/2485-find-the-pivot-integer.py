class Solution:
    def pivotInteger(self, n: int) -> int:
        ans=-1
        l=0
        r=0
        for i in range(1,n+1):
            l+=i
        for j in range(n,-1,-1):
            l-=j
            if l==r:
                ans=j
            r+=j
        return ans