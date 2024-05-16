#User function Template for python3

class Solution:
    def findNthTerm(self, n):
        s=1+((n-1)*(2*2+(n-2))//2)
        return s
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.findNthTerm(N))
# } Driver Code Ends