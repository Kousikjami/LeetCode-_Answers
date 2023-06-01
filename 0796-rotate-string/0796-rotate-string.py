class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if s==goal:
            return True
        s=list(s)
        #goal=list(goal)
        temp=[0]*len(s)
        for i in range(len(s)):
            s.append(s[i])
            temp[:]=s[i+1:]
            #print(temp)
            if ''.join(temp)==goal:
                return True
        return False