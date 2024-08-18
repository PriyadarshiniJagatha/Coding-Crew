#User function Template for python3

class Solution:
    def rotate(self, a):
        n=len(a)
        t=a[n-1]
        for i in range(n,0,-1):
            a[i-1]=a[i-2]
        a[0]=t
        return a
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ob.rotate(arr)
        print(" ".join(map(str, arr)))
        t -= 1

# } Driver Code Ends