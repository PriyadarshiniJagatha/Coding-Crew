#User function Template for python3

class Solution:
    def lenOfLongIncSubArr(self, a):
        c=1
        d=0
        n=len(a)
        for i in range(0,n-1):
            if a[i]<a[i+1]:
                c+=1
            elif c>=d:
                d=c
                c=1
            else:
                c=1
        return max(c,d)
    
    
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')

    t = int(data[0])
    results = []

    for i in range(1, t + 1):
        arr = list(map(int, data[i].split()))
        solution = Solution()
        ans = solution.lenOfLongIncSubArr(arr)
        results.append(ans)

    for result in results:
        print(result)


if __name__ == "__main__":
    main()

# } Driver Code Ends