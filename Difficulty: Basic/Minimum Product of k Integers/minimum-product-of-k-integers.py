#User function Template for python3

class Solution:
    def minProduct(self, a, k): 
        a.sort()
        p=1
        n=len(a)
        for i in range(0,min(n,k)):
            p=p*a[i]
        return p%1000000007
      



#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Position this line where user code will be pasted.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        k = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.minProduct(arr, k)
        print(res)
        t -= 1

# } Driver Code Ends