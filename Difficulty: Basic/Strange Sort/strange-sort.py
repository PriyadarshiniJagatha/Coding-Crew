#User function Template for python3

class Solution:
    def strangeSort (self,a, k):
        n=len(a)
        b=[]
        for i in range(0,k-1):
            b.append(a[i])
        for i in range(k,n):
            b.append(a[i])
        b.sort()
        b.insert(k-1,a[k-1])
        for i in range(0,n):
            a[i]=b[i]
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        ob.strangeSort(arr, k)
        n = len(arr)
        for i in range(n):
            print(arr[i], end=" ")
        print()
        tc -= 1

# } Driver Code Ends