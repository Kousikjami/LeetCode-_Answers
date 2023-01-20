class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x=0
        y=0
        m=[i for i in moves]
        for i in m:
            if i=='U':
                x+=1
            elif i=='D':
                x-=1
            elif i=='L':
                y+=1
            else:
                y-=1
        if x==0 and y==0:
            return True
        else:
            return False