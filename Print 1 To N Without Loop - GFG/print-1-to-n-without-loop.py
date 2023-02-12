#User function Template for python3
def final(i,N):
    if i>N:
        return
    print(i,end=" ")
    final(i+1,N)
class Solution:    
    #Complete this function
    def printNos(self,N):
        #Your code here
        final(1,N)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math




def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        ob=Solution()
        
        ob.printNos(N)
        print()
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends