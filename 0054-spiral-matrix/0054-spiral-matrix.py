class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top=0
        bottom=len(matrix)-1
        left=0
        right=len(matrix[0])-1
        d=0
        res=[]
        while top<=bottom and left<=right:
            if d==0:
                for i in range(left,right+1):
                    res.append(matrix[top][i])
                top+=1
                
            elif d==1:
                for i in range(top,bottom+1):
                    res.append(matrix[i][right])
                right-=1
                
            elif d==2:
                for i in range(right,left-1,-1):
                    res.append(matrix[bottom][i])
                bottom-=1
                
            elif d==3:
                for i in range(bottom,top-1,-1):
                    res.append(matrix[i][left])
                left+=1
            d=(d+1)%4
                
        return res
    