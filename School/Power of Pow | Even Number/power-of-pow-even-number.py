class Solution:
	def sum_of_square_evenNumbers(self, n):
	    s=(4*n*(n+1)*(2*n+1))//6
		return s


#{ 
 # Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.sum_of_square_evenNumbers(n)
		print(ans)
# } Driver Code Ends