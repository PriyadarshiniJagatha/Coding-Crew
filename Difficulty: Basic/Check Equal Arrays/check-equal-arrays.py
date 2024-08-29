# User function Template for python3

class Solution:
    # Function to check if two arrays are equal or not.
    def check(self, a, b) -> bool:
        n=len(a)
        d={}
        for i in a:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for j in b:
            if j not in d or d[j]==0:
                return False
            else:
                d[j]-=1
        return True

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for tc in range(t):
        arr1 = [int(x) for x in input().replace('  ', ' ').strip().split(' ')]
        arr2 = [int(x) for x in input().replace('  ', ' ').strip().split(' ')]
        ob = Solution()
        if ob.check(arr1, arr2):
            print("true")
        else:
            print("false")

# } Driver Code Ends