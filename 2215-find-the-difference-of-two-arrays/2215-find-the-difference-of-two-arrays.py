class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        l1=[]
        l2=[]
        s1=set(nums1)
        nums1=list(s1)
        s2=set(nums2)
        nums2=list(s2)
        for i in range(len(nums1)):
            if nums1[i] not in s2:
                l1.append(nums1[i])
        for i in range(len(nums2)):
            if nums2[i] not in s1:
                l2.append(nums2[i])
        res=[]
        res.append(l1)
        res.append(l2)
        return res