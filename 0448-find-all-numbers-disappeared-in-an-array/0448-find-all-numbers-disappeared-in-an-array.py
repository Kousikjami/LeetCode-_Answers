class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=set(nums)
        original=set(range(1,len(nums)+1))
        res=list(original-n)
        return res