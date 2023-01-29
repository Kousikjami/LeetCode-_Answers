class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=0
        #nums=list(set(i for i in nums))
        nums[:]=sorted(list(set(nums)))
        return len(nums)