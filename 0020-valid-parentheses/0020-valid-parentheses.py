class Solution:
    def isValid(self, s: str) -> bool:
        while s!="":
            if '()' in s:
                s=s.replace('()',"")
            elif '[]' in s:
                s=s.replace('[]',"")
            elif '{}' in s:
                s=s.replace('{}',"")
            else:
                break
        return s==""