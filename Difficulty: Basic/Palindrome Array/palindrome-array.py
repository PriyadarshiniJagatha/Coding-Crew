
from typing import List


class Solution:
    def isPerfect(self, a : List[int]) -> bool:
        n=len(a)
        c=0
        for i in range(0,n//2):
            if a[i]!=a[-i-1]:
                c=0
                break
            else:
                c=c+1
        return c
            
                
            
        



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        arr = list(map(int, input().strip().split()))

        obj = Solution()
        res = obj.isPerfect(arr)

        if res:
            print("true")
        else:
            print('false')

# } Driver Code Ends