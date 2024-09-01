class Solution:
    def findTriplet(self, arr):
        n=len(arr)
        h={}
        for i in range(0,n):
            h[arr[i]]=i
        for i in range(0,len(arr)):
            for j in range(i+1,len(arr)):
                s=arr[i]+arr[j]
                if s in h:
                    return True
        return False
                
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
# Position this line where user code will be pasted.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.findTriplet(arr)
        if (res):
            print("true")
        else:
            print("false")
        # print(res)
        # print("~")
        t -= 1

# } Driver Code Ends