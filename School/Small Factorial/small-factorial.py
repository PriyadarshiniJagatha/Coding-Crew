#User function Template for python3

class Solution:
	def find_fact(self, n):
		p=1
		for i in range (1,n+1):
		    p=p*i
		return p


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.find_fact(n)
		print(ans)

# } Driver Code Ends