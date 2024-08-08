#User function Template for python3

# arr is the array
# n is the number of elements in array
def printAl(arr):
    n=len(arr)
    for i in range(0,n):
        if i%2==0:
            print(arr[i],end=" ")

    

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        arr = list(map(int, input().split()))
        printAl(arr)
        print()

# } Driver Code Ends