class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s=list(set(nums))
        n=len(nums)/2
        for i in s:
            if nums.count(i)>n:
                return i