#User function Template for python3
import math as m
class Solution:
	def findFocalLength(self, R, type):
		if type=="concave":
		    return m.floor(R/2)
        elif type=="convex":
		    return m.floor(-R/2)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		type = input()
		R = float(input())
		ob = Solution()
		ans = ob.findFocalLength(R, type)
		print(ans)
# } Driver Code Ends