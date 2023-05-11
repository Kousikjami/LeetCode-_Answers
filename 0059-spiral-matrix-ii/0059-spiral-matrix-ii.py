class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        top=0
        bottom=n-1
        left=0
        right=n-1
        d=1
        res=[]
        for j in range(n):
            res.append([0]*n)
        while top<=bottom and left<=right:
            for i in range(left,right+1):
                res[top][i]=d
                d+=1
            top+=1
            for i in range(top,bottom+1):
                res[i][right]=d
                d+=1
            right-=1
            if top<=bottom:
                for i in range(right,left-1,-1):
                    res[bottom][i]=d
                    d+=1
                bottom-=1
            if left<=right:
                for i in range(bottom,top-1,-1):
                    res[i][left]=d
                    d+=1
                left+=1
        return res