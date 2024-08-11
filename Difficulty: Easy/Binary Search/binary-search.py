#User function template for Python

class Solution:
    def binarysearch(self, a, k):
        n=len(a)
        l=0
        r=n-1
        while (l<=r):
            mid=(l+r)//2
            if a[mid]==k:
                return mid
            elif a[mid]<k:
                l=mid+1
            else:
                r=mid-1
        return -1
                
                



#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        k = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.binarysearch(arr, k)
        print(res)

# } Driver Code Ends