class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res=[0,0,0]
        for i in nums:
            res[i]+=1
        print(res)
        k=0
        for i in range(len(res)):
            for j in range(res[i]):
                nums[k]=i
                k+=1
    