class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum=0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i==j:
                    sum+=mat[i][j]
        res=0 
        y=len(mat[0])-1
        x=0 
        while y>=0:
            res+=mat[x][y]
            x+=1 
            y-=1
        n=len(mat[0])
        if n % 2==0:
            return (res+sum)
        else:
            return res+sum-mat[n//2][n//2]