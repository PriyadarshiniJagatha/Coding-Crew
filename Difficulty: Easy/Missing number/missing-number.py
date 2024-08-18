
from typing import List


class Solution:
    def missingNumber(self, n : int, a : List[int]) -> int:
        sum=(n*(n+1))//2
        s=0
        n=len(a)
        for i in range(0,n):
            s=s+a[i]
        return sum-s
        



#{ 
 # Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        arr=IntArray().Input(n-1)
        
        obj = Solution()
        res = obj.missingNumber(n, arr)
        
        print(res)
        

# } Driver Code Ends