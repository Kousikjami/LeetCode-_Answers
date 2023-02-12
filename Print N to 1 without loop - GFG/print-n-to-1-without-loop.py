#User function Template for python3
def num(i,n):
    if i<1:
        return
    print(i,end=" ")
    num(i-1,n)
class Solution:
    def printNos(self, n):
        # Code here
        num(n,n)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printNos(N)
        print()
# } Driver Code Ends