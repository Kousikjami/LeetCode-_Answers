class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        DoVisited=set()
        for i in nums:
            if i not in DoVisited:
                DoVisited.add(i)
            else:
                return i