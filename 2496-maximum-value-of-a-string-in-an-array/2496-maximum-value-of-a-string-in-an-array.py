class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        mv=0
        for i in strs:
            if i.isdigit():
                mv=max(int(i),mv)
            else:
                mv=max(len(i),mv)
        return mv