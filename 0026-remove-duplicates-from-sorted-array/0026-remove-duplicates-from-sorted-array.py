class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res=list(set(nums))
        nums[:]=res
        nums.sort()
        return len(nums)
    
