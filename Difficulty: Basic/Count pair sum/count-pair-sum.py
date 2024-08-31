#User function Template for python3

class Solution:
    def countPairs(self,arr1, arr2, x):
        h={}
        c=0
        for i in range(0,len(arr2)):
            h[arr2[i]]=i
        for i in range(0,len(arr1)):
            d=x-arr1[i]
            if d in h:
                c=c+1
        return c



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        x = int(input())
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        ob = Solution()
        l = ob.countPairs(arr1, arr2, x)
        print(l)

# } Driver Code Ends