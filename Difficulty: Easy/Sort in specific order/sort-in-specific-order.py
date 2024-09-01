class Solution:
    def sortIt(self, a):
        n=len(a)
        b=[]
        c=[]
        for i in range(0,n):
            if a[i]%2==0:
                b.append(a[i])
            else:
                c.append(a[i])
        c.sort(reverse=True)
        b.sort()
        for i in range(0,len(c)):
            a[i]=c[i]
        for i in range(len(c),len(a)):
            a[i]=b[i-len(c)]


        
            
        
        
            
            
#{ 
 # Driver Code Starts
# Initial Template for Python 3


def main():
    T = int(input())
    while T > 0:
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        ob.sortIt(arr)
        print(*arr)
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends