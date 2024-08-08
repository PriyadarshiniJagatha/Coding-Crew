# Your task is to complete this function
# Function should return true/false
def PalinArray(arr):
    n=len(arr)
    for j in range(0,n):
        k=str(arr[j])
        for i in range(len(k)//2):
            if k[i]==k[-i-1]:
                c=1
            else:
                c=0
                return False
                break
    if c==1:
        return True
    



#{ 
 # Driver Code Starts
# Driver Program
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        arr = list(map(int, input().strip().split()))
        if PalinArray(arr):
            print("true")
        else:
            print("false")
# Contributed By: Harshit Sidhwa

# } Driver Code Ends