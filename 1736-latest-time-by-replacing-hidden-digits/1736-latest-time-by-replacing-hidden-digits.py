class Solution:
    def maximumTime(self, time: str) -> str:
        x=[i for i in time]
        #print(x)
        if x[0]=='?':
            if x[1]=="?":
                x[0]="2"
            elif x[1]>"3":
                x[0]="1"
            else:
                x[0]="2"
        if x[1]=="?":
            if x[0]<="1":
                x[1]="9"
            else:
                x[1]="3"
        if x[3]=="?":
            x[3]="5"
        if x[4]=="?":
            x[4]="9"
        #print(x)
        return ''.join(x)
        
        
        