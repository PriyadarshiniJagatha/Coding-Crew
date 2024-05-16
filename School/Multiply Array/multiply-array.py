#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def longest(self, arr, n):
        p=1
        for i in range(0,n):
            p=p*arr[i]
        return p
    


#{ 
 # Driver Code Starts.
    

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.longest(arr, n))

        T -= 1


if __name__ == "__main__":
    main()





# } Driver Code Ends