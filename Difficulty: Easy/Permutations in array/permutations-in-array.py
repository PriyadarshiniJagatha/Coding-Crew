#{ 
 # Driver Code Starts

# } Driver Code Ends
class Solution:
    def isPossible(self, k, a,b):
        n=len(a)
        a.sort()
        b.sort()
        for i in range(0,n):
            if ((a[i]+b[n-1-i])>=k):
                continue
            else:
                return False
        return True
           

#{ 
 # Driver Code Starts.
def main():
    t = int(input().strip())
    for _ in range(t):
        k = int(input().strip())
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        
        ob = Solution()
        ans = ob.isPossible(k, arr1, arr2)
        if ans:
            print("true")
        else:
            print("false")

if __name__ == "__main__":
    main()
# } Driver Code Ends