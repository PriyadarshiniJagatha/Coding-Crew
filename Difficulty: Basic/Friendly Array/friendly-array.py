class Solution:
    def calculateFriendliness(self, a):
        sum=0
        n=len(a)
        for i in range(0,n-1):
            if a[i]>a[i+1]:
                sum=sum+a[i]-a[i+1]
            else:
                sum=sum+a[i+1]-a[i]
        if a[n-1]>a[0]:
            sum=sum+a[n-1]-a[0]
        else:
            sum=sum+a[0]-a[n-1]
        return sum



#{ 
 # Driver Code Starts
def main():
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        solution = Solution()
        print(solution.calculateFriendliness(arr))


if __name__ == "__main__":
    main()

# } Driver Code Ends