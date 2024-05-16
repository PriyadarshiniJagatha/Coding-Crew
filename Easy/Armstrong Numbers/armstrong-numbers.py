#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        sum=0
        t=n
        while (t!=0):
            a=t%10
            sum=sum+a**3
            t=t//10
        if n==sum:
            return "Yes"
        else:
            return "No"


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = input()
        n=int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))
# } Driver Code Ends