class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum=-10**20
        sum=0
        for i in nums:
            sum=sum+i
            maxsum=max(maxsum,sum)
            if sum<0:
                sum=0
        return maxsum