#User function Template for python3

class Solution:
    def getNumber(self, b,n):
        t=n
        s=""
    	while t!=0:
    	    a=t%b
    	    if a>=10:
    	        a=chr(55+a)
    	    s=s+str(a)
    	    t=t//b
    	return s[::-1]
    	     
    	 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        B = int(input())
        N = int(input())
        ob = Solution()
        ans = ob.getNumber(B, N)
        print(ans)
# } Driver Code Ends