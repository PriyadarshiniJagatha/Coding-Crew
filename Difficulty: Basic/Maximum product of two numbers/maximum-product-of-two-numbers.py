#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:

	def maxProduct(self,a):
	    m1=0
	    m2=0
		for i in range(0,len(a)):
		    if a[i]>m1:
		        m2=m1
		        m1=a[i]
		    elif a[i]>m2:
		        m2=a[i]
		return m2*m1

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.maxProduct(arr)
        print(res)
        t -= 1


# } Driver Code Ends