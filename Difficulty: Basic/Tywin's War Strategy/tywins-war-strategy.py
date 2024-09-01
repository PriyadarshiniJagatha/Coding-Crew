#User function Template for python3

def min_soldiers (a, n, k) : 
    sum=0
    d=k
    b=[]
    for i in range(0,n):
        if a[i]%k!=0:
            p=k-(a[i]%k)
        else:
            p=0
        b.append(p)
    b.sort()
    if n%2==0:
        l=n//2
    else:
        l=(n+1)//2
    for i in range(0,l):
        sum=sum+b[i]
    return sum
            
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

for _ in range(0,int(input())):
    n, K = map(int, input().split())
    arr = list(map(int, input().strip().split()))
    ans = min_soldiers(arr, n, K)
    print(ans)





# } Driver Code Ends