#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
#User function Template for python3

class Solution:
    def get_min_max(self, a):
        maxi=0
        mini=50000000000
        b=[]
        n=len(a)
        for i in range(0,n):
            if a[i]<mini:
                mini=a[i]
            if a[i]>maxi:
                maxi=a[i]
        b.append(mini)
        b.append(maxi)
        return b
    

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        mn, mx = ob.get_min_max(arr)
        print(mn, mx)
        t -= 1


# } Driver Code Ends