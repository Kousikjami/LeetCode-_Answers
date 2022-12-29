class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        res=list(set(ransomNote))
        
        for i in res:
            if i not in magazine or ransomNote.count(i) > magazine.count(i):
                return False
        return True