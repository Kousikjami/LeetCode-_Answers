class Solution:
    def generate(self, n: int) -> List[List[int]]:
        ans=[[1]]
        for x in range(n-1):
            res=[0]+ans[-1]+[0]
            temp=[]
            for i in range(1,len(res)):
                temp.append(res[i-1]+res[i])
            ans.append(temp)
        return ans