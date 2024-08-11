#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
#Back-end complete function Template for Python 3
class Solution:
    # Prints average of a prefix array
    def prefixAvg(self, a):
        n=len(a)
        tot=0
        for i in range(0,n):
            tot=tot+a[i]
            av=tot//(i+1)
            a[i]=av
        return a
    

#{ 
 # Driver Code Starts.
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.prefixAvg(arr)
        print(" ".join(map(str, ans)))
# } Driver Code Ends