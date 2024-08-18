
from typing import List

class Solution:
    def search(self, k: int, a: List[int]) -> int:
        n=len(a)
        c=-1
        for i in range(0,n):
            if a[i]==k:
                c=i
                break
        if c!=-1:
            return c+1
        else:
            return -1
        



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())  # Read number of test cases
    for _ in range(t):
        k = int(input())  # Read the element to search
        arr = list(map(int, input().split()))  # Read the array elements

        obj = Solution()
        res = obj.search(k, arr)

        print(res)

# } Driver Code Ends