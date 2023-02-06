class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        result=[]
        s=0
        for i in range(len(accounts)):
            s=0
            for j in range(len(accounts[i])):
                s=s+accounts[i][j]
            result.append(s)
        return max(result)