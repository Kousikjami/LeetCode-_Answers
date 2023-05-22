class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        i=0
        res=[]
        while i<len(nums):
            if nums[i]==target:
                res.append(i)
            i+=1
        if len(res)>0:
            return [res[0],res[-1]]
        return [-1, -1]