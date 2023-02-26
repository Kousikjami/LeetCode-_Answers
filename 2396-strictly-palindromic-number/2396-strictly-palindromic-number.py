class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def decimalToBinary(num,base):
            if num == 0: 
                return 0
            else:
                return str(decimalToBinary(num//base,base)) + str((num%base)) 
        count=0
        for i in range(2,n-1):
            x=str(int(decimalToBinary(n,i)))
            if x==x[::-1]:
                count+=1
            else:
                return False
        if count==n:
            return True
        return False