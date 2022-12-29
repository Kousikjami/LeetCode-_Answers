class Solution:
    def wordPattern(self, p: str, s: str) -> bool:
        """p=list(pattern)
        s1=s.split(" ")
        s=list(s1)
        if len(p)!=len(s):
            return False
        d={}
        for i in range(len(p)):
            if p[i] not in d:
                d[p[i]]=s[i]
            else:
                if s[i] in d.values() or d[p[i]]:
                    return False 
                else:
                    d[p[i]]=s[i]
        return True"""
        words = s.split(' ')
        d=dict()

        if len(p) != len(words): 
            return False
        if len(set(p)) != len(set(words)): 
            return False # for the case w = ['dog', 'cat'] and p = 'aa'

        for i in range(len(words)):
            if words[i] not in d: 
                d[words[i]] = p[i]
            elif d[words[i]] != p[i]: 
                return False
        return True
