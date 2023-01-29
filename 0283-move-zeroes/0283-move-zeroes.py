class Solution:
    def moveZeroes(self, A: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in A:
            if i==0:
                A.remove(i)
                A.append(0)
        return A