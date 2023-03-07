class Solution:
    def countDigits(self, num: int) -> int:
        n=num
        count=0
        while n>0:
            x=n%10
            if num%x==0:
                count+=1
            n=n//10
        return count