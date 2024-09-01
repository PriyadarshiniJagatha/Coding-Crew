#User function Template for python3


class Solution:
    def minDiff(self,arr,K):
        arr.sort()
        N=len(arr)
        res = arr[N-1]-arr[0]
        for i in range(N-K+1):
            res = min(res,arr[i+K-1]-arr[i])
        return res







#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        ans = ob.minDiff(arr, k)
        print(ans)
        tc -= 1

# } Driver Code Ends