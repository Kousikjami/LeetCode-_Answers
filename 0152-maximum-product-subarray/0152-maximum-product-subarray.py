class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi=min(nums)
        p=1
        s=1
        for i in range(len(nums)):
            if p==0:
                p=1
            if s==0:
                s=1
            p*=nums[i]
            s*=nums[len(nums)-1-i]
            maxi=max(maxi,max(p,s))
        return maxi