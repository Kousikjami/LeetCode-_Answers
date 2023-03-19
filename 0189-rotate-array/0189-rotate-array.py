class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """l=len(nums)
        while k:
            nums[0]=nums[l-1]
            for i in range(len(nums)):
                nums[i-1]=nums[i]
            k-=1
        return nums"""
        k=k%len(nums)
        nums[:]=nums[-k:]+nums[:-k]