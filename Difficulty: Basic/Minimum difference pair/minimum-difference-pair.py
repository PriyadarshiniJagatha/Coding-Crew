#User function Template for python3

class Solution:
	def minimum_difference(self, a):
		a.sort()
		mini=max(a)
		for i in range(0,len(a)-1):
	        d=a[i+1]-a[i]
            if d<mini:
	            mini=d
        return mini
		        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		ob = Solution()
		ans = ob.minimum_difference(nums)
		print(ans)
# } Driver Code Ends