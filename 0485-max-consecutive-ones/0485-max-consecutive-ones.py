class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        res=[]
        for i in nums:
            if i==1:
                count+=1
            elif i==0:
                count=0
            res.append(count)    
        return max(res)