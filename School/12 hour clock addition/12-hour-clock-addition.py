#User function Template for python3

class Solution:
    def clockSum(self, num1, num2):
        h=(num1+num2)%12
        return h


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        num1, num2 = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.clockSum(num1, num2))

# } Driver Code Ends