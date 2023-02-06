class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        x=sum(nums)
        dig=[]
        for i in nums:
            for j in str(i):
                dig.append(int(j))
        y=sum(dig)
        return x-y