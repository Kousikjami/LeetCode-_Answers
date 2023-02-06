class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        keys={'type':0,'color':1,'name':2}
        x=keys[ruleKey]
        c=0
        for i in items:
            if i[x]==ruleValue:
                c=c+1
        return c