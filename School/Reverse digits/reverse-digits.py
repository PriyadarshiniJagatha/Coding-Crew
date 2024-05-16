#User function Template for python3

class Solution:
	def reverse_digit(self, n):
		t=n
		sum=0
		while t>0:
		    a=t%10
		    sum=sum*10+a
		    t=t//10
		return sum


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.reverse_digit(n)
		print(ans)
# } Driver Code Ends