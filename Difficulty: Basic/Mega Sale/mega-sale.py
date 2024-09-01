class Solution:
    def maxProfit(self, m, arr):
        n=len(arr)
        sum=0
        arr.sort()
        for i in range(0,min(m,n)):
            if arr[i]<0:
                sum=sum+arr[i]
        return -1*sum


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        k = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.maxProfit(k, arr))
# } Driver Code Ends