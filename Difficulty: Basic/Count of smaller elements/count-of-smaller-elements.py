#User function Template for python3

class Solution:
    def countOfElements(self, x, arr):
        n=len(arr)
        c=0
        for i in range(0,n):
            if arr[i]<=x:
                c+=1
        return c




#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Position this line where user code will be pasted.

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    t = int(data[0])
    index = 1
    for _ in range(t):
        x = int(data[index])
        index += 1
        arr = list(map(int, data[index].split()))
        index += 1
        obj = Solution()
        ans = obj.countOfElements(x, arr)
        print(ans)

# } Driver Code Ends