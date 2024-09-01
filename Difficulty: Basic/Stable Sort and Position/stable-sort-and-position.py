class Solution:
    def getIndexInSortedArray(self, a, n, k):
        l=0
        for i in range(0,n):
            if a[i]<a[k] or (a[i]==a[k])and i<k:
                l+=1
        return l
            


#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    
    t=int(input())
    for _ in range(0,t):
        l=list(map(int,input().split()))
        n=l[0]
        k=l[1]
        a = list(map(int,input().split()))
        ob = Solution()
        ans=ob.getIndexInSortedArray(a,n,k)
        print(ans)
# } Driver Code Ends