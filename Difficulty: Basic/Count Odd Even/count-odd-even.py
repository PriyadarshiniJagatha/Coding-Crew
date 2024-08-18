#User function Template for python3

class Solution:
	def countOddEven(self, a):
		n=len(a)
		c=0
		o=0
		b=[]
		for i in range (0,n):
		    if a[i]%2==0:
		        c+=1
		o=n-c
		b.append(o)
		b.append(c)
		return b



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    # Testcase input
    testcase = int(input())

    for _ in range(testcase):

        arr = list(map(int, input().split()))

        # Creating an object of the Solution class
        ob = Solution()

        # Calling the function to count even and odd
        res = ob.countOddEven(arr)

        # Printing the result
        print(*res)

# } Driver Code Ends