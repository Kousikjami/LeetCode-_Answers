class Solution:
    def check(self, nums: List[int]) -> bool:
        res=True
        i=0
        for i in range(len(nums)-1):
            if(nums[i]>nums[i+1]):
                if res!=False:
                    res=False
                else:
                    return False
        if nums[0]<nums[len(nums)-1] and res==False:
            return False
        return True