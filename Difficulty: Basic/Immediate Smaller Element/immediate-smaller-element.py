#User function Template for python3
class Solution:

	def immediateSmaller(self,a,n):
	    b=[]
		for i in range(0,n-1):
		    if a[i+1]<a[i]:
	            a[i]=a[i+1]
		    else:
		        a[i]=-1
		a[n-1]=-1
		return a


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tcs=int(input())

    for _ in range(tcs):
        n=int(input())
        arr=[int(x) for x in input().split()]
        ob = Solution()
        ob.immediateSmaller(arr,n)
        for x in arr:
            print(x, end=" ")
        print()
# } Driver Code Ends