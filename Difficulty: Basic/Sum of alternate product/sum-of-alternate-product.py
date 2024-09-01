#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def altProduct(self, a):
        a.sort()
        n=len(a)
        sum=0
        for i in range(0,n//2):
           sum=sum+a[i]*a[-i-1]
        return sum

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.altProduct(arr)
        print(res)
        # print("~")
        t -= 1


# } Driver Code Ends