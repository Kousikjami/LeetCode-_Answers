class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res=[]
        res1=[0,0]
        for i in range(len(nums)):
            if nums[i]==target:
                res.append(i)
        if len(res)>0:
            res1[0]=res[0]
            res1[1]=res[-1]
        else:
            return [-1, -1]
        return res1