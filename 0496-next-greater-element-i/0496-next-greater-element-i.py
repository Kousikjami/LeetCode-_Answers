class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums1)):
            count=0
            for j in range(len(nums2)):
                if nums1[i]==nums2[j]:
                    for k in range(j+1,len(nums2)):
                        if nums2[k]>nums2[j]:
                            count+=1
                            res.append(nums2[k])
                            break
                    if count==0:
                        res.append(-1)
        return res